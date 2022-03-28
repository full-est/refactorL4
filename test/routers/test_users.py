from fastapi.testclient import TestClient


def test_create_user(client):
    response = client.post(
        "/users/",
        json={"name": "Andres", "email": "andres.ch@prom.me", "password": "Test12345"}
    )
    assert response.status_code == 201


def test_update_user_me(client, users, token):
    response = client.put(
        "/users/me",
        headers={"Authorization": "Bearer " + token},
        json={"name": "Andres", "email": "test@test.cl", "password": "Test12345"}
    )
    assert response.status_code == 200
