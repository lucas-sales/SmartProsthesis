from entidade import Dedo

class Mao:
    def __init__(self):
        self.listaDedos = []

    def getDedos(self):
        for i in range(4):#5 dedos da mao
            dedo = Dedo()
            self.listaDedos.append(dedo)
        return self.listaDedos

    def setDedos(self, dedos):
        self.listaDedos = dedos
