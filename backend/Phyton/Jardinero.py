import DateTime

from backend.Phyton.Registro import Registro
from backend.Phyton.DaoGeneral import DaoGeneral
from backend.Phyton.Espacio import Espacio
from backend.Phyton.Planta import Planta


class Jardinero:


    def __init__(self):
        self.daoGeneral = DaoGeneral()
        self.formatoDia ="%Y-%m-%d %H:%M:%S"

    #funciones iniciadoras de objetos
    def crearPlanta(self, nombre, descripcion):
        plantaNueva = Planta(nombre,descripcion)
        self.daoGeneral.persistirPlanta(plantaNueva)
        return plantaNueva

    def crearEspacio(self, nombre, descripcion):
        espacio = Espacio(nombre,descripcion)
        self.daoGeneral.persistirEspacio(espacio)
        return espacio

    def crearReporte(self, idDePlnta, humedad, temperatura):
        registro = Registro(idDePlnta, humedad, temperatura)
        self.daoGeneral.persistirRegistro(registro)
        return registro


    #funciones Actualizadoras de objetos


    # funciones para recuperar datos persistidos
    def obtenerPlantas(self):
        plantas = self.daoGeneral.obtenerPlantas()
        jsonDePlantas = self.jsonifyPlantas(plantas)
        return jsonDePlantas

    def obtenerPlantaPorId(self, id):
        planta = self.daoGeneral.obtenerPlantaPorId(id)
        jsonPlanta = self.jsonifyPlantas(planta)
        return jsonPlanta

    def obtenerPlantasPorEspacioId(self, idEspacio):
        plantas = self.daoGeneral.obtenerPlantasPorEspacioId(idEspacio)
        jsonPlantas = self.jsonifyPlantas(plantas)
        return jsonPlantas

    def obtenerEspacios(self):
        espacios = self.daoGeneral.obtenerEspacio()
        return espacios

    def obtenerEspacioPorId(self, id):
        espacio = self.daoGeneral.obtenerEspacioPorId(id)
        jsonEspacio = self.jsonifyEspacios(espacio)
        return jsonEspacio

    def obtenerSenseoPorIdPlanta(self, id):
        listaRegistros = self.daoGeneral.obtenerRegistroPorId(id)
        listaRegistrosFormados = self.jsonifyRegistros(listaRegistros)
        return listaRegistrosFormados

    def obtenerSenseoPorIdPlantaYFecha(self, id, fechaInicio, fechaFin):
        listaRegistros = self.daoGeneral.obtenerSensosPorIdYFechas(id, fechaInicio, fechaFin)
        listaRegistrosFormados = self.jsonifyRegistros(listaRegistros)
        return listaRegistrosFormados


    #metodos para trasformar a json objetos
    def jsonifyPlantas(self, plantas):
        jsonDePlantas = []
        for planta in plantas:
            jsonDePlantas.append({'id': planta.id(), 'Nombre': planta.nombre(), 'Descripcion': planta.descripcion()})
        return jsonDePlantas

    def jsonifyEspacios(self, espacios):
        jsonDeEspacios = []
        for espacio in espacios:
            jsonDeEspacios.append({'id': espacio.id(), 'Nombre': espacio.nombre(), 'Descripcion': espacio.descripcion(),
                                   'tipoDeEspacio': espacio.tipiDeEspacio(), 'idPlantas': espacio.plantasId()})
        return jsonDeEspacios

    def jsonifyRegistros(self, listaRegistros):
        listaRegistrosFormados = []
        for registro in listaRegistros:
            jsonRegistro = {'fechas': DateTime.DateTime(registro[2]).strftime(self.formatoDia), 'Humedad': registro[1],
                            'Temperatura': registro[3]}
            listaRegistrosFormados.append(jsonRegistro)
        return listaRegistrosFormados









