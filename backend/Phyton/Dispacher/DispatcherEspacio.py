from backend.Phyton.Dao.DaoEspacio import DaoEspacio
from backend.Phyton.Espacio import Espacio
from backend.Phyton.Relacion import Espacio_planta


class DispatcherEspacio:

    def __init__(self):
        self.daoEspacio = DaoEspacio()

    # funciones iniciadoras de objetos
    def crearEspacio(self, nombre, descripcion):
        espacio = Espacio(nombre,descripcion)
        self.daoEspacio.persistirEspacio(espacio)
        return espacio.jsonificar()


    #funciones Actualizadoras de objetos

    # funciones para recuperar datos persistidos
    def obtenerEspacios(self):
        listaDeEspacios = self.daoEspacio.obtenerEspacio()
        jsonDeEspacios = []
        for planta in listaDeEspacios:
            jsonDeEspacios.append(planta.jsonificar())
        return jsonDeEspacios


    def obtenerEspacioPorId(self, id):
        espacio = self.daoEspacio.obtenerEspacioPorId(id)
        return espacio.jsonificar()


    def agregarPlantaAEspacio(self, idPlanta, idEspacio):
        espacio_planta = Espacio_planta(idPlanta, idEspacio)
        self.daoEspacio.agregarPlantaAEspacio(espacio_planta)
        return espacio_planta