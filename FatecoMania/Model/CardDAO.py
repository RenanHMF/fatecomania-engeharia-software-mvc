import mysql.connector

from Model.Card import Card

class CardDAO:
    def __init__(self):
        self.con = None
        self.cursor = None

    def conectar(self):
        self.con = mysql.connector.connect(host='localhost',
                                           database='CardDB', user='root', password='')
        if not self.con.is_connected():
            return False
        self.cursor = self.con.cursor()
        return True

    def desconectar(self):
        if self.con.is_connected():
            self.con.close()

    def cadastrar(self, card):
        sql = 'insert into Card values (%s,%s,%s,%s,%s,%s)'
        valores = (card.getId(), card.getDescricao(),
                   card.getNome(), card.getForca(), card.getMagia(),
                   card.getFogo())
        if not self.conectar():
            return False
        self.cursor.execute(sql, valores)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False

    def consultar(self, id):
        sql = 'select * from Card where id=' + str(id)
        if not self.conectar():
            return False
        self.cursor.execute(sql)
        for (id, descricao, nome, forca, magia, fogo) in self.cursor:
            c = Card(id, descricao, nome, forca, magia, fogo)
            return c
        return None

    def atualizar(self, c):
        sql = 'update Card set forca=%s, magia=%s, fogo=%s where id=%s'
        valores = (c.getForca(), c.getMagia(), c.getFogo(), c.getId())
        if not self.conectar():
            return False
        self.cursor.execute(sql, valores)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False

    def excluir(self, id):
        sql = 'delete from Card where id=' + str(id)
        if not self.conectar():
            return False
        self.cursor.execute(sql)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False
