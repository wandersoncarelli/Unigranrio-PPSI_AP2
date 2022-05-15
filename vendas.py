from clientes import Clientes
from motocicletas import Motocicletas

# Classe e funções para realizar as iterações com o menu de vendas


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
                cadastro['ID_Venda'] = self.vendas[-1]['ID_Venda'] + 1  # Vai buscar número do último ID e adicionar 1
            else:
                cadastro['ID_Venda'] = 1  # Se não existir vendas, vai atribuir o ID 1

            id_cliente = int(input('Digite o ID do cliente comprador (0 para cancelar): '))
            print()
            if id_cliente == 0:
                print('Operação cancelada.\n')
                break
            else:
                id_cliente -= 1
            print('Dados do cliente selecionado:')
            for k, v in Clientes.clientes[id_cliente].items():
                print(k + ':', str(v))
            print()

            id_motocicleta = int(input('Digite o ID da motocicleta a ser vendida (0 para cancelar): '))
            print()
            if id_motocicleta == 0:
                print('Operação cancelada.\n')
                break
            else:
                id_motocicleta -= 1
            print('Dados da motocicleta selecionada:')
            for k, v in Motocicletas.motocicletas[id_motocicleta].items():
                print(k + ':', str(v))
            print()

            opcao_confirmar = ''
            while opcao_confirmar != 'N' or opcao_confirmar != 'S':
                # Colocar .upper() no final do input converte a resposta para letras maiúsculas
                opcao_confirmar = input('Deseja confirmar a venda? (S/N): ').upper()
                print()
                if opcao_confirmar == 'N' or opcao_confirmar == 'S':
                    if opcao_confirmar == 'S':
                        cadastro['ID_Cliente'] = Clientes.clientes[id_cliente]['ID']
                        cadastro['Nome_Cliente'] = Clientes.clientes[id_cliente]['Nome']
                        cadastro['ID_Motocicleta'] = Motocicletas.motocicletas[id_motocicleta]['ID']
                        cadastro['Motocicleta'] = str(f'{Motocicletas.motocicletas[id_motocicleta]["Marca"]} '
                                                      f'{Motocicletas.motocicletas[id_motocicleta]["Modelo"]} '
                                                      f'{Motocicletas.motocicletas[id_motocicleta]["Ano"]}')
                        cadastro['Preço_Motocicleta'] = str(f'{Motocicletas.motocicletas[id_motocicleta]["Preço"]}')
                        self.vendas.append(cadastro)
                        cadastro = {}
                        Motocicletas.motocicletas.remove(Motocicletas.motocicletas[id_motocicleta])
                        print('Venda cadastrada com sucesso!')
                    else:
                        print('Operação cancelada.\n')
                    break
                else:
                    print('Opção inválida.\n')

            while opcao_cadastrar != 'N' or opcao_cadastrar != 'S':
                # Colocar .upper() no final do input converte a resposta para letras maiúsculas
                opcao_cadastrar = input('Deseja cadastrar outra venda? (S/N): ').upper()
                print()
                if opcao_cadastrar == 'N' or opcao_cadastrar == 'S':
                    break
                else:
                    print('Opção inválida.\n')

    def mostrar_vendas(self):
        print(66 * "=")
        print(f'{"TABELA DE VENDAS":^40}')
        print(66 * "=")
        print(f'{"ID":<5}{"CLIENTE":<30}{"MOTOCICLETA":<16}{"PREÇO":>15}')
        print(66 * "-")

        # Imprimindo a lista de vendas em formato de tabela
        for i in range(0, len(self.vendas)):
            print(f'{self.vendas[i]["ID_Venda"]:<5}{self.vendas[i]["Nome_Cliente"]:<30}'
                  f'{self.vendas[i]["Motocicleta"]:<16}{self.vendas[i]["Preço_Motocicleta"]:>15}')
        print(66 * "-")
        print()

    def consultar(self):
        pass

    def atualizar(self):
        pass

    def apagar(self):
        pass
