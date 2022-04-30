clientes = []  # Lista para armazenar todos os cadastros dos clientes
cadastro = {}  # Dicionário para fazer o cadastro dos clientes
opcao = ''  # Variável que irá interromper o loop de cadastro

# Cadastrando os clientes
while opcao != 'N':
    # Definindo o ID de cada cliente, com base na quantidade de clientes cadastrados
    cadastro['ID'] = len(clientes) + 1
    cadastro['Nome'] = input('Nome: ')
    cadastro['Idade'] = int(input('Idade: '))
    cadastro['Sexo'] = input('Sexo: ')
    cadastro['Endereço'] = input('Endereço: ')
    cadastro['Cidade'] = input('Cidade: ')
    cadastro['UF'] = input('UF: ')
    cadastro['Telefone'] = int(input('Telefone: '))
    cadastro['Email'] = input('E-mail: ')
    clientes.append(cadastro)  # Adiciona os dados de cadastro na lista
    cadastro = {}  # Apaga os dados atuais, necessário para não duplicar os cadastros na lista
    # print()
    while opcao != 'N' or opcao != 'S':
        # Colocar .upper() no final do input converte a resposta para letras maiúsculas
        opcao = input('Deseja cadastrar outro cliente? (S/N):\n').upper()
        if opcao == 'N' or opcao == 'S':
            break
        else:
            print('Opção inválida.\n')
    print()

print(40 * "=")
print(f'{"TABELA DE CLIENTES":^40}')
print(40 * "=")
print(f'{"ID":<5}{"NOME":<30}{"IDADE":>5}')
print(40 * "-")

for i in range(0, len(clientes)):
    print(f'{clientes[i]["ID"]:<5}{clientes[i]["Nome"]:<30}{clientes[i]["Idade"]:>5}')
print()

detalhes = int(input('Para consultar dados do cliente, digite seu ID correspondente: '))
print()

for k, v in clientes[detalhes - 1].items():
    print(k + ':', str(v))
