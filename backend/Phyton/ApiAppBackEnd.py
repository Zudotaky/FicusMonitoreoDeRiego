import ast
import json


from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from backend.Phyton.Jardinero import Jardinero

app = Flask(__name__, template_folder="templates")
marsh = Marshmallow(app)
jardinero = Jardinero()


# Servicios De Planta
@app.route('/agregarPlanta', methods=['POST'])
def crearPlanta():
    jsonRequest = request.get_json(force=True)
    nombre = jsonRequest['nombre']
    descripcion = jsonRequest['descripcion']
    planta = jardinero.crearPlanta(nombre, descripcion)
    return json.dumps(planta)

# Servicios que modifican

# modificarPlanta

# Sercicios de consulta

@app.route('/obtenerPlantas', methods=['GET'])
def obtenerPlantas():
    listaDePlantas = jardinero.obtenerPlantas()
    return json.dumps({'Plantas': list(listaDePlantas)})

@app.route('/obtenerPlantaPorId', methods=['POST'])
def obtenerPlantaPorId():
    jsonRequest = request.get_json(force=True)
    id = jsonRequest['id']
    planta = jardinero.obtenerPlantaPorId(id)
    return json.dumps(planta)

@app.route('/getPlantasDeEspacio', methods=['POST'])
def obtenerPlantasPorEspacio():
    jsonRequest = request.get_json(force=True)
    idEspacio = jsonRequest['idEspacio']
    listaDePlantas = jardinero.obtenerPlantasPorEspacioId(idEspacio)
    return json.dumps({'Plantas': list(listaDePlantas)})








# Servicios De Espacio
@app.route('/agregarEspacio',methods=['POST'])
def crearEspacio():
    jsonRequest = request.get_json(force=True)
    nombre = jsonRequest['nombre']
    descripcion = jsonRequest['descripcion']
    espacio = jardinero.crearEspacio(nombre,descripcion)
    return json.dumps(espacio)

# modificarEspacio
@app.route('/agregarPlantaAEspacio',methods=['POST'])
def agregarPlantaAEsapcio():
    jsonRequest = request.get_json(force=True)
    idEspacio = jsonRequest['Espacio']
    idPlanta = jsonRequest['Planta']
    jardinero.agregarPlantaAEspacio(idPlanta,idEspacio)
    return json.dumps({})
# Sercicios de consulta

@app.route('/getEspacios',methods=['GET'])
def ObtenerEspacios():
    espacios = jardinero.obtenerEspacios()
    return json.dumps({'Espacios':list(espacios)})

@app.route('/getEspacioPorId',methods=['POST'])
def obtenerEspacioPorid():
    jsonRequest = request.get_json(force=True)
    id = jsonRequest['id']
    espacio = jardinero.obtenerEspacioPorId(id)
    return json.dumps(espacio)






# Servicios De Reporte
@app.route('/crearReporte',methods=['POST'])
def crearReporte():
    datosPlanta = ast.literal_eval(request.data.decode("utf-8"))
    # jsonRequest = request.get_json(force=True)
    # idPlanta = jsonRequest['id']
    # humedad = jsonRequest['humedad']
    # temperatura = jsonRequest['temperatura']
    registro = jardinero.crearReporte(datosPlanta[0], datosPlanta[1], datosPlanta[2])
    return json.dumps(registro)

# Servicios que modifican

# Sercicios de consulta

@app.route('/obtenerSensosIPord',methods=['POST'])
def obtenerReportePorIdPlanta():
    jsonRequest = request.get_json(force=True)
    id = jsonRequest['id']
    listaDeRegistros = jardinero.obtenerRegistroPorIdPlanta(id)
    return json.dumps({'Registros': list(listaDeRegistros)})

@app.route('/obtenerSensosPorFecha',methods=['POST'])
def obtenerReportePorFecha():
    jsonRequest = request.get_json(force=True)
    id = jsonRequest['id']
    fechaInicio= jsonRequest['fechaInicio']
    fechaFin= jsonRequest['fechaFin']
    listaDeRegistros = jardinero.obtenerRegistroPorIdPlantaYFecha(id, fechaInicio, fechaFin)
    return json.dumps({'Registros': list(listaDeRegistros)})







# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run()
    # app.  run(host='0.0.0.0')