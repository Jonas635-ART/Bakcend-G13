from base_de_datos import conexion
from models.mascotas import MascotaModel
from flask_restful import Resource, request
from dtos.mascota import MascotaRequestDTO

class MascotasController(Resource):
    def post(self):
        body = request.get_json()
        dto = MascotaRequestDTO()
        try: 
            dataValidada = dto.load(body)
            nuevaMascota = MascotaModel(**dataValidada)
            conexion.session.add(nuevaMascota)
            conexion.session.commit()

            return {
                'message': 'mascota creada'
            }, 201
    
        except Exception as e:
            return {
                'message': 'Erro al crear',
                'content': e.args

            }, 400
























































