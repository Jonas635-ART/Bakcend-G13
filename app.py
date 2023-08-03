from flask import Flask
from base_de_datos import conexion
from models.usuario import UsuarioModel
from models.mascotas import MascotaModel
from urllib.parse import quote_plus
from flask_migrate import Migrate
from flask_restful import Api
from controllers.usuarios import UsuarioController, UsuariosController
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from os import environ

app = Flask(__name__)
api = Api(app)
CORS(app, 
     origins=['https://editor.swagger.io', 'https://mifrontend.com'],
     methods=['GET', 'POST', 'PUT', 'DELETE'],
     allow_headers=['authorization', 'content-type', 'accept'])

SWAGGER_URL = '/docs'
API_URL='/static/documentation_swagger.json'
configuracionSwagger = get_swaggerui_blueprint(SWAGGER_URL, API_URL,config={
    # el nombre de la pestaña del navegador
    'app_name':'Documentacion de Directorio de Mascotas' 
})

# agregar otra aplicacion que no sea Flask a nuestro proyecto de Flask
app.register_blueprint(configuracionSwagger)
#guarda las variables del proyecto de flask
app.config['SQLALCHMEY_DATABASE_URI'] = environ.get('DATABASE_URI')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/directorio' % quote_plus('root')
#Inicia app flask sqla
#dentro de la app de flask tenemos nuestra conexion a la bd
conexion.init_app(app)

Migrate(app=app, db=conexion)

#crea todas las tablas declaradas en el proyecto

#@app.route('/crear-tablas', methods=['GET'])
#def CrearTablas():
#    conexion.create_all()
#    return {
#        'message': 'Creacion ejecutada bien'
#    }

api.add_resource(UsuariosController, '/usuarios')
api.add_resource(UsuarioController, '/usuario/<int:id>')
if __name__ == '__main__':
    app.run(debug=True)
































































