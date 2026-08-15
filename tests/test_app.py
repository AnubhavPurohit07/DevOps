import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page_status(client):
    response = client.get('/')
    assert response.status_code == 200


def test_home_page_content(client):
    response = client.get('/')
    assert b'container' in response.data


def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'healthy'
