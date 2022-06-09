from Model.Card import Card
from Model.CardDAO import CardDAO


class CardController:

    def __init__(self):
        self.cDAO = CardDAO()
        self.card = None

    def cadastrar(self, id, descricao, nome, forca, magia, fogo):
        card = Card(id, descricao, nome, forca, magia, fogo)

        consulta = self.consultar(id)
        if (consulta == None):
            return self.cDAO.cadastrar(card)
        return False

    def atualizar(self, id, forca, magia, fogo):
        if not self.card.getId() == int(id):
            return False
        self.card.setForca(int(forca))
        self.card.setMagia(int(magia))
        self.card.setFogo(int(fogo))
        return self.cDAO.atualizar(self.card)

    def consultar(self, id):
        self.card = self.cDAO.consultar(id)

        if self.card != None:
            dados = [str(self.card.getId()),
                     self.card.getDescricao(),
                     str(self.card.getNome()),
                     str(self.card.getForca()),
                     str(self.card.getMagia()),
                     str(self.card.getFogo())]
            return dados
        return None

    def excluir(self, id):
        consulta = self.consultar(id)

        if consulta == None:
            return False
        return self.cDAO.excluir(int(id))
