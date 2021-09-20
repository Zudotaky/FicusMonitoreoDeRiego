from Dao.DaoPlanta import DaoPlanta
from Dispacher.DispacharGeneral import Dispacher
from Planta import Planta




class DispatcherPlanta(Dispacher):

    def __init__(self):
        self.dao = DaoPlanta()


    #funciones iniciadoras de objetos
    def crearPlanta(self, nombre, descripcion, url):
        plantaNueva = Planta(nombre, descripcion, url)
        self.dao.persistir(plantaNueva)
        return plantaNueva.jsonificar()

    #funciones Actualizadoras de objetos

    # funciones para recuperar datos persistidos
    def obtenerPlantas(self):
        listaDePlantas = self.dao.obtener()
        return self.jsonificarLista(listaDePlantas)


    def obtenerPlantaPorId(self, id):
        return self.dao.obtenerPorId(id).jsonificar()


    def obtenerPlantasPorEspacioId(self, idEspacio):
        listaDePlantas = self.dao.obtenerPlantasPorEspacioId(idEspacio)
        return self.jsonificarLista(listaDePlantas)

    def obtenerPlantasSinEspacio(self):
        listasDePlantas = self.dao.obtenerPlantaSinEspacio()
        return self.jsonificarLista(listasDePlantas)














