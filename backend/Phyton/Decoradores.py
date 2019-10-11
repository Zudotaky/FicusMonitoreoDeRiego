

class jsonificable():

    def jsonificar(self):
        data = {}
        for atributo in [atributo for atributo in self.__dict__ if not atributo.startswith('_')]:
            data[atributo] = self.__getattribute__(atributo)
        return data



def session(funcion):
    def decorada(self, obj, *args):
        self.currentSession = self.sessionConfig()
        reapuesta = funcion(self, obj, *args)
        self.currentSession.commit()
        self.currentSession.refresh(obj)
        self.currentSession.close()
        return reapuesta
    return decorada

def connecion(funcion):
    def decorada(self, *args):
        self.currentSession = self.sessionConfig()
        respuesta = funcion(self,*args)
        self.currentSession.close()
        return respuesta
    return decorada