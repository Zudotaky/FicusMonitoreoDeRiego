import json
import pickle

import DateTime
import jsonpickle

from backend.Phyton.Registro import Registro
from backend.Phyton.DaoGeneral import DaoPlanta, DaoEspacio, DaoRegistro
from backend.Phyton.Espacio import Espacio, Espacio_planta
from backend.Phyton.Planta import Planta




class Jardinero:

    def __init__(self):
        self.daoPlantas = DaoPlanta()
        self.daoEspacio = DaoEspacio()
        self.daoRegistro = DaoRegistro()
        self.formatoDia ="%Y-%m-%d %H:%M:%S"


        #separar
    #funciones iniciadoras de objetos
    def crearPlanta(self, nombre, descripcion):
        plantaNueva = Planta(nombre, descripcion)
        self.daoPlantas.persistirPlanta(plantaNueva)
        return plantaNueva.jsonificar()


    #funciones Actualizadoras de objetos

    # funciones para recuperar datos persistidos
    def obtenerPlantas(self):
        listaDePlantas = self.daoPlantas.obtenerPlantas()
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


            # separar
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







        # separar
    # funciones iniciadoras de objetos
    def crearReporte(self, idDePlnta, humedad, temperatura):
        registro = Registro(idDePlnta, humedad, temperatura)
        self.daoRegistro.persistirRegistro(registro)
        return registro.jsonificar()


    #funciones Actualizadoras de objetos

    # funciones para recuperar datos persistidos
    def obtenerRegistroPorIdPlanta(self, plantaId):
        listaDeRegistros = self.daoRegistro.obtenerRegistroPorId(plantaId)
        jsonDeRegistros = []
        for planta in listaDeRegistros:
            jsonDeRegistros.append(planta.jsonificar())
        return jsonDeRegistros

    def obtenerRegistroPorIdPlantaYFecha(self, id, fechaInicio, fechaFin):
        listaDeRegistros = self.daoRegistro.obtenerRegistrosPorIdYFechas(id, fechaInicio, fechaFin)
        jsonDeRegistros = []
        for planta in listaDeRegistros:
            jsonDeRegistros.append(planta.jsonificar())
        return jsonDeRegistros



    def agregarPlantaAEspacio(self, idPlanta, idEspacio):
        espacio_planta = Espacio_planta(idPlanta, idEspacio)
        self.daoEspacio.agregarPlantaAEspacio(espacio_planta)
        return espacio_planta





