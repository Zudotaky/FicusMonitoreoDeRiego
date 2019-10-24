from backend.Phyton.Dao.DaoPlanta import DaoPlanta
from backend.Phyton.Dispacher.DispacharGeneral import Dispacher
from backend.Phyton.Planta import Planta




class DispatcherPlanta(Dispacher):

    def __init__(self):
        self.daoPlantas = DaoPlanta()


    #funciones iniciadoras de objetos
    def crearPlanta(self, nombre, descripcion):
        plantaNueva = Planta(nombre, descripcion)
        self.daoPlantas.persistir(plantaNueva)
        return plantaNueva.jsonificar()

    #funciones Actualizadoras de objetos

    # funciones para recuperar datos persistidos
    def obtenerPlantas(self):
        listaDePlantas = self.daoPlantas.obtener()
        return self.jsonificarLista(listaDePlantas)


    def obtenerPlantaPorId(self, id):
        return self.daoPlantas.obtenerPlantaPorId(id).jsonificar()


    def obtenerPlantasPorEspacioId(self, idEspacio):
        listaDePlantas = self.daoPlantas.obtenerPlantasPorEspacioId(idEspacio)
        return self.jsonificarLista(listaDePlantas)

    def obtenerPlantasSinEspacio(self):
        listasDePlantas = self.daoPlantas.obtenerPlantaSinEspacio()
        return self.jsonificarLista(listasDePlantas)














