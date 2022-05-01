from clientes import Clientes


class Menu:
    def __init__(self):
        self.menu_opcao = self.cliente_opcao = -1
        self.main_menu()

    def main_menu(self):
        print('''MENU PRINCIPAL:
    
    [1] - Clientes
    [2] - Motocicletas
    [3] - Vendas
    [0] - Sair
                ''')
        while self.menu_opcao < 0 or self.menu_opcao > 3:
            self.menu_opcao = int(input('Digite a opção escolhida: '))
            if self.menu_opcao < 0 or self.menu_opcao > 3:
                print('Opção inválida.\n')
        if self.menu_opcao == 0:
            print('Você saiu do programa.')
            exit()
        elif self.menu_opcao == 1:
            self.menu_cliente()
        # elif self.menu_opcao == 2:
        #     self.menu_moto()
        # elif self.menu_opcao == 3:
        #     self.menu_vendas()

    def menu_cliente(self):
        self.menu_opcao = self.cliente_opcao = -1
        print('''
MENU CLIENTES:

    [1] - Cadastrar cliente
    [2] - Consultar cadastro
    [3] - Atualizar cadastro
    [4] - Apagar cadastro
    [0] - Voltar ao menu anterior
            ''')
        while self.cliente_opcao < 0 or self.cliente_opcao > 4:
            self.cliente_opcao = int(input('Digite a opção escolhida: '))
            if self.cliente_opcao < 0 or self.cliente_opcao > 4:
                print('Opção inválida.')
        if self.cliente_opcao == 0:
            print()
            self.main_menu()
        elif self.cliente_opcao == 1:
            Clientes().cadastrar()
            self.menu_cliente()
        elif self.cliente_opcao == 2:
            if len(Clientes().clientes) > 0:
                Clientes().consultar()
            else:
                print('Não existem clientes cadastrados.')
            self.menu_cliente()
        elif self.cliente_opcao == 3:
            Clientes().atualizar()
        elif self.cliente_opcao == 4:
            Clientes().apagar()

    def menu_moto(self):
        pass

    def menu_vendas(self):
        pass
