from clientes import Clientes
from motocicletas import Motocicletas


# Construindo a classe vendas
class Vendas:
    vendas = []  # Lista para armazenar a lista com todas as vendas

    # Cadastrando as vendas
    def cadastrar(self):
        cadastro = {}  # Dicionário para fazer o cadastro das vendas
        opcao_cadastrar = ''  # Variável que irá interromper o loop de cadastro

        while opcao_cadastrar != 'N':
            # Definindo o ID de cada venda
            if len(self.vendas) > 0:  # Se a quantidade se vendas existentes for maior que zero
                cadastro['ID Venda'] = self.vendas[-1]['ID Venda'] + 1  # Vai buscar número do último ID e adicionar 1
            else:
                cadastro['ID Venda'] = 1  # Se não existir vendas, vai atribuir o ID 1

            id_cliente = int(input('Digite o ID do cliente comprador (0 para cancelar): '))
            print()
            if id_cliente == 0:
                print('Operação cancelada.\n')
                opcao_cadastrar = 'N'
            else:
                for cliente in Clientes.clientes:
                    if id_cliente == cliente['ID']:
                        print('Dados do cliente selecionado:')
                        for k, v in cliente.items():
                            print(k + ':', str(v))
                        cadastro['ID Cliente'] = cliente['ID']
                        cadastro['Nome Cliente'] = cliente['Nome']
                    else:
                        print('ID inválido.')
            print()

            id_motocicleta = int(input('Digite o ID da motocicleta a ser vendida (0 para cancelar): '))
            print()
            if id_motocicleta == 0:
                print('Operação cancelada.\n')
                opcao_cadastrar = 'N'
            else:
                for motocicleta in Motocicletas.motocicletas:
                    if id_motocicleta == motocicleta['ID']:
                        print('Dados da motocicleta selecionada:')
                        for k, v in motocicleta.items():
                            print(k + ':', str(v))
                        cadastro['ID Motocicleta'] = motocicleta['ID']
                        cadastro['Motocicleta'] = str(f'{motocicleta["Marca"]} {motocicleta["Ano"]} '
                                                      f'{motocicleta["Modelo"]}')
                        cadastro['Preço Motocicleta'] = str(f'{motocicleta["Preço"]}')
                        print()
                        cadastro['Forma de pagamento'] = input('Forma de pagamento: ')

                        opcao_confirmar = ''
                        while opcao_confirmar != 'N' or opcao_confirmar != 'S':
                            # Colocar .upper() no final do input converte a resposta para letras maiúsculas
                            opcao_confirmar = input('Deseja confirmar a venda? (S/N): ').upper()
                            print()
                            if opcao_confirmar == 'N' or opcao_confirmar == 'S':
                                if opcao_confirmar == 'S':
                                    self.vendas.append(cadastro)
                                    Motocicletas.motocicletas.remove(motocicleta)
                                    print('Venda cadastrada com sucesso!')
                                else:
                                    print('Operação cancelada.\n')
                                cadastro = {}
                                break
                            else:
                                print('Opção inválida.\n')
                    else:
                        print('ID inválido.\n')

            while opcao_cadastrar != 'N' or opcao_cadastrar != 'S':
                # Colocar .upper() no final do input converte a resposta para letras maiúsculas
                opcao_cadastrar = input('Deseja cadastrar outra venda? (S/N): ').upper()
                print()
                if opcao_cadastrar == 'N' or opcao_cadastrar == 'S':
                    break
                else:
                    print('Opção inválida.\n')

    # Mostrando tabela de vendas cadastradas
    def mostrar_vendas(self):
        print(66 * "=")
        print(f'{"TABELA DE VENDAS":^40}')
        print(66 * "=")
        print(f'{"ID":<5}{"CLIENTE":<30}{"MOTOCICLETA":<16}{"PREÇO":>15}')
        print(66 * "-")

        # Imprimindo a lista de vendas em formato de tabela
        for i in range(0, len(self.vendas)):
            print(f'{self.vendas[i]["ID Venda"]:<5}{self.vendas[i]["Nome Cliente"]:<30}'
                  f'{self.vendas[i]["Motocicleta"]:<16}{self.vendas[i]["Preço Motocicleta"]:>15}')
        print(66 * "-")
        print()

    # Consultando detalhes das vendas cadastradas
    def consultar(self):
        if len(self.vendas) == 0:
            print('Não existem vendas cadastradas.\n')
        else:
            opcao_consultar = ''  # Variável que irá interromper o loop de consulta
            self.mostrar_vendas()  # Mostra a lista de vendas cadastradas

            while opcao_consultar != 'N':
                detalhes = int(input('Digite o ID correspondente a venda (0 para cancelar): '))

                if detalhes == 0:
                    print('Operação cancelada.\n')
                    opcao_consultar = 'N'
                else:
                    for i in self.vendas:
                        if detalhes == i['ID Venda']:
                            print()
                            print('Dados da venda selecionada:\n')
                            for k, v in i.items():
                                print(k + ':', str(v))
                        else:
                            print('ID inválido.')
                    print()

                    while opcao_consultar != 'N' or opcao_consultar != 'S':
                        opcao_consultar = input('Deseja consultar outra venda? (S/N): ').upper()
                        if opcao_consultar == 'N' or opcao_consultar == 'S':
                            print()
                            break
                        else:
                            print('Opção inválida.\n')

    # Atualizando dados de vendas
    def atualizar(self):
        if len(self.vendas) == 0:
            print('Não existem vendas cadastradas.\n')
        else:
            id_atualizar = ''  # Variável que irá interromper o loop de atualização
            self.mostrar_vendas()  # Mostra a lista de vendas cadastradas

            while id_atualizar != 0:
                id_atualizar = int(input('Digite o ID da venda para atualizar (0 para cancelar): '))

                if id_atualizar == 0:
                    print('Operação cancelada.\n')
                    break
                else:
                    for i in self.vendas:
                        if id_atualizar == i['ID Venda']:
                            print()
                            print('Dados da venda selecionada:\n')
                            for k, v in i.items():
                                print(k + ':', str(v))
                            print('''
Digite a opção para atualizar dados sobre a venda:
                            
    [1] Preço da motocicleta
    [2] Forma de pagamento
    [0] Cancelar
    ''')

                            while True:
                                opcao_atualizar = int(input('Digite o número da opção para atualizar o cadastro: '))
                                if opcao_atualizar < 0 or opcao_atualizar > 2:
                                    print('Opção inválida.\n')
                                else:
                                    break
                            if opcao_atualizar == 1:
                                preco = float(input('Digite o preço: R$'))
                                i['Preço Motocicleta'] = str(f'R${preco:,.2f}')
                            elif opcao_atualizar == 2:
                                i['Forma de pagamento'] = input('Digite a forma de pagamento: ')

                            print()
                            if opcao_atualizar == 0:
                                print('Operação cancelada.')
                            else:
                                print('Cadastro atualizado com sucesso.')
                        else:
                            print('ID inválido.')
                    print()

    # Apagando vendas cadastradas
    def apagar(self):
        if len(self.vendas) == 0:
            print('Não existem vendas cadastradas.\n')
        else:
            opcao_apagar = ''  # Variável que irá interromper o loop de apagar
            self.mostrar_vendas()  # Mostra a lista de vendas cadastradas

            while opcao_apagar != 'N':
                id_apagar = int(input('Digite o ID da venda para apagar (0 para cancelar): '))

                if id_apagar == 0:
                    print('Operação cancelada.\n')
                    break
                else:
                    for i in self.vendas:
                        if id_apagar == i['ID Venda']:
                            print()
                            print('Dados da venda selecionada:\n')
                            for k, v in i.items():
                                print(k + ':', str(v))
                            print()

                            while True:
                                opcao_confirmar = input('Deseja apagar a venda selecionada? (S/N): ').upper()
                                if opcao_confirmar != 'S' and opcao_confirmar != 'N':
                                    print('Opção inválida.\n')
                                else:
                                    if opcao_confirmar == 'N' or opcao_confirmar == 'S':
                                        if opcao_confirmar == 'S':
                                            self.vendas.remove(i)
                                            print('Cadastro apagado com sucesso.\n')
                                        else:
                                            print('Operação cancelada.\n')
                                        opcao_apagar = 'N'
                                        break
                        else:
                            print('ID inválido.\n')
