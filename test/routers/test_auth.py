from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_token():
    response = client.get("/auth/token")
    assert response.status_code == 200
