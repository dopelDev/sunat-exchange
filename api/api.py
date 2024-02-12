from flask_restful import Api, Resource
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from methods import sunatscrapy

app = Flask(__name__)
api = Api(app, catch_all_404s=True)
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

# Configuración de Flask-Swagger-UI
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # URL de Swagger UI
    API_URL,  # URL del archivo JSON de Swagger
    config={
        'app_name': "Ejemplo de API Flask"
    },
)

# Registrar el blueprint de Swagger UI en la aplicación Flask
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

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
