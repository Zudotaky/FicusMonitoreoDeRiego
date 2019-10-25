from DateTime import DateTime
from sqlalchemy import Integer, Column, String, Date, ForeignKey, column
from sqlalchemy.orm import relationship
from backend.Phyton.base import Base
from backend.Phyton.Decoradores import jsonificable


class Registro(Base, jsonificable):

    __tablename__ = 'registro'
    fecha = Column(Date, primary_key=True)
    plantaId = Column(Integer, ForeignKey('plantas.id'), primary_key=True)
    humedad = Column(Integer)
    temperatura = Column(Integer)

    def __init__(self, idPlanta, humedad = None, temperatura=None, fecha=DateTime()):
        self.idPlanta = idPlanta
        self.horarioRegistrado = fecha
        self.humedad = humedad
        self.temperatura = temperatura
