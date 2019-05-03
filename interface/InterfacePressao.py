from entidade import SensorLuz

class InterfaceLuz:
    def __init__(self):
        self.sensorLuz = SensorLuz()

    def getSensor(self):
        return self.sensorLuz
