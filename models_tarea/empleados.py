from basededatos import conexion
from sqlalchemy import Column, types, ForeignKey


class EmpleadoModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text, nullable=False)
    email = Column(type_=types.Text, nullable=False, unique=True)

    area_id = Column(ForeignKey(column='Tipo_areas.id'), nullable=False, name='Tipo_area.id')
    
    __tablename__ = 'empleados'




































