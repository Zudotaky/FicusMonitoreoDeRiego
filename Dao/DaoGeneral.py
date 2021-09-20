from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from Decoradores import session, connecion
from base import Base
from Planta import Planta
from Espacio import Espacio
from Registro import Registro


class DaoGeneral:
    engine = create_engine('sqlite:///ficus.db', connect_args={'check_same_thread': False}, echo=True)
    sessionConfig = sessionmaker(bind=engine)
    currentSession = sessionConfig()
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
