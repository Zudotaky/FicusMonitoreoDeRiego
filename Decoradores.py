

class jsonificable():

    def jsonificar(self):
        data = {}
        for atributo in [atributo for atributo in self.__dict__ if not atributo.startswith('_')]:
            data[atributo] = self.__getattribute__(atributo)
        return data



def session(funcion):
    def decorada(self, obj, *args):
        reapuesta = funcion(self, obj, *args)
        self.currentSession.commit()
        self.currentSession.refresh(obj)
        return reapuesta
    return decorada

def connecion(funcion):
    def decorada(self, *args):
        respuesta = funcion(self,*args)
        return respuesta
    return decorada