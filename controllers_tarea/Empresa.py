from base_de_datos import conexion
from models_tarea.Empresa import AreaModel
from flask_restful import Resource, request


class EmpresaController(Resource):
    def get(self):

    areas = conexion.session.query(AreaModel).all()

    resultado = dto.dump(areas, many=True)
    print(areas)
    print(resultado)

    def post(self):


class EmpresasController(Resource):
    def get(self, id):




























