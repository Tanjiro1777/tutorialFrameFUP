from Modelos.Materia import Materia
from Repositorios.RepositorioMateria import RepositorioMateria
from Repositorios.RepositorioDepartamento import RepositorioDepartamento

class ControladorMateria():
    def __init__(self):
        print('creando controlador Materia')
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
       return self.repositorioMateria.findAll()

    def create(self, infoMateria):
        print("Crear una materia")
        nuevoMateria = Materia(infoMateria)
        return self.repositorioMateria.save(nuevoMateria)

    def show(self, id):
        print('mostar materia con id ',id)
        elMateria = Materia(self.repositorioMateria.findById(id))
        return elMateria.__dict__

    def update(self, id, infoMateria):
        print("Actualizando materia con id",id)
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)

    def delete(self , id):
        print('eliminar materia con id ',id)
        return self.repositorioMateria.delete(id)