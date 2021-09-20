from datetime import datetime

from Dao.DaoRegistro import DaoRegistro
from Dispacher.DispacharGeneral import Dispacher
from Registro import Registro


class DispatcherRegistro(Dispacher):

    def __init__(self):
        self.dao = DaoRegistro()
        self.formatoDia ="%Y-%m-%d %H:%M:%S"

    # funciones iniciadoras de objetos
    def crearReporte(self, idDePlnta, humedad, temperatura):
        registro = Registro(idDePlnta, datetime.now().strftime(self.formatoDia), humedad, temperatura)
        self.dao.persistir(registro)
        return registro.jsonificar()


    # funciones Actualizadoras de objetos

    # funciones para recuperar datos persistidos
    def obtenerRegistroPorIdPlanta(self, plantaId):
        listaDeRegistros = self.dao.obtenerRegistroPorPlantaId(plantaId)
        return self.jsonificarLista(listaDeRegistros)


    def obtenerRegistroPorIdPlantaYFecha(self, id, fechaInicio, fechaFin):
        listaDeRegistros = self.dao.obtenerRegistrosPorIdYFechas(id, fechaInicio, fechaFin)
        return self.jsonificarLista(listaDeRegistros)

    def obtenerUltimoRegistro(self, plantaId):
        registro = self.dao.obtenerUltimoRegistro(plantaId)
        return registro.jsonificar()