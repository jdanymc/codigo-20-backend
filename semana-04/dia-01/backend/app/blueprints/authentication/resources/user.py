from flask import request
from flask_restful import Resource, Api
from ..models import User
from utils.db import db

from .. import authentication
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash

api = Api(authentication)
class UserResource(Resource):
    def get(self):
        pass
    def post(self):
        try:
            json = request.get_json()
            hashed_pwd = generate_password_hash(json['password'])
            exists_email = User.query.filter_by(email=json['email']).first()
            if not exists_email:
                record = User(name  =json['name'],email=json['email'],password = hashed_pwd)
                record.save()
                access_token = create_access_token(identity=record.id)
                refresh_token = create_refresh_token(identity=record.id)
                return {
                    'status': True,
                    'access_token': access_token,
                    'refresh_token': refresh_token
                },201
            
            return {
                'status': True,
                'content': {
                    'access_token': 'access_token',
                    'refresh_token': 'refresh_token'
                }
            }
        except Exception as e:
            db.session.rollback()
            return {
                'message': str(e),
                'status': False,
            },500
    def put(self):
        pass
    def delete(self):
        pass

class SignInResource(Resource):
    def post(self):
        try:
            json = request.get_json()
            record = User.query.filter_by(email=json['email']).first()
            if not record:
                return {
                    'status': False,
                    'message': 'Usuario o contraseña incorrectos'
                },404
            is_pwd_secure = check_password_hash(record.password,json['password'])
            if is_pwd_secure:
                access_token = create_access_token(identity=record.id)
                refresh_token = create_refresh_token(identity=record.id)
                return {
                    'status': True,
                    'access_token': access_token,
                    'refresh_token': refresh_token
                },200
 
            return {
                    'status': False,
                    'message': 'Usuario o contraseña incorrectos'
                },404
    
        except Exception as e:
            return {
                'status': False,
                'message': str(e),
            },500    
        
api.add_resource(UserResource,'/user')
api.add_resource(SignInResource,'/signin')