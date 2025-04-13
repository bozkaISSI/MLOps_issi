import joblib
import numpy as np


def load_model(filename="model.joblib"):
    """
    Load the trained machine learning model from a file.
    Args:
        filename: File name from which to load the model (default is "model.joblib").

    Returns:
        model: Loaded machine learning model.
    """
    model = joblib.load(filename)
    print(f"Model loaded from {filename}")
    return model


def predict(model, features):
    """
    Use the trained model to make predictions.
    Args:
        model: Trained machine learning model.
        features: Features for which to make predictions (numpy array or list).

    Returns:
        str: Predicted class as a string.
    """
    # Make predictions
    prediction = model.predict([features])

    # Convert prediction to a string (since we are predicting class labels)
    return f"Predicted class: {prediction[0]}"


if __name__ == "__main__":
    # Load the model
    model = load_model()

    # Example features from the Iris dataset (for testing)
    example_features = [5.1, 3.5, 1.4, 0.2]  # Example feature for an Iris flower (setosa)

    # Make a prediction
    prediction = predict(model, example_features)
    print(prediction)
