
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from backend.Phyton.Relacion import Espacio_planta
from backend.Phyton.base import Base
from backend.Phyton.Decoradores import jsonificable


class Planta(Base, jsonificable):

    __tablename__ = 'plantas'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), nullable=False)
    nombre = Column(String(30), nullable=False)
    imagen = Column(URLType, nullable=True)
    espaciosId = relationship('Espacio_planta', backref='planta',
                             primaryjoin=id == Espacio_planta.planta_id)


    def __init__(self, nombre, descripcion, url):
        self.nombre = nombre
        self.descripcion = descripcion
        self.imagen = url
