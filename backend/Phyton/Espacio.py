from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from backend.Phyton.base import Base
from sqlalchemy.orm import relationship

from backend.Phyton.Decoradores import jsonificable

class Espacio_planta(Base) :
    __tablename__ = 'espacio_planta'
    espacio_id = Column(Integer, ForeignKey('espacios.id'), primary_key=True)
    planta_id = Column(Integer, ForeignKey('plantas.id'), primary_key=True)

    def __init__(self, plantaid, espacioid):
        self.espacio_id = espacioid
        self.planta_id = plantaid


class Espacio(Base, jsonificable):
    __tablename__ = 'espacios'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), nullable=False)
    nombre = Column(String(30), nullable=False)
    plantasId = relationship('Espacio_planta', backref='espacio',
                             primaryjoin=   id == Espacio_planta.espacio_id)


    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
