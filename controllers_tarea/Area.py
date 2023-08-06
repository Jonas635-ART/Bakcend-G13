from basededatos import conexion
from models_tarea.Area import AreaModel
from flask_restful import Resource, request
from dtos_tarea import AreaRequestDTO#, AreaResponseDTO


class AreasController(Resource):
    def get(self):

        areas = conexion.session.query(AreaModel).all()
        dto = AreaRequestDTO()

        resultado = dto.dump(areas, many=True)

        return {
            'content': resultado
        }, 200
      
    def post(self):
        try:
            dto = AreaRequestDTO()
            dataValidada = dto.load(request.get_json())
            nuevaArea = AreaModel(**dataValidada)

            conexion.session.add(nuevaArea)
            conexion.session.commit()

            #dtoResponse = AreaResponseDTO()
            return {
                'message': 'Area creada exitosamente'
                #'content': dtoResponse.dump(nuevaArea)
            },
        except Exception as error:

            return {
                'message': 'Error al crear el area',
                'content': error.args
            }, 400


class AreaController(Resource):
    def get(self, id):
        AreaEncontrado = conexion.session.query(
            AreaModel).filter_by(id=id).first()
        if not AreaEncontrado:
            return {
                'message': 'El area no existe'
            }, 404

        dto = AreaRequestDTO()
        AreaConvertido = dto.dump(AreaEncontrado)

        return {
            'content': AreaConvertido
        }
