from entidade import Bateria
from controle import Controlador

class InterfaceBateria:
    def __init__(self):
        self.bateria = Bateria();
        self.controlador = Controlador()
        self.nivelBateria = 0.0

    def setNivelBateria(self):
        valor = 0.0
        #calcula o nivel de bateria:
            #if ...
            #...
            #valor = floatNivelBateria
        self.nivelBateria = valor

    def getNivelBateria(self):
        self.setNivelBateria()
        return self.nivelBateria
