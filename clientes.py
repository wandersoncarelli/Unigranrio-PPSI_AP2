class Clientes:
    clientes = []  # Lista para armazenar todos os cadastros dos clientes
    cadastro = {}  # Dicionário para fazer o cadastro dos clientes
    opcao = ''  # Variável que irá interromper o loop de cadastro

    # Cadastrando os clientes
    def cadastrar(self):
        while self.opcao != 'N':
            print()
            # Definindo o ID de cada cliente
            if len(self.clientes) > 0:  # Se a quantidade se cadastros existentes for maior que zero
                self.cadastro['ID'] = self.clientes[-1]['ID'] + 1  # Vai buscar número do último ID e adicionar 1
            else:
                self.cadastro['ID'] = 1  # Se não existir cadastros, vai atribuir o ID 1
            self.cadastro['Nome'] = input('Nome: ')
            self.cadastro['Idade'] = int(input('Idade: '))
            self.cadastro['Sexo'] = input('Sexo: ')
            self.cadastro['Endereço'] = input('Endereço: ')
            self.cadastro['Cidade'] = input('Cidade: ')
            self.cadastro['UF'] = input('UF: ')
            self.cadastro['Telefone'] = int(input('Telefone: '))
            self.cadastro['Email'] = input('E-mail: ')
            self.clientes.append(self.cadastro)  # Adiciona os dados de cadastro na lista
            self.cadastro = {}  # Apaga os dados atuais, necessário para não duplicar os cadastros na lista
            print('\nCliente cadastrado com sucesso!')
            while self.opcao != 'N' or self.opcao != 'S':
                # Colocar .upper() no final do input converte a resposta para letras maiúsculas
                self.opcao = input('Deseja cadastrar outro cliente? (S/N): ').upper()
                if self.opcao == 'N' or self.opcao == 'S':
                    break
                else:
                    print('Opção inválida.')

    # Consultando os clientes cadastrados
    def consultar(self):
        opcao_consultar = ''
        print()
        print(40 * "=")
        print(f'{"TABELA DE CLIENTES":^40}')
        print(40 * "=")
        print(f'{"ID":<5}{"NOME":<30}{"IDADE":>5}')
        print(40 * "-")

        for i in range(0, len(self.clientes)):
            print(
                f'{self.clientes[i]["ID"]:<5}{self.clientes[i]["Nome"]:<30}{self.clientes[i]["Idade"]:>5}')
        print()

        while opcao_consultar != 'N':
            detalhes = int(input('Digite o ID correspondente ao cliente (0 para sair): '))
            print()

            if detalhes == 0:
                opcao_consultar = 'N'
            else:
                for k, v in self.clientes[detalhes - 1].items():
                    print(k + ':', str(v))
                print()
                while opcao_consultar != 'N' or opcao_consultar != 'S':
                    opcao_consultar = input('Deseja consultar outro cliente? (S/N): ').upper()
                    if opcao_consultar == 'N' or opcao_consultar == 'S':
                        break
                    else:
                        print('Opção inválida.')

    # Atualizando o cadastro de clientes
    def atualizar(self):
        pass

    # Apagando o cadastro de clientes
    def apagar(self):
        pass
