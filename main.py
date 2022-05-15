from clientes import Clientes
from motocicletas import Motocicletas
from vendas import Vendas


class Application:
    # Construtor da classe
    def __init__(self):
        # Variáveis para validar as repostas das opções dos menus
        self.menu_opcao = -1
        self.main_menu()  # Inicia o menu principal

    # Construção do menu principal
    def main_menu(self):
        print('''MENU PRINCIPAL:

    [1] - Clientes
    [2] - Motocicletas
    [3] - Vendas
    [0] - Sair do programa
    ''')

        while self.menu_opcao < 0 or self.menu_opcao > 3:  # Enquanto a resposta não estiver nas opções
            self.menu_opcao = int(input('Digite a opção escolhida: '))  # Vai solicitar a resposta
            print()
            if self.menu_opcao < 0 or self.menu_opcao > 3:  # Valida a resposta
                print('Opção inválida.\n')  # Mensagem de erro

        if self.menu_opcao == 0:
            print('Você saiu do programa.')
            exit()
        elif self.menu_opcao == 1:
            self.menu_cliente()
        elif self.menu_opcao == 2:
            self.menu_motocicleta()
        elif self.menu_opcao == 3:
            self.menu_vendas()

    # Construção do menu de clientes
    def menu_cliente(self):
        self.menu_opcao = -1
        cliente_opcao = -1
        print('''MENU CLIENTES:

    [1] - Cadastrar cliente
    [2] - Consultar cliente
    [3] - Atualizar cliente
    [4] - Apagar cliente
    [0] - Voltar ao menu anterior
            ''')
        while cliente_opcao < 0 or cliente_opcao > 4:
            cliente_opcao = int(input('Digite a opção escolhida: '))
            print()
            if cliente_opcao < 0 or cliente_opcao > 4:
                print('Opção inválida.')
        if cliente_opcao == 0:
            self.main_menu()
        elif cliente_opcao == 1:
            Clientes().cadastrar()
            self.menu_cliente()
        elif cliente_opcao == 2:
            if len(Clientes().clientes) == 0:
                print('Não existem clientes cadastrados.\n')
            else:
                Clientes().consultar()
            self.menu_cliente()
        elif cliente_opcao == 3:
            if len(Clientes().clientes) == 0:
                print('Não existem clientes cadastrados.\n')
            else:
                Clientes().atualizar()
            self.menu_cliente()
        elif cliente_opcao == 4:
            if len(Clientes().clientes) == 0:
                print('Não existem clientes cadastrados.\n')
            else:
                Clientes().apagar()
            self.menu_cliente()

    # Construção do menu de motocicletas (ainda não iniciado)
    def menu_motocicleta(self):
        self.menu_opcao = -1
        motocicleta_opcao = -1
        print('''MENU MOTOCICLETAS:

    [1] - Cadastrar motocicleta
    [2] - Consultar motocicleta
    [3] - Atualizar motocicleta
    [4] - Apagar motocicleta
    [0] - Voltar ao menu anterior
    ''')

        while motocicleta_opcao < 0 or motocicleta_opcao > 4:
            motocicleta_opcao = int(input('Digite a opção escolhida: '))
            print()
            if motocicleta_opcao < 0 or motocicleta_opcao > 4:
                print('Opção inválida.')
        if motocicleta_opcao == 0:
            self.main_menu()
        elif motocicleta_opcao == 1:
            Motocicletas().cadastrar()
            self.menu_motocicleta()
        elif motocicleta_opcao == 2:
            Motocicletas().consultar()
            self.menu_motocicleta()
        elif motocicleta_opcao == 3:
            if len(Motocicletas().motocicletas) == 0:
                print('Não existem motocicletas cadastradas.\n')
            else:
                Motocicletas().atualizar()
            self.menu_motocicleta()
        elif motocicleta_opcao == 4:
            if len(Motocicletas().motocicletas) == 0:
                print('Não existem motocicletas cadastradas.\n')
            else:
                Motocicletas().apagar()
            self.menu_motocicleta()

    # Construção do menu de vendas (ainda não iniciado)
    def menu_vendas(self):
        self.menu_opcao = -1
        venda_opcao = -1
        print('''MENU VENDAS:

        [1] - Cadastrar venda
        [2] - Consultar vendas
        [3] - Atualizar venda
        [4] - Apagar venda
        [0] - Voltar ao menu anterior
        ''')

        while venda_opcao < 0 or venda_opcao > 4:
            venda_opcao = int(input('Digite a opção escolhida: '))
            print()
            if venda_opcao < 0 or venda_opcao > 4:
                print('Opção inválida.')
        if venda_opcao == 0:
            self.main_menu()
        elif venda_opcao == 1:
            Vendas().cadastrar()
            self.menu_vendas()
        elif venda_opcao == 2:
            if len(Vendas().vendas) == 0:
                print('Não existem vendas cadastradas.\n')
            else:
                Vendas().consultar()
            self.menu_vendas()
        elif venda_opcao == 3:
            if len(Vendas().vendas) == 0:
                print('Não existem vendas cadastradas.\n')
            else:
                Vendas().atualizar()
            self.menu_vendas()
        elif venda_opcao == 4:
            if len(Vendas().vendas) == 0:
                print('Não existem vendas cadastradas.\n')
            else:
                Vendas().apagar()
            self.menu_vendas()


Application()
