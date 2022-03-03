from fastapi.testclient import TestClient
from test.test import test_app

client = TestClient(test_app())

def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "Andres", "email": "andres.ch@prom.me", "password": "Test123"}
    )
    assert response.status_code == 201

def test_update_user_me():
    # response = client.put(
    #     "/users/",
    #     json={"name": "Andres", "email": "andres.ch@prom.me", "password": "Test123"}
    # )
    # assert response.status_code == 201
    pass
