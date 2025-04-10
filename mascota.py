class Mascota:
    
    TIPOS = ["Perro", "Gato", "Tortuga"]

    ids_usados = []

    def __init__(self, nombre, id, tipo, edad, disponibilidad=True):
        self.setNombre(nombre)
        self.setId(id)
        self.setTipo(tipo)
        self.setEdad(edad)
        self.setDisponibilidad(disponibilidad)

    def setNombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if len(nombre.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío.")
        if not nombre.strip().isalpha():
            raise ValueError("El nombre solo puede contener letras.")
        self.nombre = nombre

    def setId(self, id):
        if not isinstance(id, int):
            raise TypeError("El ID debe ser un número entero.")
        if id <= 0:
            raise ValueError("El ID debe ser un número positivo.")
        if id in Mascota.ids_usados:
            raise ValueError("El ID ya existe.")
        Mascota.ids_usados.append(id)
        self.id = id

    def setTipo(self, tipo):
        if tipo not in Mascota.TIPOS:
            raise ValueError(f"Tipo inválido. Debe ser uno de los siguientes: {Mascota.TIPOS}.")
        self.tipo = tipo

    def setEdad(self, edad):
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.edad = edad

    def setDisponibilidad(self, disponibilidad):
        if not isinstance(disponibilidad, bool):
            raise TypeError("La disponibilidad debe ser un valor booleano.")
        self.disponibilidad = disponibilidad

    def getNombre(self):
        return self.nombre

    def getId(self):
        return self.id

    def getTipo(self):
        return self.tipo

    def getEdad(self):
        return self.edad

    def getDisponibilidad(self):
        return self.disponibilidad

    def adoptarMascota(self):
        if not self.disponibilidad:
            raise ValueError("La mascota ya ha sido adoptada.")
        self.disponibilidad = False
        print(f"La mascota {self.nombre} ha sido adoptada.")

    def verificarInformacionMascota(self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Tipo: {self.tipo}, Edad: {self.edad}, Disponibilidad: {'Sí' if self.disponibilidad else 'No'}"

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Tipo: {self.tipo}, Edad: {self.edad}, Disponibilidad: {'Sí' if self.disponibilidad else 'No'}"

    def __eq__(self, other):
        if not isinstance(other, Mascota):
            raise TypeError("La comparación solo es válida entre instancias de Mascota.")
        return self.id == other.id and self.nombre == other.nombre and self.tipo == other.tipo

    def __del__(self):
        Mascota.ids_usados.remove(self.id)
        print(f"El objeto {self.nombre} ha sido eliminado y su ID {self.id} ha sido liberado.")

if __name__ == "__main__": # Para verificar Mascota
     
    mascota1 = Mascota("Firulais", 1, "Perro", 3)
    mascota2 = Mascota("Miau", 2, "Gato", 2)
    mascota3 = Mascota("Tortuga", 3, "Tortuga", 5)

    print(mascota1)
    print(mascota2)
    print(mascota3)

    print(mascota1 == mascota2)  # False
    print(mascota1 == mascota1)  # True
    print(mascota1 == mascota3)  # False

    mascota1.adoptarMascota()
    print(mascota1.verificarInformacionMascota())

    del mascota1  # Esto eliminará el objeto y liberará su ID
    print(Mascota.ids_usados) 

    del mascota2  # Esto eliminará el objeto y liberará su ID
    print(Mascota.ids_usados)

    del mascota3  # Esto eliminará el objeto y liberará su ID
    print(Mascota.ids_usados)

    print(Mascota.TIPOS)  # ["Perro", "Gato", "Tortuga"]