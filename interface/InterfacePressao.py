from entidade import SensorPressao

class InterfacePressao:
    def __init__(self):
        self.sensorPressao = SensorPressao()
        self.abrir = False

    def getPressao(self):
        self.setPressao()
        return self.sensorPressao

    def setPressao(self):
        #Verifica se o sensor foi pressionado duas vezes
        #if ...
        #...
        #...
        self.abrir = True
