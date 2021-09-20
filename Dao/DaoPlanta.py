from Dao.DaoGeneral import DaoGeneral
from Decoradores import session, connecion
from Planta import Planta
from Relacion import Espacio_planta


class DaoPlanta(DaoGeneral):

    classe = Planta

    @connecion
    def obtenerPlantasPorEspacioId(self, espacioId):
        return self.currentSession.query(self.classe).join(self.classe.espaciosId).\
            filter(Espacio_planta.espacio_id == espacioId).all()


    @connecion
    def obtenerPlantaSinEspacio(self):
        return self.currentSession.query(self.classe).filter(self.classe.espaciosId == None )
