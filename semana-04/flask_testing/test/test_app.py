from flask import Flask
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

    #client = app.test_client()
    #return client
class Test:
    def test_app(self, client: Flask):
        response = client.get('/')
        assert response.data == b"Hello World!"

    def test_users_get(self,client: Flask):
        ''' LISTAR TODOS LOS USUARIOS'''
        response = client.get('/users')
        assert response.status_code == 200
        assert response.json == [{
            'name':"Jhon Dany",
            'email':'jdany.mc@gmail.com'
        }]

    def test_users_post(self,client: Flask):
        """CREAR UN USUARIO"""
        response = client.post('/users',json = {
            'name':'Jhon Dany',
            'email':'jdany.mc@gmail.com'
        })
        assert response.status_code == 201
        assert response.json == {
            'id':1,
            'name':'Jhon Dany',
            'email':'jdany.mc@gmail.com'
        }
    def test_users_post_error(self, client: Flask):
        """error añ crear usuario"""
        response = client.post('/users', json={
            'name': 'Jhon Dany'            
        })
        assert response.status_code == 500
        assert 'message' in response.json
        assert 'error' in response.json
        assert response.json['message'] == 'Internal server error'
        assert isinstance(response.json['error'], str)
        assert response.json['error'] != ''
