import numpy as np

def recommend_recipes(user_input, vectorizer, model, data, top_n=3):
    user_vector = vectorizer.transform([user_input])
    predictions = model.predict_proba(user_vector)[0]
    ranked_indices = np.argsort(predictions)[::-1]

    user_ingredients = [ingredient.strip().lower() for ingredient in user_input.split(',')]
    filtered_recipes = []
    for idx in ranked_indices:
        recipe_ingredients = data.iloc[idx]['ingredients'].lower()
        if all(ingredient in recipe_ingredients for ingredient in user_ingredients):
            filtered_recipes.append(idx)

    final_indices = filtered_recipes[:top_n]
    top_recipes = data.iloc[final_indices]
    return top_recipes[['title', 'ingredients', 'directions']]
