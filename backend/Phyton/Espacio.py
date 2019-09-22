from enum import Enum



class TipoDeEspacio(Enum):
    INDIVIDUAL = 'INDIVIDUAL'
    GRUPAL = 'GRUPAL'

    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)


class Espacio():

    def __init__(self, nombre, descripcion, tipoDeEspacio = TipoDeEspacio.INDIVIDUAL, plantas = None, id = None):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__plantasId = plantas
        self.__id = id
        self.__tipoDeEspacio = tipoDeEspacio

    def nombre(self):
        return self.__nombre

    def descripcion(self):
        return self.__descripcion

    def plantasId(self):
        return self.__plantasId

    def id(self):
        return self.__id

    def tipiDeEspacio(self):
        return self.__tipoDeEspacio.name

    def cambiarId(self, id):
        self.__id = id