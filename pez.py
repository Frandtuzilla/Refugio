from mascota import *

class Pez(Mascota):
    agua=["Agua dulce", "Agua salada"]
    def __init__(self, nombre: str, id:int, tipo:str, edad:int, disponibilidad:bool, agua:str):
        super().__init__(nombre, id, tipo, edad, disponibilidad)
        if agua in Pez.agua:
            self.agua=agua
        else: 
            raise ValueError("El valor ingresado no es válido")

    def getAgua(self):
        return self.agua
    
    def setAgua_dulce(self, nuevo_estado):
        if nuevo_estado not in Pez.agua:
            raise ValueError("El valor ingresado no es válido")
        else:
            self.agua=nuevo_estado

    def saludar(self):
        print('Dio dos vueltas')
# Prueba del código

pez1=Pez("Nemo", 1234, "Pez", 12, True, "Agua dulce")
pez1.saludar("dar 2 vueltas")
