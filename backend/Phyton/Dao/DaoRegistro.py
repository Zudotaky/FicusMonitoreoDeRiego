from backend.Phyton.Dao.DaoGeneral import DaoGeneral
from backend.Phyton.Decoradores import session, connecion
from backend.Phyton.Registro import Registro


class DaoRegistro(DaoGeneral):

    classe = Registro

    @connecion
    def obtenerRegistroPorPlantaId(self, idplanta):
        return self.currentSession.query(self.classe).filter(self.classe.plantaId == idplanta).all()

    @connecion
    def obtenerRegistrosPorIdYFechas(self, plantaId, fechaInicio, fechaFin):
            return self.currentSession.query(self.classe).filter(self.classe.plantaId == plantaId, self.classe.fecha > fechaInicio,
                                                          self.classe.fecha < fechaFin).all()