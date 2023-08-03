from base_de_datos import conexion
from sqlalchemy import Column, types, Enum

class CategoRopa(Enum):
    Brasier = 'Brasier'
    Truza = 'Truza'
    Conjunto = 'Conjunto'

class ropaModel(conexion.Model):

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    categoria = Column(type_=types.Enum(CategoRopa), nullable=False)
    precio = Column(type_=types.Text, nullable=False)
    detalle = Column(type_=types.Text, nullable=True)
    imagen = Column(type_=types.Text, nullable=False)


    __tablename__ = 'ropas_intimas'
















