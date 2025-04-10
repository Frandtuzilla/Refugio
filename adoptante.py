class Adoptante:
    
    def __init__(self, nombre, dni):
        self.setNombre(nombre)
        self.setDNI(dni)
        self.historial_adopciones = []

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