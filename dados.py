import sqlite3


# Construindo a classe do banco de dados
class BancoDados:

    # Conectando o banco de dados ao iniciar a classe
    def __init__(self):
        self.connect = sqlite3.connect('database.db')
        self.cursor = self.connect.cursor()
        self.tb_clientes()
        self.tb_motocicletas()
        self.tb_vendas()

    # Desconectando o banco de dados
    def desconectar(self):
        self.connect.close()

    # Criando a tabela de clientes, se não existir
    def tb_clientes(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome CHAR(40) NOT NULL,
        idade INTEGER(2) NOT NULL,
        sexo CHAR(10) NOT NULL,
        endereço CHAR(40) NOT NULL,
        cidade CHAR(30) NOT NULL,
        uf CHAR(2) NOT NULL,
        telefone INTEGER(11) NOT NULL,
        email CHAR(30) NOT NULL)""")

    # Criando a tabela de motocicletas, se não existir
    def tb_motocicletas(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS motocicletas (
        id INTEGER PRIMARY KEY,
        marca CHAR(30) NOT NULL,
        modelo CHAR(30) NOT NULL,
        ano INTEGER(4) NOT NULL,
        cilindrada INTEGER(5) NOT NULL,
        preco INTEGER(10) NOT NULL,
        id_dono INTEGER(5) NOT NULL,
        nome_dono CHAR(40) NOT NULL)""")

    # Criando a tabela de vendas, se não existir
    def tb_vendas(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY,
        id_cliente INTEGER(5) NOT NULL,
        nome_cliente CHAR(40) NOT NULL,
        id_motocicleta INTEGER(5) NOT NULL,
        marca_motocicleta CHAR(30) NOT NULL,
        modelo_motocicleta CHAR(30) NOT NULL,
        ano_motocicleta INTEGER(4) NOT NULL,
        preco_motocicleta INTEGER(10) NOT NULL)""")
