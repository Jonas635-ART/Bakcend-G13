from models import UsuarioModel
from utilitarios import conexion
from flask_restful import Resource, request
from dtos import UsuarioRequestDTO, UsuarioResponseDTO, LoginRequestDTO, CambiasPasswordRequestDTO
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from mensajeria import cambiarPassword

class RegistroController(Resource):
    def post(self):
        """
        file:registroUsuarioSwagger.yml
        """
        try:
            dto = UsuarioRequestDTO()
            identificador = get_jwt_identity()
            print(identificador)
            return {
                'message': 'Todo ok'
            }
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
        """
        file: loginSwagger.yml
        """
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
           token = create_access_token(identity= usuarioEncontrado.id)
           print(token)
           return {
                'content': token
            }
        except Exception as e:
            return {
                'message': 'E usuario no existe',
                'content': e.args
            }, 400
            
class UsuarioController(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()

        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = identity).first()
        if not usuarioEncontrado:
            return {
                'message': 'El usuario no existe'
            }, 404
        dto = UsuarioResponseDTO()

        return {
            'content': dto.dump(usuarioEncontrado)
        }
class CambiarcontrasenaController(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        dto = CambiasPasswordRequestDTO()
        identity = get_jwt_identity()
        try:
            dataValidadda = dto.load(data)
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = identity).first()
            if not usuarioEncontrado:
                return {
                    'message': 'Usuario no existe'
                }, 404
            password = bytes(dataValidadda.get('password'), 'utf-8')
            hashedpassword = bytes(usuarioEncontrado.password, 'utf-8')
            if checkpw(password, hashedpassword) == False:
                return {
                    'message': 'No es la contraseña'
                }, 404
            nuevapasword = bytes(dataValidadda.get('nuevapassword'), 'utf-8')
            salt = gensalt()
            hashnuevapassword = hashpw(nuevapasword, salt).decode('utf-8')

            usuarioEncontrado.password = hashnuevapassword

            conexion.session.commit()

            cambiarPassword(usuarioEncontrado.correo)

            return {
                'message': 'Contraseña actualizada'
            }

        except Exception as error:
            return {
                'message': 'Error al actualizar',
                'content': error.args
            }






































