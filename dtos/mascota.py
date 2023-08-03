from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.mascotas import MascotaModel

class MascotaRequestDTO(SQLAlchemyAutoSchema):
    class Meta:
        model = MascotaModel
        include_fk = True

















































