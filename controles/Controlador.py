from interfaces import InterfaceSensor
from interfaces import InterfaceBateria
from interfaces import InterfaceLuz
from interfaces import InterfacePressao
from interfaces import InterfaceRotacao
from atuadores import AtuadorPrincipal

class Controlador:
    def __init__(self):
        self.luminosidade = 0.0
        self.interfBateria = InterfaceBateria()
        self.interSensor = InterfaceSensor()
        self.atuador = AtuadorPrincipal()

    def setLuminosidade(self):
        self.luminosidade = interSensor.getLuminosidade()

    def fecharMao(self):
        if self.luminosidade < 10: #exemplo
            self.atuador.fecharMao()
