from mascota import *

class Perro(Mascota):
    def __init__(self, nombre:str, id:int, tipo:str, edad:int, disponibilidad:bool, lazarillo:bool):
        super().__init__(nombre, id, tipo, edad, disponibilidad)
        self.lazarillo = lazarillo
    
    def getLazarillo(self):
        return self.lazarillo
    def setAgua(self, lazarillo_nuevo):
        self.lazarillo = lazarillo_nuevo

if __name__=="__main__":
    #pruebo el codigo
    Coco = Perro('Coco', 5, 'Perro', 8, True, True)
    print(Coco)
    Coco.saludar('Guau')
