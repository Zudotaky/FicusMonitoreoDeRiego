
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.Phyton.base import Base
from backend.Phyton.Decoradores import jsonificable


class Planta(Base, jsonificable):

    __tablename__ = 'planta'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), nullable=False)
    nombre = Column(String(30), nullable=False)
    espaciosId = relationship('Espacio', secondary='espacio_planta')

    def __init__(self, nombre, descripcion, id=None, espacios=[]):
        self.nombre = nombre
        self.descripcion = descripcion
        self.id = id
        self.espacios = espacios
