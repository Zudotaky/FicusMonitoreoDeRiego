from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.Phyton.Decoradores import session, connecion
from backend.Phyton.base import Base
from backend.Phyton.Planta import Planta
from backend.Phyton.Espacio import Espacio
from backend.Phyton.Registro import Registro


class DaoGeneral:
    engine = create_engine('sqlite:///ficus.db', echo=True)
    sessionConfig = sessionmaker(bind=engine)
    currentSession = None
    connector = None
    classe = None

    @session
    def persistir(self, objeto):
        self.currentSession.add(objeto)
        return objeto

    @connecion
    def obtener(self):
        return self.currentSession.query(self.classe).all()

    @connecion
    def obtenerPorId(self, id):
        return self.currentSession.query(self.classe).filter(self.classe.id == id).one()


Base.metadata.create_all(DaoGeneral.engine)
