from basededatos import conexion
from models_tarea.empleados import EmpleadoModel
from flask_restful import Resource, request
from dtos_tarea.empleadosdto import EmpleadoRequestDto

class EmpleadoController(Resource):
    def post(self):
        
        try:
            dto = EmpleadoRequestDto()
            dataValidada = dto.load(request.get_json())
            nuevoEmpleado = EmpleadoModel(**dataValidada)

            conexion.session.add(nuevoEmpleado)
            conexion.session.commit()
            
            return {
                'message': 'Empleado creada exitosamente'
            }, 201
        
        except Exception as e:
            return {
                'message': 'Error al crear el Empleado',
                'content': e.args
            }, 400
class EmpleadosController(Resource):
        def get(self):
            empleados = conexion.session.query(EmpleadoModel).all()
            dto = EmpleadoRequestDto()

            resultado = dto.dump(empleados, many=True)
            print(empleados)
            print(resultado)

            return {
                'content': resultado
            }        









