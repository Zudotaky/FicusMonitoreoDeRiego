from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.Phyton.base import Base


class Planta(Base):

    __tablename__ = 'planta'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), nullable=False)
    nombre = Column(String(30), nullable=False)
    espacios = relationship("espacios", secondary='espacio_planta')

    def __init__(self, nombre, descripcion, id=None, espacioId=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.id = id
        self.espacioId = espacioId


