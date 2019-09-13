import DateTime

from backend.Phyton.DaoFlor import DaoFlor
from backend.Phyton.Planta import Planta


class Jardinero:


    def __init__(self):
        self.daoFlores = DaoFlor()
        self.plantas = self.recuperarPlantas()
        self.formatoDia ="%Y-%m-%d %H:%M:%S"



    def nuevaPlanta(self, nombre, descripcion):
        plantaNueva = Planta(nombre,descripcion)
        self.daoFlores.persistirPlanta(plantaNueva)

    def recuperarPlantas(self):
        return self.formarPlantas(self.daoFlores.obtenerPlantas())

    def obtenerPlantas(self):
        self.plantas = self.recuperarPlantas()
        jsonDePlantas = []
        for planta in self.plantas:
            jsonDePlantas.append({'id': planta.id(), 'Nombre': planta.nombre(), 'Descripcion': planta.descripcion()})
        return jsonDePlantas


    def sensar(self,id,estadoDePlanta):
        fechaActual = DateTime.DateTime().strftime(self.formatoDia)
        self.daoFlores.agregarSenseo(id,estadoDePlanta,fechaActual)

    def otenerSenseo(self,id,fechaInicio,fechaFin):
        listaSenseos = self.daoFlores.obtenerSenseos(id, fechaInicio,fechaFin)
        listaSenseos = self.formarSenseos(listaSenseos)
        return listaSenseos

    def formarSenseos(self,senseosAformar):
        senseosListos = []
        for senso in senseosAformar:
            senseosListos.append({'Humedad' : senso[1] , 'fechas' : senso[2]})
        return senseosListos

    def formarPlantas(self, listaPlantas):
        listaPlantasRecuperada = []
        for planta in listaPlantas:
            plantaRecuperada = Planta(planta[1],planta[2],planta[0])
            listaPlantasRecuperada.append(plantaRecuperada)
        return listaPlantasRecuperada
