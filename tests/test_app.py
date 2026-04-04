import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    # Add simple assertions about the template rendering
    assert b'Fat Loss' in response.data or b'Muscle Gain' in response.data

def test_get_program_valid_fat_loss(client):
    response = client.get('/api/program/fl')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 'fl'
    assert data['name'] == 'Fat Loss (FL)'
    assert 'workout' in data
    assert 'diet' in data

def test_get_program_valid_muscle_gain(client):
    response = client.get('/api/program/mg')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 'mg'

def test_get_program_invalid(client):
    response = client.get('/api/program/invalid_id')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Program not found'
