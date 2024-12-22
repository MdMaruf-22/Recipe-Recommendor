import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from data_processing import load_and_preprocess_data
from vectorization import vectorize_ingredients
from model import train_model
from recommendations import recommend_recipes

def main():
    st.title("Recipe Recommender System 🍳")
    st.write("Enter a list of ingredients, and get personalized recipe recommendations!")

    @st.cache_resource
    def load_backend():
        data = load_and_preprocess_data()
        vectorizer, ingredient_matrix = vectorize_ingredients(data)
        model, cm = train_model(ingredient_matrix, data)
        return data, vectorizer, model, cm

    data, vectorizer, model, cm = load_backend()

    # Display the confusion matrix
    st.write("### Model Confusion Matrix:")
    fig, ax = plt.subplots(figsize=(8, 6))
    ConfusionMatrixDisplay(confusion_matrix=cm).plot(ax=ax)
    st.pyplot(fig)

    # Take user input
    user_input = st.text_input("Enter ingredients (comma-separated):", "")
    if user_input:
        st.write("Searching for recipes...")
        recommendations = recommend_recipes(user_input, vectorizer, model, data)
        if not recommendations.empty:
            st.write("### Recommended Recipes:")
            for _, row in recommendations.iterrows():
                st.subheader(row['title'])

                ingredients = row['ingredients'].split(', ')
                st.markdown("#### Ingredients:")
                for i, ingredient in enumerate(ingredients, 1):
                    st.markdown(f"{i}. {ingredient.capitalize()}")

                directions = row['directions'].split(', ')
                st.markdown("#### Directions:")
                for i, step in enumerate(directions, 1):
                    st.markdown(f"{i}. {step.strip().capitalize()}")

                st.markdown("---")
        else:
            st.error("No matching recipes found!")

if __name__ == "__main__":
    main()
