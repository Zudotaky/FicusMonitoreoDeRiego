from backend.Phyton.Dao.DaoGeneral import DaoGeneral
from backend.Phyton.Decoradores import session, connecion
from backend.Phyton.Planta import Planta
from backend.Phyton.Relacion import Espacio_planta


class DaoPlanta(DaoGeneral):

    classe = Planta

    @connecion
    def obtenerPlantaPorId(self, id):
        return self.currentSession.query(Planta).filter(Planta.id == id).one()

    @connecion
    def obtenerPlantasPorEspacioId(self, espacioId):
        return self.currentSession.query(Planta).join(Planta.espaciosId).\
            filter(Espacio_planta.espacio_id == espacioId).all()


    @connecion
    def obtenerPlantaSinEspacio(self):
        return self.currentSession.query(Planta).filter(Planta.espaciosId == None )
