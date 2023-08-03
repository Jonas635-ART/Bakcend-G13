from base_de_datos import conexion
from sqlalchemy import Column, types


class PedidosModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nro_depedido = Column(type_=types.number, nullable=False, unique=True)
    direccion = Column(type_=types.text, nullable=False)
    fecha_de_facturacion = Column(type_=types.Date, nullable=False)
    fecha_llegada = Column(type_=types.Date, nullable=False)
    






























