from models import UsuarioModel
from utilitarios import conexion
from flask_restful import Resource, request
from dtos import UsuarioRequestDTO, UsuarioResponseDTO, LoginRequestDTO
from bcrypt import gensalt, hashpw, checkpw

class RegistroController(Resource):
    def post(self):
        try:
            dto = UsuarioRequestDTO()
            dataValidada = dto.load(request.get_json())
            nuevoUsuario = UsuarioModel(**dataValidada)

            salt = gensalt()
            password = dataValidada.get('password')
            #convertimos el password abytes
            passwordBytes = bytes(password, 'utf-8')
            #mezclamos apassword con el salt generado y lo convertimos a string
            passwordHaseada = hashpw(passwordBytes, salt).decode('utf-8')
            #sobrescribimos el pasword con el hash generado
            dataValidada['password'] = passwordHaseada

            #fin del hashsing de la password

            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            dtoResponse = UsuarioRequestDTO()
            return {
                'message': 'Usuario Creado',
                'content': dtoResponse.dump(nuevoUsuario)
            },201
        except Exception as e:
            return {
                'message': 'error al crear',
                'content':e.args
            }, 400

class LoginController(Resource):
    def post(self):
        dto = LoginRequestDTO()
        try:
           dataValidada = dto.load(request.get_json())
           usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(correo = dataValidada.get('correo')).first()
           if not usuarioEncontrado:
               return {
                   'message': 'E usuario no existe'
               }, 400
           password = usuarioEncontrado.password
           passwordEntrante = bytes(dataValidada.get('password'), 'utf-8')
           #valida si es el password
           resultado = checkpw(passwordEntrante, password)

            if resultado == False:
                return {
                    'message': 'Credenciales incorrectas'
                }, 400
            return {
                'message': 'Si eres!'
            }
        except Exception as e:
            return {
                'message': 'E usuario no existe',
                'content': e.args
            }, 400
            








































