from mascota import *

class Gato(Mascota):
    rasgos_gatos = ['sociable', 'solitario']
    def __init__(self, nombre:str, id:int, tipo:str, edad:int, disponibilidad:bool, rasgo:str):
        if not Gato.ValidacionRasgo(rasgo):
            raise ValueError (f'El rasgo {rasgo} no esta permitido')
        super().__init__(nombre, id, tipo, edad, disponibilidad)
        self.rasgo = rasgo 
        
    def getRasgo(self):
        return self.rasgo
    def setAgua(self, rasgo_nuevo):
        self.rasgo = rasgo_nuevo
        
    @staticmethod
    def ValidacionRasgo(rasgo):
        return rasgo in Gato.rasgos_gatos

if __name__=="__main__":

    Tago = Gato('Tago', 5, 'Perro', 8, True, 'sociable')
    print(Tago)
    Tago.saludar('Miau')