from backend.Phyton.Dao.DaoGeneral import DaoGeneral
from backend.Phyton.Decoradores import session, connecion
from backend.Phyton.Planta import Planta


class DaoPlanta(DaoGeneral):

    classe = Planta

    @connecion
    def obtenerPlantaPorId(self, id):
        return self.currentSession.query(Planta).filter(Planta.id == id).one()

    @connecion
    def obtenerPlantasPorEspacioId(self, espacioId):
        return self.currentSession.query(Planta).filter(Planta.espacios.id == espacioId).one()