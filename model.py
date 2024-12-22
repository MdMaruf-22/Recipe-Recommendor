from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import numpy as np

def train_model(ingredient_matrix, data, total_tree=100, max_depth=10):
    labels = np.arange(len(data))
    X_train, X_test, y_train, y_test = train_test_split(
        ingredient_matrix, labels, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(n_estimators=total_tree, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)

    # Generate confusion matrix
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    return model, cm
