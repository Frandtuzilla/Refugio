from mascota import Mascota 
from adoptante import Adoptante
from adopcion import Adopcion 

class Refugio:
    
    def __init__(self, nombre, nit, direccion):
        self.setNombre(nombre)
        self.setNIT(nit)
        self.setDireccion(direccion)
        self.mascotas = []
        self.adoptantes = []
        self.adopciones = []

    def setNombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena de texto no vacía.")
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setNIT(self, nit):
        if not isinstance(nit, str) or not nit.strip():
            raise ValueError("El NIT debe ser una cadena de texto no vacía.")
        self.nit = nit

    def getNIT(self):
        return self.nit

    def setDireccion(self, direccion):
        if not isinstance(direccion, str) or not direccion.strip():
            raise ValueError("La dirección debe ser una cadena de texto no vacía.")
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion

    def agregarMascota(self, mascota):
        if mascota in self.mascotas:
            raise ValueError("La mascota ya está registrada en el refugio.")
        self.mascotas.append(mascota)

    def eliminarMascota(self, mascota_id):
        mascota = self.buscarMascota(mascota_id)
        if mascota:
            self.mascotas.remove(mascota)
        else:
            raise ValueError("La mascota no existe en el refugio.")

    def buscarMascota(self, mascota_id):
        for mascota in self.mascotas:
            if mascota.getId() == mascota_id:
                return mascota
        return None

    def agregarAdoptante(self, adoptante):
        if adoptante in self.adoptantes:
            raise ValueError("El adoptante ya está registrado en el refugio.")
        self.adoptantes.append(adoptante)

    def eliminarAdoptante(self, dni):
        adoptante = self.buscarAdoptante(dni)
        if adoptante:
            self.adoptantes.remove(adoptante)
        else:
            raise ValueError("El adoptante no existe en el refugio.")

    def buscarAdoptante(self, dni):
        for adoptante in self.adoptantes:
            if adoptante.getDNI() == dni:
                return adoptante
        return None

    def modificarMascota(self, mascota_id, nuevo_nombre=None, nuevo_tipo=None, nueva_edad=None, nueva_disponibilidad=None):
        mascota = self.buscarMascota(mascota_id)
        if not mascota:
            raise ValueError("La mascota con ese ID no existe.")

        if nuevo_nombre is not None:
            mascota.setNombre(nuevo_nombre)
        if nuevo_tipo is not None:
            mascota.setTipo(nuevo_tipo)
        if nueva_edad is not None:
            mascota.setEdad(nueva_edad)
        if nueva_disponibilidad is not None:
            mascota.setDisponibilidad(nueva_disponibilidad)

    def modificarAdoptante(self, dni, nuevo_nombre=None, mascota_nueva=None):
        adoptante = self.buscarAdoptante(dni)
        if not adoptante:
            raise ValueError("El adoptante con ese ID no existe.")

        if nuevo_nombre is not None:
            adoptante.setNombre(nuevo_nombre)
        if mascota_nueva is not None:
            adoptante.setMascota(mascota_nueva)

    def consultarMascota(self, mascota_id, nombre=None, tipo=None, edad=None, disponibilidad=None):
        mascota = self.buscarMascota(mascota_id)
        if not mascota:
            raise ValueError("La mascota con ese ID no existe.")

        if nombre is not None:
            mascota.getNombre
        if tipo is not None:
            mascota.getTipo
        if edad is not None:
            mascota.getEdad
        if disponibilidad is not None:
            mascota.getDisponibilidad

    def consultarAdoptante(self, dni, nombre=None, mascota=None):
        adoptante = self.buscarAdoptante(dni)
        if not adoptante:
            raise ValueError("El adoptante con ese ID no existe.")

        if nombre is not None:
            adoptante.getNombre
        if mascota is not None:
            adoptante.getMascota

    def consultarAdopciones(self):
        for adoptante in self.adoptantes:
            adopciones = adoptante.getAdopciones()
            if adopciones:
                print(f"Adoptante: {adoptante.getNombre()} (DNI: {adoptante.getDNI()})")
                for adopcion in adopciones:
                    print(f"  - {adopcion}")