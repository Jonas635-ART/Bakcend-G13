from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models import UsuarioModel, TipoUsuario
from marshmallow_enum import EnumField
from marshmallow import fields, Schema

class UsuarioRequestDTO(SQLAlchemyAutoSchema):
    #correo = auto_field()
    correo = fields.Email(required=True)
    class Meta:
        model: UsuarioModel
class UsuarioResponseDTO(SQLAlchemyAutoSchema):
    TipoUsuario = EnumField(TipoUsuario)
    password = auto_field(load_only=True)

    class Meta:
        model: UsuarioModel

class LoginRequestDTO(Schema):
    correo = fields.Email(required=True)
    password = fields.Str(required=True)





















