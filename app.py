from fastapi import FastAPI
from inference import load_model, predict
from api.models.iris import PredictRequest, PredictResponse
from fastapi import HTTPException

# Initialize the FastAPI app
app = FastAPI()

# Global model variable
model = None


# Load the model during the app startup
@app.on_event("startup")
def load_model_on_startup():
    global model
    model = load_model()  # Load the model using the inference.py load_model function


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict_flower(request: PredictRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded")

    # Extract features from the request
    features = [request.sepal_length, request.sepal_width, request.petal_length, request.petal_width]

    # Get the prediction using the loaded model
    prediction = predict(model, features)

    # Return the prediction as a response
    return PredictResponse(prediction=prediction)
