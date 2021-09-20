from flask_restplus import Resource, Namespace, reqparse
from Dispacher.DispatcherPlanta import DispatcherPlanta

plantasRequest = Namespace('Plantas', description='Plantas request')

dispacherPlanta = DispatcherPlanta()


# Servicios De Planta

crear = reqparse.RequestParser()
crear.add_argument('descripcion', type=str, required=True)
crear.add_argument('nombre', type=str, required=True)
crear.add_argument('url')


@plantasRequest.route('/Agregar',methods=['POST'])
@plantasRequest.expect(crear)
class crearPlanta(Resource):

    @plantasRequest.doc('planta')
    def post(self):
        jsonRequest = crear.parse_args()
        nombre = jsonRequest['nombre']
        descripcion = jsonRequest['descripcion']
        url = jsonRequest['url']
        planta = dispacherPlanta.crearPlanta(nombre, descripcion, url)
        return planta

# Servicios que modifican

# modificarPlanta

# Sercicios de consulta


@plantasRequest.route('/Obtener', methods=['GET'])
class obtenerPlantas(Resource):

    @plantasRequest.doc('lista_plantas')
    def get(self):
        listaDePlantas = dispacherPlanta.obtenerPlantas()
        return {'Plantas': list(listaDePlantas)}


obtenerPorId = reqparse.RequestParser()
obtenerPorId.add_argument('id', type=int, required=True)

@plantasRequest.route('/ObtenerPorId', methods=['POST'])
@plantasRequest.expect(obtenerPorId)
class obtenerPlantaPorId(Resource):

    @plantasRequest.doc('lista_plantas')
    def post(self):
        jsonRequest = obtenerPorId.parse_args()
        print(jsonRequest)
        id = jsonRequest['id']
        print(id)
        planta = dispacherPlanta.obtenerPlantaPorId(id)
        return planta




obtenerPorIdEspacio = reqparse.RequestParser()
obtenerPorIdEspacio.add_argument('idEspacio', type=int, required=True)

@plantasRequest.route('/ObtenerPorEspaioId', methods=['POST'])
@plantasRequest.expect(obtenerPorIdEspacio)
class obtenerPorEspaioId(Resource):

    @plantasRequest.doc('lista_plantas')
    def post(self):
        jsonRequest = obtenerPorIdEspacio.parse_args()
        idEspacio = jsonRequest['idEspacio']
        listaDePlantas = dispacherPlanta.obtenerPlantasPorEspacioId(idEspacio)
        return {'Plantas': list(listaDePlantas)}


@plantasRequest.route('/ObtenerSinEspacio', methods=['GET'])
class ObtenerSinEspacio(Resource):

    @plantasRequest.doc('lista_plantas')
    def get(self):
        listaDePlantas = dispacherPlanta.obtenerPlantasSinEspacio()
        return {'Plantas': list(listaDePlantas)}