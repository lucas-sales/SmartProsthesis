from controle import Controlador
from interface import *

class InterfaceSensor:
    def __init__(self):
        self.interfSensorLuz = InterfaceLuz()
        self.interfBateria = InterfaceBateria()
        self.interfSensorPressao = InterfacePressao()
        self.controlador = Controlador()
        self.luminosidade = 0.0
        self.abrir = False

    def setLuminosidade(self):
        self.luminosidade = self.interfSensorLuz.getLuminosidade()

    def getLuminosidade(self):
        while True:
            #verificando a luminosidade
            self.setLuminosidade()
            return self.luminosidade

    def verificarNivelBateria(self):
        while True:
            #verificando a bateria
            self.interfBateria.getNivelBateria()
            self.controlador.ativarLed()

    def abrirMao(self):
        while True:
            #verificando variavel self.abrir
            self.interfSensorPressao.getPressao()
            self.controlador.abrirMao()
