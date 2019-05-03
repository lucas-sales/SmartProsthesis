from entidade import Bateria
from controles import Controlador

class InterfaceBateria:
    def __init__(self):
        self.bateria = Bateria();
        self.controlador = Controlador()
        self.nivelBateria = 0.0

    def setNivelBateria(self):
        valor = 0.0
        #calcula o nivel de bateria:
            #...
            #...
            #valor = floatNivelBateria
        self.nivelBateria = valor

    def getNivelBateria(self):
        setNivelBateria()
        return self.nivelBateria
