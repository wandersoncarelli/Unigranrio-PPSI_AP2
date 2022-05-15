# Classe e funções para realizar as iterações com o menu de motocicletas

# Construindo a classe motocicletas
class Motocicletas:
    motocicletas = []

    def cadastrar(self):
        cadastro = {}  # Dicionário para fazer o cadastro dos clientes
        opcao_cadastrar = ''  # Variável que irá interromper o loop de cadastro

        while opcao_cadastrar != 'N':
            # Definindo o ID de cada motocicleta
            if len(self.motocicletas) > 0:  # Se a quantidade se cadastros existentes for maior que zero
                cadastro['ID'] = self.motocicletas[-1]['ID'] + 1  # Vai buscar número do último ID e adicionar 1
            else:
                cadastro['ID'] = 1  # Se não existir cadastros, vai atribuir o ID 1
            cadastro['Marca'] = input('Marca: ')
            cadastro['Modelo'] = input('Modelo: ')
            cadastro['Ano'] = int(input('Ano: '))
            cadastro['Cilindrada'] = int(input('Cilindradas: '))
            preco = float(input('Preço: R$'))
            cadastro['Preço'] = str(f'R${preco:,.2f}')
            self.motocicletas.append(cadastro)  # Adiciona os dados de cadastro na lista
            cadastro = {}  # Apaga os dados atuais, necessário para não duplicar os cadastros na lista
            print('\nMotocicleta cadastrada com sucesso!')

            while opcao_cadastrar != 'N' or opcao_cadastrar != 'S':
                # Colocar .upper() no final do input converte a resposta para letras maiúsculas
                opcao_cadastrar = input('Deseja cadastrar outra motocicleta? (S/N): ').upper()
                print()
                if opcao_cadastrar == 'N' or opcao_cadastrar == 'S':
                    break
                else:
                    print('Opção inválida.\n')

    def mostrar_motocicletas(self):
        print(54 * "=")
        print(f'{"TABELA DE MOTOCICLETAS":^54}')
        print(54 * "=")
        print(f'{"ID":<5}{"MARCA":<14}{"MODELO":<14}{"ANO":<6}{"PREÇO":>14}')
        print(54 * "-")

        # Imprimindo a lista de motocicletas em formato de tabela
        for i in range(0, len(self.motocicletas)):
            print(f'{self.motocicletas[i]["ID"]:<5}{self.motocicletas[i]["Marca"]:<14}'
                  f'{self.motocicletas[i]["Modelo"]:<14}{self.motocicletas[i]["Ano"]:<6}'
                  f'{self.motocicletas[i]["Preço"]:>14}')
        print(54 * "-")
        print()

    def consultar(self):
        opcao_consultar = ''  # Variável que irá interromper o loop de consulta
        self.mostrar_motocicletas()

        while opcao_consultar != 'N':
            detalhes = int(input('Digite o ID correspondente a motocicleta (0 para cancelar): '))
            print()

            if detalhes == 0:
                print('Operação cancelada.\n')
                opcao_consultar = 'N'
            else:
                for k, v in self.motocicletas[detalhes - 1].items():
                    print(k + ':', str(v))
                print()

                while opcao_consultar != 'N' or opcao_consultar != 'S':
                    opcao_consultar = input('Deseja consultar outra motocicleta? (S/N): ').upper()
                    if opcao_consultar == 'N' or opcao_consultar == 'S':
                        print()
                        break
                    else:
                        print('Opção inválida.\n')

    def atualizar(self):
        id_atualizar = -1
        self.mostrar_motocicletas()  # Mostra a lista de motocicletas cadastrados

        while 0 > id_atualizar < len(self.motocicletas):
            id_atualizar = int(input('Digite o ID da motocicleta para atualizar o cadastro (0 para cancelar): '))
            if id_atualizar < 0 or id_atualizar > len(self.motocicletas):
                print('Opção inválida.\n')
        if id_atualizar == 0:
            print('Operação cancelada.\n')
        else:
            id_atualizar -= 1
            print()
            cont = 'X'
            print('Dados da motocicleta selecionada:')
            for k, v in self.motocicletas[id_atualizar].items():
                print(f'[{cont}]', k + ':', str(v))
                if cont == 'X':
                    cont = 0
                cont += 1
            print('[0] CANCELAR')
            print()

            while True:
                opcao_atualizar = int(input('Digite o número da opção para atualizar o cadastro: '))
                if opcao_atualizar < 0 or opcao_atualizar > 6:
                    print('Opção inválida.\n')
                else:
                    break
            if opcao_atualizar == 1:
                self.motocicletas[id_atualizar]['Marca'] = input('Digite a marca: ')
            elif opcao_atualizar == 2:
                self.motocicletas[id_atualizar]['Modelo'] = input('Digite o modelo: ')
            elif opcao_atualizar == 3:
                self.motocicletas[id_atualizar]['Ano'] = int(input('Digite o ano: '))
            elif opcao_atualizar == 4:
                self.motocicletas[id_atualizar]['Cilindrada'] = int(input('Digite as cilindradas: '))
            elif opcao_atualizar == 5:
                preco = float(input('Digite o preço: R$'))
                self.motocicletas[id_atualizar]['Preço'] = str(f'R${preco:,.2f}')

            if opcao_atualizar == 0:
                print('Operação cancelada.\n')
            else:
                print('Cadastro atualizado com sucesso.\n')

    def apagar(self):
        id_apagar = -1
        self.mostrar_motocicletas()

        while id_apagar < 0 or id_apagar > len(self.motocicletas):
            id_apagar = int(input('Digite o ID da motocicleta para apagar o cadastro (0 para cancelar): '))
            if id_apagar < 0 or id_apagar > len(self.motocicletas):
                print('Opção inválida.\n')
            else:
                if id_apagar == 0:
                    print('Operação cancelada.\n')
                else:
                    id_apagar -= 1
                    self.motocicletas.remove(self.motocicletas[id_apagar])
                    print('Cadastro apagado com sucesso.\n')
