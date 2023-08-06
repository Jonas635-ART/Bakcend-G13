from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models_tarea.empleados import EmpleadoModel

class EmpleadoRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = EmpleadoModel
        # validara tbn las columnas que son llaves foraneas
        include_fk = True