

class jsonificable():

    def jsonificar(self):
        data = {}
        for atributo in [atributo for atributo in self.__dict__ if not atributo.startswith('_')]:
            data[atributo] = self.__getattribute__(atributo)
        return data



def session(funcion):
    def decorada(self, obj):
        self.session = self.sessionConfig()
        reapuesta = funcion(self, obj)
        self.session.commit()
        self.session.refresh(obj)
        self.session.close()
        return reapuesta
    return decorada

def connecion(funcion):
    def decorada(self, *args):
        self.session = self.sessionConfig()
        respuesta = funcion(self,*args)
        self.session.close()
        return respuesta
    return decorada