from mascota import Mascota
from adoptante import Adoptante

class Adopcion:
    
    def __init__(self, id_adopcion: int, adoptante:Adoptante, mascota:Mascota, fecha_adopcion:str):
        self.setIdAdopcion(id_adopcion)
        self.setAdoptante(adoptante)
        self.setMascota(mascota)
        self.setFechaAdopcion(fecha_adopcion)

    def setIdAdopcion(self, id_adopcion):
        if not isinstance(id_adopcion, int) or id_adopcion <= 0:
            raise ValueError("El ID de adopción debe ser un número entero positivo.")
        self.id_adopcion = id_adopcion

    def getIdAdopcion(self):
        return self.id_adopcion

    def setAdoptante(self, adoptante):
        if not isinstance(adoptante, Adoptante):
            raise TypeError("El adoptante debe ser una instancia de la clase Adoptante.")
        self.adoptante = adoptante

    def getAdoptante(self):
        return self.adoptante

    def setMascota(self, mascota):
        if not isinstance(mascota, Mascota):
            raise TypeError("La mascota debe ser una instancia de la clase Mascota.")
        self.mascota = mascota

    def getMascota(self):
        return self.mascota

    def setFechaAdopcion(self, fecha_adopcion):
        if not isinstance(fecha_adopcion, str) or not fecha_adopcion.strip():
            raise ValueError("La fecha de adopción debe ser una cadena de texto no vacía.")
        self.fecha_adopcion = fecha_adopcion

    def getFechaAdopcion(self):
        return self.fecha_adopcion

    def consultarAdopcion(self):
        return f"ID Adopción: {self.id_adopcion}, Adoptante: {self.adoptante.getNombre()}, Mascota: {self.mascota.getNombre()}, Fecha: {self.fecha_adopcion}"

    def __str__(self):
        return f"ID Adopción: {self.id_adopcion}, Adoptante: {self.adoptante.getNombre()}, Mascota: {self.mascota.getNombre()}, Fecha: {self.fecha_adopcion}"
    
