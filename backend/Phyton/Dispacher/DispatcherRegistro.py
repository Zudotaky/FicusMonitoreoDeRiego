from backend.Phyton.Dao.DaoRegistro import DaoRegistro
from backend.Phyton.Dispacher.DispacharGeneral import Dispacher
from backend.Phyton.Registro import Registro


class DispatcherRegistro(Dispacher):

    def __init__(self):
        self.daoRegistro = DaoRegistro()
        self.formatoDia ="%Y-%m-%d %H:%M:%S"

    # funciones iniciadoras de objetos
    def crearReporte(self, idDePlnta, humedad, temperatura):
        registro = Registro(idDePlnta, humedad, temperatura)
        self.daoRegistro.persistir(registro)
        return registro.jsonificar()


    # funciones Actualizadoras de objetos

    # funciones para recuperar datos persistidos
    def obtenerRegistroPorIdPlanta(self, plantaId):
        listaDeRegistros = self.daoRegistro.obtenerRegistroPorId(plantaId)
        return self.jsonificarLista(listaDeRegistros)


    def obtenerRegistroPorIdPlantaYFecha(self, id, fechaInicio, fechaFin):
        listaDeRegistros = self.daoRegistro.obtenerRegistrosPorIdYFechas(id, fechaInicio, fechaFin)
        return self.jsonificarLista(listaDeRegistros)