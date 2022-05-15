from clientes import Clientes
from motocicletas import Motocicletas
from vendas import Vendas


# Construindo a classe Menu
class Menu:

    # Construindo o menu de clientes
    def menu_clientes(self):
        print('''   MENU CLIENTES:

        [1] - Cadastrar cliente
        [2] - Consultar cliente
        [3] - Atualizar cliente
        [4] - Apagar cliente
        [0] - Voltar ao menu anterior
        ''')

        while True:
            cliente_opcao = int(input('Digite a opção escolhida: '))
            if cliente_opcao < 0 or cliente_opcao > 4:
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
                    Clientes().atualizar()
                    return self.menu_clientes()
                elif cliente_opcao == 4:
                    Clientes().apagar()
                    return self.menu_clientes()
            print()

    # Construindo o menu de motocicletas
    def menu_motocicletas(self):
        print('''   MENU MOTOCICLETAS:

        [1] - Cadastrar motocicleta
        [2] - Consultar motocicleta
        [3] - Atualizar motocicleta
        [4] - Apagar motocicleta
        [0] - Voltar ao menu anterior
        ''')

        while True:
            motocicleta_opcao = int(input('Digite a opção escolhida: '))
            if motocicleta_opcao < 0 or motocicleta_opcao > 4:
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
                    Motocicletas().atualizar()
                    return self.menu_motocicletas()
                elif motocicleta_opcao == 4:
                    Motocicletas().apagar()
                    return self.menu_motocicletas()
            print()

    # Construindo o menu de vendas
    def menu_vendas(self):
        print('''   MENU VENDAS:

        [1] - Cadastrar venda
        [2] - Consultar vendas
        [3] - Atualizar venda
        [4] - Apagar venda
        [0] - Voltar ao menu anterior
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
                    Vendas().atualizar()
                    return self.menu_vendas()
                elif venda_opcao == 4:
                    Vendas().apagar()
                    return self.menu_vendas()
