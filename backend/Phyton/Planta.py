

class Planta():

    def __init__(self,nombre,descripcion, id = None, espacio = None ):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__espacioActual = espacio
        self.__id = id

    def nombre(self):
        return self.__nombre

    def descripcion(self):
        return self.__descripcion

    def id(self):
        return self.__id

    def cambiarId(self,id):
        self.__id = id