from interface import InterfaceSensor
from interface import InterfaceBateria
from interface import InterfaceLuz
from interface import InterfacePressao
from interface import InterfaceRotacao
from atuador import AtuadorPrincipal

class Controlador:
    def __init__(self):
        self.luminosidade = 0.0
        self.nivelBateria = 0.0
        self.interfBateria = InterfaceBateria()
        self.interSensor = InterfaceSensor()
        self.atuador = AtuadorPrincipal()

    def setLuminosidade(self):
        self.luminosidade = interSensor.getLuminosidade()
        fecharMao()

    def fecharMao(self):
        if self.luminosidade < 10: #exemplo
            self.atuador.fecharMao()

    def setNivelBateria(self):
        self.nivelBateria = self.interfSensor.verificarNiveBateria()

    def ativarLed(self):
        if self.nivelBateria < 10: #exemplo
            self.atuador.ativarLedVermelho()
        elif self.nivelBateria > 10 and self.nivelBateria <= 30:
            self.atuador.ativarLedLaranja()
