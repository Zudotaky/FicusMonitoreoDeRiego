from backend.Phyton.Dao.DaoEspacio import DaoEspacio
from backend.Phyton.Dispacher.DispacharGeneral import Dispacher
from backend.Phyton.Espacio import Espacio
from backend.Phyton.Relacion import Espacio_planta


class DispatcherEspacio(Dispacher):

    def __init__(self):
        self.dao = DaoEspacio()

    # funciones iniciadoras de objetos
    def crear(self, nombre, descripcion, url):
        espacio = Espacio(nombre,descripcion, url)
        self.dao.persistir(espacio)
        return espacio.jsonificar()


    #funciones Actualizadoras de objetos

    # funciones para recuperar datos persistidos
    def obtenerEspacios(self):
        listaDeEspacios = self.dao.obtener()
        return self.jsonificarLista(listaDeEspacios)


    def obtenerEspacioPorId(self, id):
        espacio = self.dao.obtenerEspacioPorId(id)
        return espacio.jsonificar()


    def agregarPlantaAEspacio(self, idPlanta, idEspacio):
        espacio_planta = Espacio_planta(idPlanta, idEspacio)
        self.dao.agregarPlantaAEspacio(espacio_planta)
        return espacio_planta