from sqlalchemy import Integer, Column, String, Date, ForeignKey, column
from sqlalchemy.orm import relationship
from backend.Phyton.base import Base
from backend.Phyton.Decoradores import jsonificable


class Registro(Base, jsonificable):

    __tablename__ = 'registro'
    plantaId = Column(Integer, ForeignKey('plantas.id'), primary_key=True)
    fecha = Column(String(30), primary_key=True)
    humedad = Column(Integer)
    temperatura = Column(Integer)

    def __init__(self, idPlanta, fecha, humedad = None, temperatura = None):
        self.plantaId = idPlanta
        self.fecha = fecha
        self.humedad = humedad
        self.temperatura = temperatura
