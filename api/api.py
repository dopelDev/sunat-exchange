from flask_restful import Api, Resource, reqparse
from flask import Flask, request, jsonify
from methods import sunatscrapy, jwt_implementation
from config import config

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

date, compra, venta = sunatscrapy.get_rate()

class Data(Resource):
    def get(self):
            return jsonify({'fecha': date,
                    'venta' : venta,
                    'compra' : compra})

class Greeting(Resource):
    @jwt_implementation.token_required
    def get(self):
        return jsonify({'message' : 'Greetings'})

class Tokenzation(Resource):
    def get(self):
        return jsonify({'message' : 'endpoint to verification'})
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user')
        parser.add_argument('password')
        data = parser.parse_args()
        print(data)
        return jwt_implementation.create_token(data)



api.add_resource(Data, '/api/v1/data')
api.add_resource(Greeting, '/')
api.add_resource(Tokenzation, '/auth_v1')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
