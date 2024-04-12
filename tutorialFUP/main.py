#configuracion inicial
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

#Servicio que usaremos, funcion de Python que sirve para
#Usaremos el Crud
#Primer elemento a usar se usara un elemento de flask, de la siguiente manera:
#En la linea de app.route es el camino que se toma para ejecutar cierta accion,todo se hace a traves de la url

@app.route("/", methods=['GET'])
def test ():
    json = {}
    json["message"] = "Server Running..." #Esto hay que convertir una variable de tipo json
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running: " + "http://" + dataConfig['url-backend'] + ":" + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])
