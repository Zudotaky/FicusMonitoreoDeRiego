from backend.Phyton.Dao.DaoPlanta import DaoPlanta
from backend.Phyton.Planta import Planta




class DispatcherPlanta:

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
        jsonDePlantas = []
        for planta in listaDePlantas:
            jsonDePlantas.append(planta.jsonificar())
        return jsonDePlantas


    def obtenerPlantaPorId(self, id):
        return self.daoPlantas.obtenerPlantaPorId(id).jsonificar()


    def obtenerPlantasPorEspacioId(self, idEspacio):
        listaDePlantas = self.daoPlantas.obtenerPlantasPorEspacioId(idEspacio)
        jsonDePlantas = []
        for planta in listaDePlantas:
            jsonDePlantas.append(planta.jsonificar())
        return jsonDePlantas













