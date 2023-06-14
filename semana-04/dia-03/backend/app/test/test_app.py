from flask import Flask, request
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class Test:
    def test_app(self, client: Flask):
        response = client.get('/')
        assert response.status_code == 200
        assert response.json == {
            'status': True,
            'content': 'api rest activo'
        }