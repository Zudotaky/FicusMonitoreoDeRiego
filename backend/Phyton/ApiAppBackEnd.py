import ast

from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow

from backend.Phyton.Jardinero import Jardinero

app = Flask(__name__, template_folder="templates")
marsh = Marshmallow(app)
jardinero = Jardinero()


# Servicios De Alta
@app.route('/agregarPlanta',methods=['POST'])
def crearPlanta():
    json = request.get_json(force=True)
    nombre = json['nombre']
    descripcion = json['descripcion']
    planta = jardinero.crearPlanta(nombre,descripcion)
    return jsonify({'id': planta.id})

@app.route('/crearEspacio',methods=['POST'])
def crearEspacio():
    json = request.get_json(force=True)
    nombre = json['id']
    descripcion = json['descripcion']
    espacio = jardinero.crearEspacio(nombre,descripcion)
    return jsonify()

@app.route('/crearReporte',methods=['POST'])
def crearReporte():
    datosPlanta = ast.literal_eval(request.data.decode("utf-8"))
    # json = request.get_json(force=True)
    # idPlanta = json['id']
    # humedad = json['humedad']
    # temperatura = json['temperatura']
    registro = jardinero.crearReporte(datosPlanta[0], datosPlanta[1], datosPlanta[2])
    return jsonify()


# Servicios que modifican

# modificarEspacio - modificarPlanta



# Sercicios de consulta


@app.route('/getPlantas',methods=['GET'])
def obtenerPlantas():
    nombres = jardinero.obtenerPlantas()
    return jsonify({'Plantas' : nombres })

@app.route('/getPlantaPorId',methods=['POST'])
def obtenerPlantaPorId():
    json = request.get_json(force=True)
    id = json['id']
    planta = jardinero.obtenerPlantaPorId(id)
    return jsonify({'Planta': planta})

@app.route('/getPlantasDeEspacio',methods=['POST'])
def obtenerPlantasPorEspacio():
    json = request.get_json(force=True)
    idEspacio = json['idEspacio']
    plantas = jardinero.obtenerPlantasPorEspacioId(idEspacio)
    return plantas

# @app.route('/')
# def obtenerPlantasPortipoDeEspacio():

@app.route('/getEspacios',methods=['GET'])
def ObtenerEspacios():
    espacios = jardinero.obtenerEspacios()
    return espacios

@app.route('/getEspacioPorId',methods=['POST'])
def obtenerEspacioPorid():
    json = request.get_json(force=True)
    id = json['id']
    espacio = jardinero.obtenerEspacioPorId(id)
    return espacio

# @app.route('/')
# def obtenerEspaciosPorTipo():

@app.route('/obtenerSensosIPord',methods=['POST'])
def obtenerReportePorIdPlanta():
    json = request.get_json(force=True)
    id = json['id']
    listaDeSenseos = jardinero.obtenerSenseoPorIdPlanta(id)
    return jsonify({'Sensos': listaDeSenseos})

@app.route('/obtenerSensosPorFecha',methods=['POST'])
def obtenerReportePorFecha():
    json = request.get_json(force=True)
    id = json['id']
    fechaInicio= json['fechaInicio']
    fechaFin= json['fechaFin']
    listaDeSenseos = jardinero.obtenerSenseoPorIdPlantaYFecha(id, fechaInicio, fechaFin)
    return jsonify({'Sensos' : listaDeSenseos})


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run()
    # app.  run(host='0.0.0.0')