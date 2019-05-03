class Bateria:
    def __init__(self):
        self.tensao
        self.corrente
        self.nivel

    def getTensao(self):
        return self.tensao
    def setTensao(self, tensao):
        self.tensao = tensao

    def getCorrente(self):
        return self.corrente
    def setCorrente(self, corrente):
        self.corrente = corrente

    def getNivel(self):
        return self.nivel
    def setNivel(self, nivel):
        self.nivel = nivel
