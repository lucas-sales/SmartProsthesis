from entidade import Motor

class Dedo:
    def __init__(self):
        self.listaMotor = []

    def getMotores(self):
        for i in range(2): #cada dedo tem 3 articulacoes
            motor = Motor()
            self.listaMotor.append(motor)
        return self.listaMotor

    def setMotores(self, motores):
       self.listaMotor = motores
