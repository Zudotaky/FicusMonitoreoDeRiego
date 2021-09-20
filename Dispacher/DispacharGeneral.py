

class Dispacher:

    dao = None;


    def jsonificarLista(self,lista):
        jsonLista = []
        for planta in lista:
            jsonLista.append(planta.jsonificar())
        return jsonLista