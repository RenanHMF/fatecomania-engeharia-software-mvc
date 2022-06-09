class Card:
    id = 0
    descricao = ''
    nome = ""
    forca = 0
    magia = 0
    fogo = 0

    def __init__(self, id, descricao, nome, forca, magia, fogo):
        self.id = id
        self.descricao = descricao
        self.nome = nome
        self.forca = forca
        self.magia = magia
        self.fogo = fogo

    def getId(self):
        return self.id

    def getDescricao(self):
        return self.descricao

    def getNome(self):
        return self.nome

    def getForca(self):
        return self.forca

    def getMagia(self):
        return self.magia

    def getFogo(self):
        return self.fogo


    def setForca(self, forca):
        self.forca = forca

    def setMagia(self, magia):
        self.magia = magia

    def setFogo(self, fogo):
        self.fogo = fogo