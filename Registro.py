from sqlalchemy import Integer, Column, String, Date, ForeignKey, column
from sqlalchemy.orm import relationship, mapper
from base import Base
from Decoradores import jsonificable


class Registro(Base, jsonificable):

    __tablename__ = 'registro'
    id = Column(Integer, primary_key=True, autoincrement=True)
    plantaId = Column(Integer, ForeignKey('plantas.id'))
    fecha = Column(String(30))
    humedad = Column(Integer)
    temperatura = Column(Integer)

    def __init__(self, idPlanta, fecha, humedad = None, temperatura = None):
        self.plantaId = idPlanta
        self.fecha = fecha
        self.humedad = humedad
        self.temperatura = temperatura

