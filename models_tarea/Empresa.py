from basededatos import conexion
from sqlalchemy import Column, types, ForeignKey
from enum import Enum


class tipoArea(Enum):
    MARKETING = 'MARKETING'
    SISTEMAS = 'SISTEMAS'
    CONTABILIDAD = 'CONTABILIDAD'


class AreaModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Enum(tipoArea), nullable=False)
    piso = Column(type_=types.Text, nullable=False)

    __tablename__ = 'Tipo_areas'





















