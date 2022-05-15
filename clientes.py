# Classe e funções para realizar as iterações com o menu de clientes

# Construindo a classe clientes

class Clientes:
    clientes = []  # Lista para armazenar os cadastros dos clientes

    # Cadastrando os clientes
    def cadastrar(self):
        cadastro = {}  # Dicionário para fazer o cadastro dos clientes
        opcao_cadastrar = ''  # Variável que irá interromper o loop de cadastro

        while opcao_cadastrar != 'N':
            # Definindo o ID de cada cliente
            if len(self.clientes) > 0:  # Se a quantidade se cadastros existentes for maior que zero
                cadastro['ID'] = self.clientes[-1]['ID'] + 1  # Vai buscar número do último ID e adicionar 1
            else:
                cadastro['ID'] = 1  # Se não existir cadastros, vai atribuir o ID 1
            cadastro['Nome'] = input('Nome completo: ')
            cadastro['Idade'] = int(input('Idade: '))
            cadastro['Sexo'] = input('Sexo: ')
            cadastro['Endereço'] = input('Endereço: ')
            cadastro['Cidade'] = input('Cidade: ')
            cadastro['UF'] = input('UF: ')
            cadastro['Telefone'] = int(input('Telefone: '))
            cadastro['Email'] = input('E-mail: ')
            self.clientes.append(cadastro)  # Adiciona os dados de cadastro na lista
            cadastro = {}  # Apaga os dados atuais, necessário para não duplicar os cadastros na lista
            print('\nCliente cadastrado com sucesso!')
            while opcao_cadastrar != 'N' or opcao_cadastrar != 'S':
                # Colocar .upper() no final do input converte a resposta para letras maiúsculas
                opcao_cadastrar = input('Deseja cadastrar outro cliente? (S/N): ').upper()
                print()
                if opcao_cadastrar == 'N' or opcao_cadastrar == 'S':
                    break
                else:
                    print('Opção inválida.\n')

    # Mostrando tabela de clientes cadastrados
    def mostrar_clientes(self):
        print(40 * "=")
        print(f'{"TABELA DE CLIENTES":^40}')
        print(40 * "=")
        print(f'{"ID":<5}{"NOME":<30}{"IDADE":>5}')
        print(40 * "-")

        # Imprimindo a lista de clientes em formato de tabela
        for i in range(0, len(self.clientes)):
            print(f'{self.clientes[i]["ID"]:<5}{self.clientes[i]["Nome"]:<30}{self.clientes[i]["Idade"]:>5}')
        print(40 * "-")
        print()

    # Consultando os clientes cadastrados
    def consultar(self):
        opcao_consultar = ''  # Variável que irá interromper o loop de consulta
        self.mostrar_clientes()  # Mostra a lista de clientes cadastrados

        while opcao_consultar != 'N':
            detalhes = int(input('Digite o ID correspondente ao cliente (0 para cancelar): '))
            print()

            if detalhes == 0:
                print('Operação cancelada.\n')
                opcao_consultar = 'N'
            else:
                for k, v in self.clientes[detalhes - 1].items():
                    print(k + ':', str(v))
                print()

                while opcao_consultar != 'N' or opcao_consultar != 'S':
                    opcao_consultar = input('Deseja consultar outro cliente? (S/N): ').upper()
                    if opcao_consultar == 'N' or opcao_consultar == 'S':
                        print()
                        break
                    else:
                        print('Opção inválida.\n')

    # Atualizando o cadastro de clientes
    def atualizar(self):
        id_atualizar = -1
        self.mostrar_clientes()  # Mostra a lista de clientes cadastrados

        while 0 > id_atualizar < len(self.clientes):
            id_atualizar = int(input('Digite o ID do cliente para atualizar seu cadastro (0 para cancelar): '))
            if id_atualizar < 0 or id_atualizar > len(self.clientes):
                print('Opção inválida.\n')
        if id_atualizar == 0:
            print('Operação cancelada.\n')
        else:
            id_atualizar -= 1
            print()
            cont = 'X'
            print('Dados do cliente selecionado:')
            for k, v in self.clientes[id_atualizar].items():
                print(f'[{cont}]', k + ':', str(v))
                if cont == 'X':
                    cont = 0
                cont += 1
            print('[0] CANCELAR')
            print()

            while True:
                opcao_atualizar = int(input('Digite o número da opção para atualizar o cadastro: '))
                if opcao_atualizar < 0 or opcao_atualizar > 8:
                    print('Opção inválida.\n')
                else:
                    break
            if opcao_atualizar == 1:
                self.clientes[id_atualizar]['Nome'] = input('Digite o nome: ')
            elif opcao_atualizar == 2:
                self.clientes[id_atualizar]['Idade'] = input('Digite a idade: ')
            elif opcao_atualizar == 3:
                self.clientes[id_atualizar]['Sexo'] = input('Digite o sexo: ')
            elif opcao_atualizar == 4:
                self.clientes[id_atualizar]['Endereço'] = input('Digite o endereço: ')
            elif opcao_atualizar == 5:
                self.clientes[id_atualizar]['Cidade'] = input('Digite a cidade: ')
            elif opcao_atualizar == 6:
                self.clientes[id_atualizar]['UF'] = input('Digite a UF: ')
            elif opcao_atualizar == 7:
                self.clientes[id_atualizar]['Telefone'] = input('Digite o telefone: ')
            elif opcao_atualizar == 8:
                self.clientes[id_atualizar]['Email'] = input('Digite o email: ')

            if opcao_atualizar == 0:
                print('Operação cancelada.\n')
            else:
                print('Cadastro atualizado com sucesso.\n')

    # Apagando o cadastro de clientes
    def apagar(self):
        id_apagar = -1
        self.mostrar_clientes()

        while id_apagar < 0 or id_apagar > len(self.clientes):
            id_apagar = int(input('Digite o ID do cliente para apagar seu cadastro (0 para cancelar): '))
            if id_apagar < 0 or id_apagar > len(self.clientes):
                print('Opção inválida.\n')
            else:
                if id_apagar == 0:
                    print('Operação cancelada.\n')
                else:
                    id_apagar -= 1
                    self.clientes.remove(self.clientes[id_apagar])
                    print('Cadastro apagado com sucesso.\n')
