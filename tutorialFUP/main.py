#configuracion inicial
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEstudiante import ControladorEstudiante


app = Flask(__name__)
cors = CORS(app)


#Implementacion de los metodos
miControladorEstudiante=ControladorEstudiante()

#Servicio que usaremos, funcion de Python que sirve para
#Usaremos el Crud
#Primer elemento a usar se usara un elemento de flask, de la siguiente manera:
#En la linea de app.route es el camino que se toma para ejecutar cierta accion,todo se hace a traves de la url


@app.route("/", methods=['GET'])
def test ():
    json = {}
    json["message"] = "Server Running..." #Esto h
    # ay que convertir una variable de tipo json
    return jsonify(json)

################################################################

@app.route("/estudiantes", methods=['GET'])
def getEstudiantes():
    json = miControladorEstudiante.index()
    return jsonify(json)


@app.route("/estudiantes", methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json = miControladorEstudiante.create(data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['GET'])
def getEstudiante(id):
    json = miControladorEstudiante.show(id)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json = miControladorEstudiante.update(id, data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
    json = miControladorEstudiante.delete(id)
    return jsonify(json)


#####################################################################



def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running: " + "http://" + dataConfig['url-backend'] + ":" + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])
