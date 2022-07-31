from flask import jsonify, request
import jwt
from cryptography.hazmat.primitives import serialization
import datetime
from functools import wraps

jwt_key_secret_file = open('.ssh/id_rsa', 'r').read()
jwt_key_secret = serialization.load_ssh_private_key(jwt_key_secret_file.encode(), password=b'gato') 
jwt_key_secret_file_public = open('.ssh/id_rsa.pub', 'r').read()
jwt_key_secret_public = serialization.load_ssh_public_key(jwt_key_secret_file_public.encode())

def create_token(data: dict):
    print(data.user, data.password)
    print(jwt_key_secret)
    token = jwt.encode({'user' : data.user, 'password' : data.password, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=4)}
            , key=jwt_key_secret, algorithm = 'RS256' )
    return jsonify({'token' : token})

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token') 
        if not token:
            return jsonify({'message' : 'Token is missing'})
        else:
            try:
                data = jwt.decode(token, jwt_key_secret_public, algorithms='RS256')
            except:
                return jsonify({'message' : 'Token is invalid'})

        return func(*args, **kwargs)
    return decorated
