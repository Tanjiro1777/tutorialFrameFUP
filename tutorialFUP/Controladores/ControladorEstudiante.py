from Modelos.Estudiante import Estudiante

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorEstudiante():

    def init(self):
        print("Creando ControladorEstudiante")

    def index(self):
        print("Listar todos los estudiantes")
        unEstudiante = {
            "_id": "abc123",
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return [unEstudiante]

    def create(self, infoEstudiante):
        print("Crear un estudiante")
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__

    def show(self, id):
        print("Mostrando un estudiante con id ", id)
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elEstudiante

    def update(self, id, infoEstudiante):
        print("Actualizando estudiante con id", id)
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__

    def delete(self, id):
        print("Elimiando estudiante con id ", id)
        return {"deleted_count": 1}