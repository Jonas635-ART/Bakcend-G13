from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models_tarea.Area import AreaModel #tipoArea
#from marshmallow_enum import EnumField

class AreaRequestDTO(SQLAlchemyAutoSchema):
    class Meta:
        model = AreaModel
#class AreaResponseDTO(SQLAlchemyAutoSchema):
 #   tipoArea = EnumField(tipoArea)
 #   class Meta:
   #     model = AreaModel