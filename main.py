from clientes import Clientes


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
            print('Menu ainda não construido.')
            # self.menu_moto()
        elif self.menu_opcao == 3:
            print('Menu ainda não construido.')
            # self.menu_vendas()

    # Construção do menu de clientes
    def menu_cliente(self):
        self.menu_opcao = -1
        cliente_opcao = -1
        print('''MENU CLIENTES:

    [1] - Cadastrar cliente
    [2] - Consultar cadastro
    [3] - Atualizar cadastro
    [4] - Apagar cadastro
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
    def menu_moto(self):
        pass

    # Construção do menu de vendas (ainda não iniciado)
    def menu_vendas(self):
        pass


Application()
