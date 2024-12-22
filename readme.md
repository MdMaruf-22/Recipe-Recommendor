# 🍳 Recipe Recommender System  

Welcome to the **Recipe Recommender System**, a machine learning-powered app that helps you discover the best recipes based on the ingredients you have! Just enter a list of ingredients, and our system will provide personalized recipe suggestions complete with ingredients and step-by-step directions.

---

## 🌟 Features

- **Ingredient-Based Search**: Simply input the ingredients you have, and get recipes tailored to your kitchen.
- **Interactive UI**: Built with **Streamlit** for a clean, user-friendly experience.
- **Fast Recommendations**: Uses a **Random Forest Classifier** and **CountVectorizer** to provide accurate results.
- **Scalable Dataset**: Built using a dataset of over **2 million recipes** from [RecipeNLG](https://www.kaggle.com/datasets/paultimothymooney/recipenlg).

---

## 📚 Dataset

This project uses the **RecipeNLG dataset**, which contains over **2 million recipes** with detailed information such as ingredients, directions, and links. You can find the dataset [here](https://www.kaggle.com/datasets/paultimothymooney/recipenlg).

---

## 🛠️ Setup and Installation

Follow these steps to get the project up and running:

### 1. Clone the Repository
git clone https://github.com/MdMaruf-22/recipe-recommender.git
cd recipe-recommender
### 2.Install Dependencies
Ensure you have Python 3.8+ installed. Install the required Python libraries:
pip install -r requirements.txt
### 3. Clone the Repository
 Download the Dataset
 Download the RecipeNLG dataset, and place the file subset_dataset.csv in the root directory of the project.
 Link: https://www.kaggle.com/datasets/paultimothymooney/recipenlg
### 4.Run the application
Launch the Streamlit app:
streamlit run app.py

## 🧪 How It Works
Preprocessing: The dataset is cleaned and ingredients are tokenized.
Vectorization: Ingredients are vectorized using CountVectorizer for machine learning compatibility.
Model Training: A RandomForestClassifier is trained to predict recipes based on ingredients.
Recommendation: Based on user input, the app ranks and filters recipes to provide the top results.

## 🌟 Example
Start the app.
Enter ingredients, e.g., tomato, onion, garlic.
Get personalized recipe recommendations like this:
Recipe Name: Tomato Soup
Ingredients: Tomato, Onion, Garlic, Salt, Pepper
Directions: 1. Chop tomatoes. 2. Sauté onions...

