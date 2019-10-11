from backend.Phyton.Dao.DaoGeneral import DaoGeneral
from backend.Phyton.Decoradores import session, connecion
from backend.Phyton.Registro import Registro


class DaoRegistro(DaoGeneral):

    classe = Registro

    @connecion
    def obtenerRegistroPorId(self, plantaId):
        return self.currentSession.query(Registro).filter(Registro.idPlanta == plantaId).all()

    @connecion
    def obtenerRegistrosPorIdYFechas(self, plantaId, fechaInicio, fechaFin):
        return self.currentSession.query(Registro).filter(Registro.plantaId == plantaId, Registro.fecha > fechaInicio,
                                                          Registro.fecha < fechaFin).all()