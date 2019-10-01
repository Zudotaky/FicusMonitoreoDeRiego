
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.Phyton.Espacio import Espacio
from backend.Phyton.Planta import Planta
from backend.Phyton.Registro import Registro
from backend.Phyton.Decoradores import session, connecion


class DaoGeneral:

    engine = create_engine('sqlite:///ficus.db', echo=True)
    sessionConfig = sessionmaker(bind=engine)
    session = None
    connector = None


class DaoPlanta(DaoGeneral):

    @session
    def persistirPlanta(self, planta):
        self.session.add(planta)
        return planta

    @connecion
    def obtenerPlantas(self):
        plantas = self.session.query(Planta).all()
        return plantas

    @connecion
    def obtenerPlantaPorId(self, id):
        return self.session.query(Planta).filter(Planta.id == id).one()

    @connecion
    def obtenerPlantasPorEspacioId(self, espacioId):
        return self.session.query(Planta).filter(Planta.espacios.id == espacioId).one()





class DaoEspacio(DaoGeneral):

    @session
    def persistirEspacio(self, espacio):
        self.session.add(espacio)
        return espacio

    @connecion
    def obtenerEspacio(self):
        return self.session.query(Espacio).all()

    @connecion
    def obtenerEspacioPorId(self, id):
        return self.session.query(Espacio).filter(Espacio.id == id).one()


class DaoRegistro(DaoGeneral):

    @session
    def persistirRegistro(self, registro):
        self.session.add(registro)
        return registro

    @connecion
    def obtenerRegistroPorId(self, plantaId):
        return self.session.query(Registro).filter(Registro.idPlanta == plantaId).all()

    @connecion
    def obtenerRegistrosPorIdYFechas(self, plantaId, fechaInicio, fechaFin):
        return self.session.query(Registro).filter(Registro.plantaId == plantaId, Registro.fecha > fechaInicio, Registro.fecha < fechaFin).all()

#Base.metadata.create_all(DaoGeneral.engine)
