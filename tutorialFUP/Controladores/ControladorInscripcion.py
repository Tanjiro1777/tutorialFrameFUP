from Modelos.Inscripcion import Inscripcion
from Repositorios.RepositorioInscripcion import RepositorioInscripcion

class ControladorInscripcion():
    def __init__(self):
        self.repositorioInscripcion = RepositorioInscripcion()

    def index(self):
        # Retorna todos los Inscripcion existentes en la base de datos
        return self.repositorioInscripcion.findAll()

    def create(self, infoInscripcion):
        nuevaInscripcion = Inscripcion(infoInscripcion)

        return self.repositorioInscripcion.save(nuevaInscripcion)

    def show(self, id):
        laInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))

        return laInscripcion.__dict__

    def update(self, id, infoInscripcion):
        inscripcionActual = Inscripcion(self.repositorioInscripcion.findById(id))

        inscripcionActual.año = infoInscripcion["año"]
        inscripcionActual.semestre = infoInscripcion["semestre"]
        inscripcionActual.nota_final = infoInscripcion["nota_final"]

        return self.repositorioInscripcion.save(inscripcionActual)

    def delete(self, id):
        return self.repositorioInscripcion.delete(id)

