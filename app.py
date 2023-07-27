from flask import Flask
from base_de_datos import conexion
from models.usuario import UsuarioModel
from urllib.parse import quote_plus


app = Flask(__name__)
#guarda las variables del proyecto de flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/directorio' % quote_plus('root')
#Inicia app flask sqla
#dentro de la app de flask tenemos nuestra conexion a la bd
conexion.init_app(app)

#crea todas las tablas declaradas en el proyecto

@app.route('/crear-tablas', methods=['GET'])
def CrearTablas():
    conexion.create_all()
    return {
        'message': 'Creacion ejecutada bien'
    }

if __name__ == '__main__':
    app.run(debug=True)
































































