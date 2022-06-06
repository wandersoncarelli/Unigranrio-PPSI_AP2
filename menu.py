from clientes import Clientes
from motocicletas import Motocicletas
from vendas import Vendas
from dados import BancoDados


# Construindo a classe Menu
class Menu:

    def __init__(self):
        BancoDados().__init__()

    # Construindo o menu de clientes
    def menu_clientes(self):
        print('''   MENU CLIENTES:

        [1] - Cadastrar cliente
        [2] - Consultar cadastro
        [3] - Procurar cadastro por nome
        [4] - Atualizar cadastro
        [5] - Apagar cadastro
        [0] - Voltar ao menu principal
        ''')

        while True:
            cliente_opcao = int(input('Digite a opção escolhida: '))
            if cliente_opcao < 0 or cliente_opcao > 5:
                print('Opção inválida.')
            else:
                print()
                if cliente_opcao == 0:
                    break
                elif cliente_opcao == 1:
                    Clientes().cadastrar()
                    return self.menu_clientes()
                elif cliente_opcao == 2:
                    Clientes().consultar()
                    return self.menu_clientes()
                elif cliente_opcao == 3:
                    Clientes().procurar()
                    return self.menu_clientes()
                elif cliente_opcao == 4:
                    Clientes().atualizar()
                    return self.menu_clientes()
                elif cliente_opcao == 5:
                    Clientes().apagar()
                    return self.menu_clientes()
            print()

    # Construindo o menu de motocicletas
    def menu_motocicletas(self):
        print('''   MENU MOTOCICLETAS:

        [1] - Cadastrar motocicleta
        [2] - Consultar cadastro
        [3] - Procurar cadastro por marca
        [4] - Atualizar cadastro
        [5] - Apagar cadastro
        [0] - Voltar ao menu principal
        ''')

        while True:
            motocicleta_opcao = int(input('Digite a opção escolhida: '))
            if motocicleta_opcao < 0 or motocicleta_opcao > 5:
                print('Opção inválida.')
            else:
                print()
                if motocicleta_opcao == 0:
                    break
                elif motocicleta_opcao == 1:
                    Motocicletas().cadastrar()
                    return self.menu_motocicletas()
                elif motocicleta_opcao == 2:
                    Motocicletas().consultar()
                    return self.menu_motocicletas()
                elif motocicleta_opcao == 3:
                    Motocicletas().procurar()
                    return self.menu_motocicletas()
                elif motocicleta_opcao == 4:
                    Motocicletas().atualizar()
                    return self.menu_motocicletas()
                elif motocicleta_opcao == 5:
                    Motocicletas().apagar()
                    return self.menu_motocicletas()
            print()

    # Construindo o menu de vendas
    def menu_vendas(self):
        print('''   MENU VENDAS:

        [1] - Efetuar venda
        [2] - Consultar todas as vendas
        [3] - Procurar venda por cliente/marca
        [4] - Apagar venda
        [0] - Voltar ao menu principal
        ''')

        while True:
            venda_opcao = int(input('Digite a opção escolhida: '))
            print()
            if venda_opcao < 0 or venda_opcao > 4:
                print('Opção inválida.')
            else:
                if venda_opcao == 0:
                    break
                elif venda_opcao == 1:
                    Vendas().cadastrar()
                    return self.menu_vendas()
                elif venda_opcao == 2:
                    Vendas().consultar()
                    return self.menu_vendas()
                elif venda_opcao == 3:
                    Vendas().procurar()
                    return self.menu_vendas()
                elif venda_opcao == 4:
                    Vendas().apagar()
                    return self.menu_vendas()


# Função para desconectar o banco de dados
def desconectar_bd():
    BancoDados().desconectar()
