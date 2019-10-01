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
@app.route('/crearEspacio',methods=['POST'])
def crearEspacio():
    json = request.get_json(force=True)
    nombre = json['id']
    descripcion = json['descripcion']
    espacio = jardinero.crearEspacio(nombre,descripcion)
    return json.dumps(espacio)

# Servicios que modifican

# modificarEspacio

# Sercicios de consulta

@app.route('/getEspacios',methods=['GET'])
def ObtenerEspacios():
    espacios = jardinero.obtenerEspacios()
    return json.dumps({'Espacios':list(espacios)})

@app.route('/getEspacioPorId',methods=['POST'])
def obtenerEspacioPorid():
    json = request.get_json(force=True)
    id = json['id']
    espacio = jardinero.obtenerEspacioPorId(id)
    return json.dumps(espacio)






# Servicios De Reporte
@app.route('/crearReporte',methods=['POST'])
def crearReporte():
    datosPlanta = ast.literal_eval(request.data.decode("utf-8"))
    # json = request.get_json(force=True)
    # idPlanta = json['id']
    # humedad = json['humedad']
    # temperatura = json['temperatura']
    registro = jardinero.crearReporte(datosPlanta[0], datosPlanta[1], datosPlanta[2])
    return json.dumps(registro)

# Servicios que modifican

# Sercicios de consulta

@app.route('/obtenerSensosIPord',methods=['POST'])
def obtenerReportePorIdPlanta():
    json = request.get_json(force=True)
    id = json['id']
    listaDeRegistros = jardinero.obtenerRegistroPorIdPlanta(id)
    return json.dumps({'Registros': list(listaDeRegistros)})

@app.route('/obtenerSensosPorFecha',methods=['POST'])
def obtenerReportePorFecha():
    json = request.get_json(force=True)
    id = json['id']
    fechaInicio= json['fechaInicio']
    fechaFin= json['fechaFin']
    listaDeRegistros = jardinero.obtenerRegistroPorIdPlantaYFecha(id, fechaInicio, fechaFin)
    return jsonify({'Registros': listaDeRegistros})







# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run()
    # app.  run(host='0.0.0.0')