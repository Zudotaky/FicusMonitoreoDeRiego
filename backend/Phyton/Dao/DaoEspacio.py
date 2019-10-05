from backend.Phyton.Dao.DaoGeneral import DaoGeneral
from backend.Phyton.Decoradores import session, connecion
from backend.Phyton.Espacio import Espacio


class DaoEspacio(DaoGeneral):

    @session
    def persistirEspacio(self, espacio):
        self.session.add(espacio)
        return espacio

    @connecion
    def obtenerEspacio(self):
        return self.session.query(Espacio).all()

    @connecion
    def obtenerEspacioPorId(self, id):
        return self.session.query(Espacio).filter(Espacio.id == id).one()

    @session
    def agregarPlantaAEspacio(self, espacio_planta):
        return self.session.add(espacio_planta)