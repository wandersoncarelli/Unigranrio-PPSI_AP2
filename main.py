from menu import Menu  # Importando a classe Menu, criada no arquivo 'menu.py'


# Construindo a classe do programa
class Application:

    # Construtor da classe
    def __init__(self):
        self.menu_opcao = -1  # Variáveis definida para interromper o loop do menu principal
        self.main_menu()  # Inicia o menu principal

    # Construção do menu principal
    def main_menu(self):
        print('''MENU PRINCIPAL:

    [1] - Clientes
    [2] - Motocicletas
    [3] - Vendas
    [0] - Sair do programa
    ''')

        while True:
            self.menu_opcao = int(input('Digite a opção escolhida: '))  # Solicita a opção do menu
            print()
            if self.menu_opcao < 0 or self.menu_opcao > 3:  # Valida a resposta
                print('Opção inválida.\n')  # Mensagem de erro, caso digite uma opção que não exista
            else:
                if self.menu_opcao == 0:
                    print('Você saiu do programa.')
                    exit()  # Encerra a reprodução do código
                elif self.menu_opcao == 1:
                    Menu.menu_clientes(Menu())  # Chama o menu de clientes
                    self.menu_opcao = -1  # Usado para impedir o loop do menu de clientes
                    return self.main_menu()  # Retorna para o menu principal
                elif self.menu_opcao == 2:
                    Menu.menu_motocicletas(Menu())  # Chama o menu de motocicletas
                    self.menu_opcao = -1  # Usado para impedir o loop do menu de motocicletas
                    return self.main_menu()  # Retorna para o menu principal
                elif self.menu_opcao == 3:
                    Menu.menu_vendas(Menu())  # Chama o menu de vendas
                    self.menu_opcao = -1  # Usado para impedir o loop do menu de vendas
                    return self.main_menu()  # Retorna para o menu principal


if __name__ == '__main__':  # Usado para verificar se o arquivo atual é o principal (main.py)
    Application()  # Inicia o programa
