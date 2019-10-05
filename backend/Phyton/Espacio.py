from sqlalchemy import Column, Integer, String

from backend.Phyton.Relacion import Espacio_planta
from backend.Phyton.base import Base
from sqlalchemy.orm import relationship

from backend.Phyton.Decoradores import jsonificable


class Espacio(Base, jsonificable):
    __tablename__ = 'espacios'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), nullable=False)
    nombre = Column(String(30), nullable=False)
    plantasId = relationship('Espacio_planta', backref='espacio',
                             primaryjoin=id == Espacio_planta.espacio_id)


    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
