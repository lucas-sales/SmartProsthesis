from controle import Controlador
from interface import *

class InterfaceSensor:
    def __init__(self):
        self.interfSensorLuz = InterfaceLuz()
        self.interfBateria = InterfaceBateria()
        self.controlador = Controlador()
        self.luminosidade = 0.0

    def setLuminosidade(self):
        self.luminosidade = self.interfSensorLuz.getLuminosidade()

    def getLuminosidade(self):
        while True:
            #verificando a luminosidade
            setLuminosidade()
        return self.luminosidade

    def verificarNiveBateria(self):
        #while True:
            #verificando a bateria
            self.interfBateria.getNivelBateria()
