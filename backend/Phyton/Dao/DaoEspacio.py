from backend.Phyton.Dao.DaoGeneral import DaoGeneral
from backend.Phyton.Decoradores import session, connecion
from backend.Phyton.Espacio import Espacio


class DaoEspacio(DaoGeneral):

    classe = Espacio

    @session
    def agregarPlantaAEspacio(self, espacio_planta):
        return self.currentSession.add(espacio_planta)