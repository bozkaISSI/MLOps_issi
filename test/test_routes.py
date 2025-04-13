from fastapi.testclient import TestClient
from app import app  # Import your FastAPI app

# Initialize the TestClient
client = TestClient(app)

# Test the root route ("/")
def test_welcome_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}

# Test the health check route ("/health")
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
