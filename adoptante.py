from mascota import Mascota
from adopcion import Adopcion

class Adoptante:
    
    def __init__(self, nombre, dni, mascota):
        self.setNombre(nombre)
        self.setDNI(dni)
        self.historial_adopciones = []
        self.setMascota(mascota)

    def setNombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena de texto no vacía.")
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setDNI(self, dni):
        if not isinstance(dni, str) or not dni.strip():
            raise ValueError("El DNI debe ser una cadena de texto no vacía.")
        self.dni = dni

    def getDNI(self):
        return self.dni
    
    def setMascota(self,mascota):
        if not isinstance(mascota, Mascota):
            raise TypeError('La mascota debe ser una instancia de la clase Mascota')
        self.mascota=mascota

    def getMascota(self):
        return self.mascota
    
    def registrarAdopcion(self, adopcion):
        if not isinstance(adopcion, Adopcion):
            raise TypeError("La adopción debe ser una instancia de la clase Adopcion.")
        self.historial_adopciones.append(adopcion)
    
    def consultarAdopciones(self):
        if not self.historial_adopciones:
            print("No hay adopciones registradas.")
            return
        for adopcion in self.historial_adopciones:
            print(adopcion.consultarAdopcion())

    def __str__(self):
       return f"Nombre: {self.nombre}\n DNI: {self.dni}\n Cantidad de adopciones: {len(self.historial_adopciones)}"