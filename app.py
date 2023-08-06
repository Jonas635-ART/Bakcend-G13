from flask import Flask
from basededatos import conexion
from models_tarea.Area import AreaModel
from models_tarea.empleados import EmpleadoModel
from urllib.parse import quote_plus
from flask_restful import Api
from flask_migrate import Migrate
from controllers_tarea.Area import AreaController,AreasController
from controllers_tarea.empleados import EmpleadoController, EmpleadosController
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/tarea' % quote_plus('root')

conexion.init_app(app)
Migrate(app=app, db=conexion)


api.add_resource(AreasController, '/areas')
api.add_resource(AreaController, '/area/<int:id>')
api.add_resource(EmpleadoController, '/empleado')
api.add_resource(EmpleadosController, '/empleados')


if __name__ == '__main__':
    app.run(debug=True)
















































