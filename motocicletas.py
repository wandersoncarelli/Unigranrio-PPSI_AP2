# Classe e funções para realizar as iterações com o menu de motocicletas

# Construindo a classe motocicletas
class Motocicletas:
    motocicletas = []

    # Cadastrando clientes
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

    # Mostrando tabela de motocicletas cadastradas
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

    # Consultando detalhes das motocicletas cadastradas
    def consultar(self):
        if len(self.motocicletas) == 0:
            print('Não existe motocicletas cadastradas.\n')
        else:
            opcao_consultar = ''  # Variável que irá interromper o loop de consulta
            self.mostrar_motocicletas()  # Mostra a lista de motocicletas cadastradas

            while opcao_consultar != 'N':
                detalhes = int(input('Digite o ID correspondente a motocicleta (0 para cancelar): '))

                if detalhes == 0:
                    print('Operação cancelada.\n')
                    opcao_consultar = 'N'
                else:
                    for i in self.motocicletas:
                        if detalhes == i['ID']:
                            print()
                            print('Dados da motocicleta selecionada:\n')
                            for k, v in i.items():
                                print(k + ':', str(v))
                        else:
                            print('ID inválido.')
                    print()

                    while opcao_consultar != 'N' or opcao_consultar != 'S':
                        opcao_consultar = input('Deseja consultar outra motocicleta? (S/N): ').upper()
                        if opcao_consultar == 'N' or opcao_consultar == 'S':
                            print()
                            break
                        else:
                            print('Opção inválida.\n')

    # Atualizando cadastro de motocicletas
    def atualizar(self):
        if len(self.motocicletas) == 0:
            print('Não existe motocicletas cadastradas.\n')
        else:
            id_atualizar = ''  # Variável que irá interromper o loop de atualização
            self.mostrar_motocicletas()  # Mostra a lista de motocicletas cadastradas

            while id_atualizar != 0:
                id_atualizar = int(input('Digite o ID da motocicleta para atualizar seu cadastro (0 para cancelar): '))

                if id_atualizar == 0:
                    print('Operação cancelada.\n')
                    break
                else:
                    for i in self.motocicletas:
                        if id_atualizar == i['ID']:
                            cont = 'X'
                            print()
                            print('Dados da motocicleta selecionada:\n')
                            for k, v in i.items():
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
                                i['Marca'] = input('Digite a marca: ')
                            elif opcao_atualizar == 2:
                                i['Modelo'] = input('Digite o modelo: ')
                            elif opcao_atualizar == 3:
                                i['Ano'] = int(input('Digite o ano: '))
                            elif opcao_atualizar == 4:
                                i['Cilindrada'] = int(input('Digite as cilindradas: '))
                            elif opcao_atualizar == 5:
                                preco = float(input('Digite o preço: R$'))
                                i['Preço'] = str(f'R${preco:,.2f}')

                            if opcao_atualizar == 0:
                                print('Operação cancelada.')
                            else:
                                print('Cadastro atualizado com sucesso.')
                        else:
                            print('ID inválido.')
                    print()

    # Apagando o cadastro de motocicletas
    def apagar(self):
        if len(self.motocicletas) == 0:
            print('Não existe motocicletas cadastradas.\n')
        else:
            opcao_apagar = ''  # Variável que irá interromper o loop de apagar
            self.mostrar_motocicletas()  # Mostra a lista de motocicletas cadastradas

            while opcao_apagar != 'N':
                id_apagar = int(input('Digite o ID da motocicleta para apagar seu cadastro (0 para cancelar): '))

                if id_apagar == 0:
                    print('Operação cancelada.\n')
                    break
                else:
                    for i in self.motocicletas:
                        if id_apagar == i['ID']:
                            print()
                            print('Dados da motocicleta selecionada:\n')
                            for k, v in i.items():
                                print(k + ':', str(v))
                            print()

                            while True:
                                opcao_confirmar = input('Deseja apagar o cadastro selecionado? (S/N): ').upper()
                                if opcao_confirmar != 'S' and opcao_confirmar != 'N':
                                    print('Opção inválida.\n')
                                else:
                                    if opcao_confirmar == 'N' or opcao_confirmar == 'S':
                                        if opcao_confirmar == 'S':
                                            self.motocicletas.remove(i)
                                            print('Cadastro apagado com sucesso.\n')
                                        else:
                                            print('Operação cancelada.\n')
                                        opcao_apagar = 'N'
                                        break
                        else:
                            print('ID inválido.\n')
