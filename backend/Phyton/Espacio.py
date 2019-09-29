from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from backend.Phyton.base import Base
from sqlalchemy.orm import relationship

espacio_planta = Table('espacio_planta', Base.metadata,
                       Column('planta_id', Integer, ForeignKey('planta.id')),
                       Column('esapcio_id', Integer, ForeignKey('espacio.id')))

class Espacio(Base):
    __tablename__ = 'espacio'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), nullable=False)
    nombre = Column(String(30), nullable=False)
    plantas = relationship("plantas", secondary='espacio_planta')

    def __init__(self, nombre, descripcion, plantas=None, id=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.plantas = plantas
        self.id = id
