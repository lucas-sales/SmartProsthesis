from entidade import SensorLuz

class InterfaceLuz:
    def __init__(self):
        self.sensorLuz = SensorLuz()
        self.luminosidade = 0.0

    def getLuminosidade(self):
        setLuminosidade()
        return self.luminosidade

    def setLuminosidade(self):
        valor = 0.0
        #calcula a luminosidade:
            #if ...
            #...
            #valor = floatLuz
        self.luminosidade = valor
