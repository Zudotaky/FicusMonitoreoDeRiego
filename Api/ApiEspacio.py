from flask_restplus import Resource, Namespace, reqparse
from Dispacher.DispatcherEspacio import DispatcherEspacio

espacioRequest = Namespace('Espacio', description='Espacio request')

dispacherEspacio = DispatcherEspacio()



# Servicios De Espacio

crear = reqparse.RequestParser()
crear.add_argument('descripcion', type=str, required=True)
crear.add_argument('nombre', type=str, required=True)
crear.add_argument('url')


@espacioRequest.route('/Agregar',methods=['POST'])
@espacioRequest.expect(crear)
class crearEspacio(Resource):

    def post(self):
        jsonRequest = crear.parse_args()
        nombre = jsonRequest['nombre']
        descripcion = jsonRequest['descripcion']
        url = jsonRequest['url']
        espacio = dispacherEspacio.crear(nombre, descripcion, url)
        return espacio



# modificarEspacio

agregarPlantaEspaio = reqparse.RequestParser()
agregarPlantaEspaio.add_argument('Espacio', type=str, required=True)
agregarPlantaEspaio.add_argument('Planta', type=str, required=True)

@espacioRequest.route('/AgregarPorPlantaId',methods=['POST'])
@espacioRequest.expect(agregarPlantaEspaio)
class agregarPlantaAEsapcio(Resource):

    def post(self):
        jsonRequest = agregarPlantaEspaio.parse_args()
        idEspacio = jsonRequest['Espacio']
        idPlanta = jsonRequest['Planta']
        dispacherEspacio.agregarPlantaAEspacio(idPlanta, idEspacio)
        return { 200 }



# Sercicios de consulta

@espacioRequest.route('/obtenerEspacios',methods=['GET'])
class ObtenerEspacios(Resource):

    def get(self):
        espacios = dispacherEspacio.obtenerEspacios()
        return {'Espacios':list(espacios)}


obtenerEspacios = reqparse.RequestParser()
obtenerEspacios.add_argument('id', type=str, required=True)

@espacioRequest.route('/obtenerEspacioPorId',methods=['POST'])
@espacioRequest.expect(obtenerEspacios)
class obtenerEspacioPorid(Resource):

    def post(self):
        jsonRequest = obtenerEspacios.parse_args()
        id = jsonRequest['id']
        espacio = dispacherEspacio.obtenerEspacioPorId(id)
        return espacio
