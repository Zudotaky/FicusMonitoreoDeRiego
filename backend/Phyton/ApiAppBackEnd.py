import ast

from  flask import Flask  , request, jsonify
from flask_marshmallow import Marshmallow

from backend.Phyton.Jardinero import Jardinero

app = Flask(__name__, template_folder="templates")
marsh = Marshmallow(app)
jardinero = Jardinero()

# Create a URL route in our application for "/"
@app.route('/getFlores',methods=['GET'])
def getFlores():
    nombres = jardinero.obtenerPlantas()
    return jsonify({'Flores' : nombres })


@app.route('/agregarPlanta',methods=['POST'])
def crearPlanta():
    json = request.get_json(force=True)
    nombre = json['nombre']
    descripcion = json['descripcion']
    jardinero.nuevaPlanta(nombre,descripcion)
    return jsonify(), 200

# get que recive raw string con dry ,wet ,verry wet y id , seguarda con fecha
@app.route('/sensar',methods=['POST'])
def sensar():
    datosPlanta = ast.literal_eval(request.data.decode("utf-8"))
    jardinero.sensar(datosPlanta[1], datosPlanta[0])
    return jsonify(),200

# post con 2 fechas y un id que devuelva un { [{ humedades:, fechas: } ]}
@app.route('/obtenerSenesos',methods=['POST'])
def datosSeneso():
    json = request.get_json(force=True)
    id = json['id']
    fechaInicio= json['fechaInicio']
    fechaFin= json['fechaFin']
    listaDeSenseos = jardinero.otenerSenseo(id,fechaInicio,fechaFin)
    return jsonify(listaDeSenseos),200

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run()