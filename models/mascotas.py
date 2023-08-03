from sqlalchemy import Column, types, ForeignKey
from base_de_datos import conexion
from enum import Enum

class tipomascota(Enum):
    PERRO = 'PERRO'
    GATO = 'GATO'
    LORO = 'LORO'

class SexoMascota(Enum):
    MACHO = 'MACHO'
    HERMBRA = 'HEMBRA'


class MascotaModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    tipo = Column(type_=types.Enum(tipomascota), nullable=False)
    sexo = Column(type_=types.Enum(SexoMascota),default=SexoMascota.MACHO)
    f_naci = Column(type_=types.Date, name='fecha_nacimiento')

    usuario_id = Column(ForeignKey(column='usuarios.id'), nullable=False, name='usuario.id')
    __tablename__ = 'mascotas'










































