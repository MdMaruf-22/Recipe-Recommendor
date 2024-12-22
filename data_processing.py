import pandas as pd

def load_and_preprocess_data():
    dataset_path = 'subset_dataset.csv'
    data = pd.read_csv(dataset_path)
    data = data.dropna(subset=['title', 'ingredients', 'link'])

    def clean_ingredients(ingredients):
        ingredients = ingredients.strip("[]").replace('"', '').replace("'", "")
        return ingredients

    data['ingredients'] = data['ingredients'].apply(clean_ingredients)
    data['directions'] = data['directions'].apply(lambda x: x.strip("[]").replace('"', '').replace("'", ""))
    return data
