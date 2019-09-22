from DateTime import DateTime


class Registro():

    def __init__(self, idPlanta, humedad = None, temperatura = None, fecha = DateTime.DateTime()):
        self.__idPlanta = idPlanta
        self.__horarioRegistrado = fecha
        self.__humedad = humedad
        self.__temperatura = temperatura

    def plantaId(self):
        return self.__idPlanta

    def horarioDeRegistro(self):
        return self.__horarioRegistrado

    def humedad(self):
        return self.__humedad

    def temperatura(self):
        return self.__temperatura