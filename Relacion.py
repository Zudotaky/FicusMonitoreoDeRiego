from sqlalchemy import Column, Integer, ForeignKey

from base import Base


class Espacio_planta(Base) :
    __tablename__ = 'espacio_planta'
    espacio_id = Column(Integer, ForeignKey('espacios.id'), primary_key=True)
    planta_id = Column(Integer, ForeignKey('plantas.id'), primary_key=True)

    def __init__(self, plantaid, espacioid):
        self.espacio_id = espacioid
        self.planta_id = plantaid