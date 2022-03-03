from fastapi.testclient import TestClient

from test.test import test_app

client = TestClient(test_app())

def test_main():
    response = client.get("/")
    assert response.status_code == 200
