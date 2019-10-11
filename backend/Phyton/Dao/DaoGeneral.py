from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.Phyton.Decoradores import session, connecion


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

# Base.metadata.create_all(DaoGeneral.engine)
