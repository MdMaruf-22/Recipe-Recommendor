from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import csr_matrix

def vectorize_ingredients(data, max_features=500):
    vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','), max_features=max_features)
    ingredient_matrix = vectorizer.fit_transform(data['ingredients'])
    return vectorizer, csr_matrix(ingredient_matrix)
