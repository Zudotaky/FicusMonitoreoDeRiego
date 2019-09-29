
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.Phyton.base import Base
from backend.Phyton.Espacio import Espacio
from backend.Phyton.Planta import Planta
from backend.Phyton.Registro import Registro

class DaoGeneral:

    engine = create_engine('sqlite:///libros.db', echo=True)
    session = None

    #Funciones de sql
    def levantarSession(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def cerrarSession(self):
        self.session.close()

    # #Funciones para inicializar la persistencia de objetos
    # def persistirPlanta(self, planta):
    #     self.connectarSql()
    #     mycursor = self.mysqlConector.cursor()
    #     mycursor.execute(self.queryGuardarPlanta, (planta.nombre(), planta.descripcion()))
    #     self.mysqlConector.commit()
    #     id = mycursor.lastrowid
    #     planta.id(id)
    #     self.cerrarSql()
    #
    #
    # def persistirEspacio(self, espacio):
    #     self.connectarSql()
    #     registroDatos = (espacio.nombre(), espacio.descripcion(), espacio.tipiDeEspacio())
    #     mycursor = self.mysqlConector.cursor()
    #     mycursor.execute(self.queryGuardarEspacio, registroDatos)
    #     self.mysqlConector.commit()
    #     id = mycursor.lastrowid
    #     espacio.id(id)
    #     self.cerrarSql()
    #
    # def persistirRegistro(self, registro):
    #     self.connectarSql()
    #     registroDatos = (registro.plantaId(), registro.horarioDeRegistro(), registro.humedad(), registro.temperatura())
    #     mycursor = self.mysqlConector.cursor()
    #     mycursor.execute(self.queryGuardarSensos, registroDatos)
    #     self.mysqlConector.commit()
    #     self.cerrarSql()
    #
    #
    #
    # #funciones para Actualizar datos de objetos
    #
    #
    #
    # #Funciones para recuperar Objetos
    # def obtenerPlantas(self):
    #     self.connectarSql()
    #     mycursor = self.mysqlConector.cursor()
    #     mycursor.execute(self.queryRecuperarPlantas)
    #     plantas = mycursor.fetchall()
    #     self.cerrarSql()
    #     plantas = self.formarPlantas(plantas)
    #     return plantas
    #
    # def obtenerPlantasPorEspacioId(self, idEspacio):
    #     self.connectarSql()
    #     mycursor = self.mysqlConector.cursor()
    #     datos = (idEspacio)
    #     mycursor.execute(self.queryRecuperarPlantaPorEspacioId, datos)
    #     plantas = mycursor.fetchall()
    #     self.cerrarSql()
    #     plantas = self.formarPlantas(plantas)
    #     return plantas
    #
    # def obtenerPlantaPorId(self, id):
    #     self.connectarSql()
    #     mycursor = self.mysqlConector.cursor()
    #     datos = (id)
    #     mycursor.execute(self.queryRecuperarPlantaPorId, datos)
    #     planta = mycursor.fetchall()
    #     self.cerrarSql()
    #     planta = self.formarPlantas(planta)
    #     return planta
    #
    #
    # def obtenerEspacio(self):
    #     self.connectarSql()
    #     mycursor = self.mysqlConector.cursor()
    #     mycursor.execute(self.queryRecuperarEsapcios)
    #     espacios = mycursor.fetchall()
    #     self.cerrarSql()
    #     espacios = self.formarEspacios(espacios)
    #     return espacios
    #
    # def obtenerEspacioPorId(self, id):
    #     self.connectarSql()
    #     mycursor = self.mysqlConector.cursor()
    #     datos = (id)
    #     mycursor.execute(self.queryRecuperarEsapcioPorId, datos)
    #     espacio = mycursor.fetchall()
    #     self.cerrarSql()
    #     espacio = self.formarEspacios(espacio)
    #     return espacio
    #
    # def obtenerRegistroPorId(self, id):
    #     self.connectarSql()
    #     mycursor = self.mysqlConector.cursor()
    #     mycursor.execute(self.querySelecionerRegistroPorId, (id))
    #     registros = mycursor.fetchall()
    #     self.cerrarSql()
    #     registros = self.formarRegistros(registros)
    #     return registros
    #
    # def obtenerSensosPorIdYFechas(self, id, fechaInicio, fechaFin):
    #     self.connectarSql()
    #     mycursor = self.mysqlConector.cursor()
    #     mycursor.execute(self.querySelecionerRegistroPorIdYFechas, (id, fechaInicio, fechaFin))
    #     registros = mycursor.fetchall()
    #     self.cerrarSql()
    #     registros = self.formarRegistros(registros)
    #     return registros





    #
    # #funciones para crear objetos recuperados
    # def formarPlantas(self, listaPlantas):
    #     listaPlantasFormados = []
    #     for datosPlanta in listaPlantas:
    #         plantaRecuperada = Planta(datosPlanta[1], datosPlanta[2], datosPlanta[0], datosPlanta[3])
    #         listaPlantasFormados.append(plantaRecuperada)
    #     return listaPlantasFormados
    #
    # def formarEspacios(self, listaEspacios):
    #     listaEspaciosFormados = []
    #     for datosEspacio in listaEspacios:
    #         plantaRecuperada = Espacio(datosEspacio[1], datosEspacio[2], datosEspacio[4], datosEspacio[3], datosEspacio[0])
    #         listaEspaciosFormados.append(plantaRecuperada)
    #     return listaEspaciosFormados
    #
    # def formarRegistros(self, listaRegistros):
    #     listaRegistrosFormados = []
    #     for datosRegistro in listaRegistros:
    #         plantaRecuperada = Registro(datosRegistro[0], datosRegistro[1], datosRegistro[2], datosRegistro[3])
    #         listaRegistrosFormados.append(plantaRecuperada)
    #     return listaRegistrosFormados

engine = create_engine('sqlite:///ficus.db', echo=True)

Base.metadata.create_all(engine)
