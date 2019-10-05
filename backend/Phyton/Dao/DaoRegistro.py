from backend.Phyton.Dao.DaoGeneral import DaoGeneral
from backend.Phyton.Decoradores import session, connecion
from backend.Phyton.Registro import Registro


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
        return self.session.query(Registro).filter(Registro.plantaId == plantaId, Registro.fecha > fechaInicio,
                                                   Registro.fecha < fechaFin).all()