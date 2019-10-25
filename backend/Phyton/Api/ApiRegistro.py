
from flask_restplus import Resource, Namespace, reqparse
from backend.Phyton.Dispacher.DispatcherRegistro import DispatcherRegistro

registroRequest = Namespace('Registro', description='Registro request')

dispacherRegistro = DispatcherRegistro()



crear = reqparse.RequestParser()
crear.add_argument('id', type=int, required=True)
crear.add_argument('humedad', type=int, required=False)
crear.add_argument('temperatura', type=int, required=False)

# Servicios De Reporte
@registroRequest.route('/crearReporte', methods=['POST'])
@registroRequest.expect(crear)
class crearReporte(Resource):

    def post(self):
        jsonRequest = crear.parse_args()
        idPlanta = jsonRequest['id']
        humedad = jsonRequest['humedad']
        temperatura = jsonRequest['temperatura']
        registro = dispacherRegistro.crearReporte(idPlanta, humedad, temperatura)
        return registro

# Servicios que modifican

# Sercicios de consulta

obtenerPorIdPlanta = reqparse.RequestParser()
obtenerPorIdPlanta.add_argument('id', type=int, required=True)

@registroRequest.route('/obtenerSensosPorId',methods=['POST'])
@registroRequest.expect(obtenerPorIdPlanta)
class obtenerReportePorIdPlanta(Resource):

    def post(self):
        jsonRequest = obtenerPorIdPlanta.parse_args()
        id = jsonRequest['id']
        listaDeRegistros = dispacherRegistro.obtenerRegistroPorIdPlanta(id)
        return {'Registros': list(listaDeRegistros)}




obtenerPorFecha = reqparse.RequestParser()
obtenerPorFecha.add_argument('id', type=int, required=True)
obtenerPorFecha.add_argument('fechaInicio', type=str, required=True)
obtenerPorFecha.add_argument('fechaFin', type=str, required=True)


@registroRequest.route('/obtenerSensosPorFecha',methods=['POST'])
@registroRequest.expect(obtenerPorFecha)
class obtenerReportePorFecha(Resource):
    def post(self):
        jsonRequest = obtenerPorFecha.parse_args()
        id = jsonRequest['id']
        fechaInicio= jsonRequest['fechaInicio']
        fechaFin= jsonRequest['fechaFin']
        listaDeRegistros = dispacherRegistro.obtenerRegistroPorIdPlantaYFecha(id, fechaInicio, fechaFin)
        return {'Registros': list(listaDeRegistros)}

