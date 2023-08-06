from basededatos import conexion
from sqlalchemy import Column, types
from enum import Enum


class AreaModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    piso = Column(type_=types.Text, nullable=False)

    

    __tablename__ = 'areas'





















