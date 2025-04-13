import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def load_data():
    """
    Load the Iris dataset from scikit-learn.
    Returns:
        X_train, X_test, y_train, y_test: Training and testing data and labels.
    """
    # Load Iris dataset
    iris = load_iris()
    X = iris.data  # Features
    y = iris.target  # Labels

    # Split the dataset into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    """
    Train a simple classification model using Decision Tree Classifier.
    Args:
        X_train: Training features.
        y_train: Training labels.

    Returns:
        model: Trained machine learning model.
    """
    # Initialize the classifier
    model = DecisionTreeClassifier(random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    return model


def save_model(model, filename="model.joblib"):
    """
    Save the trained model to a file using joblib.
    Args:
        model: Trained machine learning model.
        filename: File name to save the model (default is "model.joblib").
    """
    # Save the model to a file
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")


if __name__ == "__main__":
    # Load data
    X_train, X_test, y_train, y_test = load_data()

    # Train the model
    model = train_model(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model's performance
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    # Save the trained model
    save_model(model)
