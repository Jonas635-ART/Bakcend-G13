from base_de_datos import conexion
from sqlalchemy import Column, types


class usuariosModel(conexion.Model):

    id = Column(types_=types.Integer,primary_Key=True, autoincrement=True)
    nombre_apellido = Column(type_=types.Text, nullable=False)
    correo = Column(type_=types.Text, unique=True, nullable=False)
    direccion = Column(type_=types.Text, nullable=False)
    telefono = Column(type_=types.Text, nullable=False)



























