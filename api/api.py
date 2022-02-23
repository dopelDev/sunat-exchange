from flask_restful import Api, Resource
from flask import Flask
from methods import sunatscrapy

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

date, compra, venta = sunatscrapy.get_rate()

class data(Resource):
    def get(self):
        return {'fecha': date,
                'venta' : venta,
                'compra' : compra}

class greeting(Resource):
    def get(self):
        return {'greeting' : 'Greetings'}

api.add_resource(data, '/api/v1/data')
api.add_resource(greeting, '/')

if __name__ == '__main__':
    app.run()
