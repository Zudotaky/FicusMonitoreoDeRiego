import DateTime

from backend.Phyton.DaoFlor import DaoFlor
from backend.Phyton.Planta import Planta


class Jardinero:


    def __init__(self):
        self.daoFlores = DaoFlor()
        self.plantas = self.formarPlantas(self.daoFlores.obtenerPlantas())
        self.formatoDia ="%Y-%m-%d %H:%M:%S"


    def nuevaPlanta(self, nombre, descripcion):
        plantaNueva = Planta(nombre,descripcion)
        self.daoFlores.persistirPlanta(plantaNueva)


    def obtenerPlantas(self):
        jsonDePlantas = []
        for planta in self.plantas:
            jsonDePlantas.append({'id': planta.id(), 'Nombre': planta.nombre(), 'Descripcion': planta.descripcion()})

        return jsonDePlantas


    def formarPlantas(self, listaPlantas):
        listaPlantasRecuperada = []
        for planta in listaPlantas:
            plantaRecuperada = Planta(planta[1],planta[2],planta[0])
            listaPlantasRecuperada.append(plantaRecuperada)
        return listaPlantasRecuperada

    def sensar(self,id,estadoDePlanta):
        fechaActual = DateTime.DateTime().strftime(self.formatoDia)
        self.daoFlores.agregarSenseo(id,estadoDePlanta,fechaActual)
