import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_for_activity():
    # Suponiendo que existe una actividad llamada 'Chess Club'
    activity = "Chess Club"
    email = "testuser@example.com"
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200 or response.status_code == 400
    # Puede fallar si ya está inscrito, pero nunca debe ser 500

def test_unregister_participant():
    activity = "Chess Club"
    email = "testuser@example.com"
    response = client.post(f"/activities/{activity}/unregister?email={email}")
    assert response.status_code == 200 or response.status_code == 404
    # Puede fallar si no está inscrito, pero nunca debe ser 500
