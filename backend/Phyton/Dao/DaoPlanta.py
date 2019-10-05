from backend.Phyton.Dao.DaoGeneral import DaoGeneral
from backend.Phyton.Decoradores import session, connecion
from backend.Phyton.Planta import Planta


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