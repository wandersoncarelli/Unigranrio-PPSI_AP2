from dados import BancoDados

bd = BancoDados()


# Construindo a classe vendas
class Vendas:

    # Cadastrando as vendas
    def __init__(self):
        self.ID_Cliente = self.Nome_Cliente = None
        self.ID_Motocicleta = self.Marca_Motocicleta = self.Modelo_Motocicleta = self.Ano_Motocicleta = \
            self.Preco_Motocicleta = None

    def cadastrar(self):
        opcao_cadastrar = ''  # Variável que irá interromper o loop de cadastro

        while opcao_cadastrar != 'N':
            id_cliente = int(input('Digite o ID do cliente comprador (0 para cancelar): '))
            if id_cliente == 0:
                print('Operação cancelada.\n')
                opcao_cadastrar = 'N'
            else:
                # Realizando a busca na tabela com filtro pelo ID
                bd.cursor.execute(f"""SELECT * FROM clientes WHERE id = {id_cliente}""")

                # Verificando se o ID escolhido é valido
                if bd.cursor.fetchone() is None:
                    print('ID inválido.\n')
                else:
                    bd.cursor.execute(f"""SELECT * FROM clientes WHERE id = {id_cliente}""")
                    # Armazenando os dados em uma variável
                    resultado = bd.cursor.fetchall()
                    for index in resultado:
                        print(f'''
Dados do cliente selecionado:

ID: {index[0]}
Nome: {index[1]}
Idade: {index[2]}
Sexo: {index[3]}
Endereço: {index[4]}
Cidade: {index[5]}
UF: {index[6]}
Telefone: {index[7]}
E-mail: {index[8]}
''')

                        self.ID_Cliente = index[0]
                        self.Nome_Cliente = index[1]

            id_motocicleta = int(input('Digite o ID da motocicleta a ser vendida (0 para cancelar): '))
            if id_motocicleta == 0:
                print('Operação cancelada.\n')
                opcao_cadastrar = 'N'
            else:
                # Realizando a busca na tabela com filtro pelo ID
                bd.cursor.execute(f"""SELECT * FROM motocicletas WHERE id = {id_motocicleta}""")

                # Verificando se o ID escolhido é valido
                if bd.cursor.fetchone() is None:
                    print('ID inválido.\n')
                else:
                    bd.cursor.execute(f"""SELECT * FROM motocicletas WHERE id = {id_motocicleta}""")
                    # Armazenando os dados em uma variável
                    resultado = bd.cursor.fetchall()
                    for index in resultado:
                        if index[6] != 0:
                            print('A motocicleta seleciona já possui um dono.\n')
                            break
                        else:
                            print(f'''
Dados da motocicleta selecionada:

ID: {index[0]}
Marca: {index[1]}
Modelo: {index[2]}
Ano: {index[3]}
Cilindradas: {index[4]}
Preço: R${index[5]:,.2f}
ID cliente dono: {index[6]}
Nome cliente dono: {index[7]}
''')

                        self.ID_Motocicleta = index[0]
                        self.Marca_Motocicleta = index[1]
                        self.Modelo_Motocicleta = index[2]
                        self.Ano_Motocicleta = index[3]
                        self.Preco_Motocicleta = index[5]

                        opcao_confirmar = ''
                        while opcao_confirmar != 'N' or opcao_confirmar != 'S':
                            # Colocar .upper() no final do input converte a resposta para letras maiúsculas
                            opcao_confirmar = input('Deseja confirmar a venda? (S/N): ').upper()
                            print()
                            if opcao_confirmar == 'N' or opcao_confirmar == 'S':
                                if opcao_confirmar == 'S':
                                    # Armazenando os dados de cadastro nos campos da tabela
                                    bd.cursor.execute("""
                                    INSERT INTO vendas (id_cliente, nome_cliente, id_motocicleta, marca_motocicleta, 
                                    modelo_motocicleta, ano_motocicleta, preco_motocicleta) VALUES (?, ?, ?, ?, ?, ?, ?)
                                    """, (self.ID_Cliente, self.Nome_Cliente, self.ID_Motocicleta,
                                          self.Marca_Motocicleta, self.Modelo_Motocicleta,
                                          self.Ano_Motocicleta, self.Preco_Motocicleta))

                                    # Atualizando os dados da motocicleta vendida
                                    bd.cursor.execute(f"""UPDATE motocicletas SET id_dono = {self.ID_Cliente} 
                                                        WHERE id = "{id_motocicleta}" """)
                                    bd.cursor.execute(f"""UPDATE motocicletas SET nome_dono = "{self.Nome_Cliente}" 
                                                        WHERE id = "{id_motocicleta}" """)

                                    # Enviando os dados para o banco de dados
                                    bd.connect.commit()

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

    # Consultando todas as vendas cadastradas com detalhes
    @staticmethod
    def consultar():
        opcao_consultar = ''  # Variável que irá interromper o loop de consulta
        # Imprimindo a formatação da tabela
        print(66 * "=")
        print(f'{"TABELA DE VENDAS":^66}')
        print(66 * "=")
        print(f'{"ID":<5}{"CLIENTE":<26}{"MOTOCICLETA":<20}{"PREÇO":>15}')
        print(66 * "-")

        # Selecionando todas as informações da tabela do banco de dados
        bd.cursor.execute("""SELECT * FROM vendas""")

        # Armazenando as informações em uma variável
        resultado = bd.cursor.fetchall()

        # Imprimindo a lista de clientes em formato de tabela
        for index in resultado:
            motocicleta = f'{index[4]} {index[5]} {index[6]}'
            preco = str(f'R${index[7]:,.2f}')
            print(f'{index[0]:<5}{index[2]:<26}{motocicleta:<20}{preco:>15}')
            print(66 * "-")
        print()

        while opcao_consultar != 'N':
            detalhes = int(input('Digite o ID correspondente à venda para ver detalhes (0 para cancelar): '))

            if detalhes == 0:
                print('Operação cancelada.\n')
                opcao_consultar = 'N'
            else:
                # Realizando a busca na tabela com filtro pelo ID
                bd.cursor.execute(f"""SELECT * FROM vendas WHERE id = {detalhes}""")

                # Verificando se o ID escolhido é valido
                if bd.cursor.fetchone() is None:
                    print('ID inválido.\n')
                else:
                    bd.cursor.execute(f"""SELECT * FROM vendas WHERE id = {detalhes}""")
                    # Armazenando os dados em uma variável
                    resultado = bd.cursor.fetchall()
                    for index in resultado:
                        print(f'''
Detalhes da venda selecionada:

ID Venda: {index[0]}
ID Cliente: {index[1]}
Nome: {index[2]}
ID Motocicleta: {index[3]}
Marca: {index[4]}
Modelo: {index[5]}
Ano: {index[6]}
Preço: R${index[7]:,.2f}
''')

                while opcao_consultar != 'N' or opcao_consultar != 'S':
                    opcao_consultar = input('Deseja consultar outra venda? (S/N): ').upper()
                    if opcao_consultar == 'N' or opcao_consultar == 'S':
                        print()
                        break
                    else:
                        print('Opção inválida.\n')

    # Procurando vendas cadastradas por cliente/motocicleta
    @staticmethod
    def procurar():
        resultado = ''

        while True:
            print('''PROCURAR POR:
    
    [1] - Cliente
    [2] - Motocicleta
    [0] - Voltar ao menu anterior
''')

            procurar_opcao = int(input('Digite a opção escolhida: '))
            print()
            if procurar_opcao < 0 or procurar_opcao > 2:
                print('Opção inválida.')
            else:
                if procurar_opcao == 0:
                    break
                elif procurar_opcao == 1:
                    cliente = input('Digite o nome do cliente a ser procurado: ')
                    # Realizando a busca na tabela com filtro pelo nome
                    bd.cursor.execute(f"""SELECT * FROM vendas WHERE nome_cliente like "%{cliente}%" """)

                    # Verificando se o nome digitado está na tabela
                    if bd.cursor.fetchone() is None:
                        print('Nenhuma venda cadastrada com o cliente selecionado.\n')
                    else:
                        print()
                        bd.cursor.execute(f"""SELECT * FROM vendas WHERE nome_cliente like "%{cliente}%" """)
                        # Armazenando os dados em uma variável
                        resultado = bd.cursor.fetchall()

                elif procurar_opcao == 2:
                    marca = input('Digite a marca da motocicleta a ser procurada: ')
                    # Realizando a busca na tabela com filtro pelo nome
                    bd.cursor.execute(f"""SELECT * FROM vendas WHERE marca_motocicleta like "%{marca}%" """)

                    # Verificando se o nome digitado está na tabela
                    if bd.cursor.fetchone() is None:
                        print('Nenhuma venda cadastrada com a marca de motocicleta selecionada.\n')
                    else:
                        print()
                        bd.cursor.execute(f"""SELECT * FROM vendas WHERE marca_motocicleta like "%{marca}%" """)
                        # Armazenando os dados em uma variável
                        resultado = bd.cursor.fetchall()

                if resultado != '':
                    # Imprimindo a formatação da tabela
                    print(66 * "=")
                    print(f'{"TABELA DE VENDAS":^66}')
                    print(66 * "=")
                    print(f'{"ID":<5}{"CLIENTE":<26}{"MOTOCICLETA":<20}{"PREÇO":>15}')
                    print(66 * "-")

                    # Imprimindo a lista de clientes em formato de tabela
                    for index in resultado:
                        motocicleta = f'{index[4]} {index[5]} {index[6]}'
                        preco = str(f'R${index[7]:,.2f}')
                        print(f'{index[0]:<5}{index[2]:<26}{motocicleta:<20}{preco:>15}')
                        print(66 * "-")
                        print()

    # Apagando vendas cadastradas
    @staticmethod
    def apagar():
        opcao_apagar = ''  # Variável que irá interromper o loop de apagar
        # Imprimindo a formatação da tabela
        print(66 * "=")
        print(f'{"TABELA DE VENDAS":^66}')
        print(66 * "=")
        print(f'{"ID":<5}{"CLIENTE":<26}{"MOTOCICLETA":<20}{"PREÇO":>15}')
        print(66 * "-")

        # Selecionando todas as informações da tabela do banco de dados
        bd.cursor.execute("""SELECT * FROM vendas""")

        # Armazenando as informações em uma variável
        resultado = bd.cursor.fetchall()

        # Imprimindo a lista de clientes em formato de tabela
        for index in resultado:
            motocicleta = f'{index[4]} {index[5]} {index[6]}'
            preco = str(f'R${index[7]:,.2f}')
            print(f'{index[0]:<5}{index[2]:<26}{motocicleta:<20}{preco:>15}')
            print(66 * "-")
        print()

        while opcao_apagar != 'N':
            id_apagar = int(input('Digite o ID da venda para apagar (0 para cancelar): '))

            if id_apagar == 0:
                print('Operação cancelada.\n')
                break
            else:
                # Realizando a busca na tabela com filtro pelo ID
                bd.cursor.execute(f"""SELECT * FROM vendas WHERE id = {id_apagar}""")

                # Verificando se o ID escolhido é valido
                if bd.cursor.fetchone() is None:
                    print('ID inválido.\n')
                else:
                    bd.cursor.execute(f"""SELECT * FROM vendas WHERE id = {id_apagar}""")
                    # Armazenando os dados em uma variável
                    resultado = bd.cursor.fetchall()
                    for index in resultado:
                        print(f'''
Detalhes da venda selecionada:

ID Venda: {index[0]}
ID Cliente: {index[1]}
Nome: {index[2]}
ID Motocicleta: {index[3]}
Marca: {index[4]}
Modelo: {index[5]}
Ano: {index[6]}
Preço: R${index[7]:,.2f}
''')

                    while True:
                        opcao_confirmar = input('Deseja apagar a venda selecionada? (S/N): ').upper()
                        if opcao_confirmar != 'S' and opcao_confirmar != 'N':
                            print('Opção inválida.\n')
                        else:
                            if opcao_confirmar == 'N' or opcao_confirmar == 'S':
                                if opcao_confirmar == 'S':

                                    # Apagando as informações do cadastro selecionado
                                    bd.cursor.execute(f"""DELETE FROM vendas WHERE id = {id_apagar}""")

                                    # Enviando as alterações para a tabela
                                    bd.connect.commit()
                                    print('Venda apagada com sucesso.\n')
                                else:
                                    print('Operação cancelada.\n')
                                opcao_apagar = 'N'
                                break
