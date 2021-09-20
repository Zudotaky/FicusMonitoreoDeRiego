from Dao.DaoGeneral import DaoGeneral
from Decoradores import session, connecion
from Espacio import Espacio


class DaoEspacio(DaoGeneral):

    classe = Espacio

    @session
    def agregarPlantaAEspacio(self, espacio_planta):
        return self.currentSession.add(espacio_planta)