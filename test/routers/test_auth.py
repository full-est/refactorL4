from fastapi.testclient import TestClient

def test_get_token(client, users):
    credentials = {'username': 'test@test.cl', 'password': 'Test12345'}
    response = client.post("/auth/token", data=credentials)
    assert response.status_code == 200
