from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import URLType

from Relacion import Espacio_planta
from base import Base
from sqlalchemy.orm import relationship

from Decoradores import jsonificable


class Espacio(Base, jsonificable):
    __tablename__ = 'espacios'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), nullable=False)
    nombre = Column(String(30), nullable=False)
    imagen = Column(URLType, nullable=True)
    plantasId = relationship('Espacio_planta', backref='espacio',
                             primaryjoin=id == Espacio_planta.espacio_id)


    def __init__(self, nombre, descripcion, url):
        self.nombre = nombre
        self.descripcion = descripcion
        self.imagen = url