import sqlite3


# Construindo a classe do banco de dados
class BancoDados:

    # Conectando o banco de dados ao iniciar a classe
    def __init__(self):
        self.connect = sqlite3.connect('database.db')
        self.cursor = self.connect.cursor()

    # Desconectando o banco de dados
    def desconectar(self):
        self.connect.close()