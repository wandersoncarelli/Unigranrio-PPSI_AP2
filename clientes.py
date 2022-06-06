from dados import BancoDados

bd = BancoDados()


# Construindo a classe clientes
class Clientes:

    # Cadastrando os clientes
    @staticmethod
    def cadastrar():
        opcao_cadastrar = ''  # Variável que irá interromper o loop de cadastro

        while opcao_cadastrar != 'N':
            # Solicitando os dados de cadastro do cliente
            Nome = input('Nome completo: ')
            Idade = int(input('Idade: '))
            Sexo = input('Sexo: ')
            Endereco = input('Endereço: ')
            Cidade = input('Cidade: ')
            UF = input('UF: ')
            Telefone = int(input('Telefone: '))
            Email = input('E-mail: ')

            # Armazenando os dados de cadastro nos campos da tabela
            bd.cursor.execute("""
            INSERT INTO clientes (nome, idade, sexo, endereço, cidade, uf, telefone, email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (Nome, Idade, Sexo, Endereco, Cidade, UF, Telefone, Email))

            # Enviando as alterações para a tabela
            bd.connect.commit()

            print('\nCliente cadastrado com sucesso!')

            # Verificação para cadastro de outros clientes
            while opcao_cadastrar != 'N' or opcao_cadastrar != 'S':
                # Colocar .upper() no final do input converte a resposta para letras maiúsculas
                opcao_cadastrar = input('Deseja cadastrar outro cliente? (S/N): ').upper()
                print()
                if opcao_cadastrar == 'N' or opcao_cadastrar == 'S':
                    break
                else:
                    print('Opção inválida.\n')

    # Mostrando tabela de clientes cadastrados
    @staticmethod
    def mostrar_clientes():
        # Imprimindo a formatação da tabela
        print(40 * "=")
        print(f'{"TABELA DE CLIENTES":^40}')
        print(40 * "=")
        print(f'{"ID":<5}{"NOME":<30}{"IDADE":>5}')
        print(40 * "-")

        # Selecionando todas as informações da tabela do banco de dados
        bd.cursor.execute("""SELECT * FROM clientes""")

        # Armazenando as informações em uma variável
        resultado = bd.cursor.fetchall()

        # Imprimindo a lista de clientes em formato de tabela
        for index in resultado:
            print(f'{index[0]:<5}{index[1]:<30}{index[2]:>5}')
        print(40 * "-")
        print()

    # Consultando os detalhes dos clientes cadastrados
    def consultar(self):
        opcao_consultar = ''  # Variável que irá interromper o loop de consulta
        self.mostrar_clientes()  # Mostra a lista de clientes cadastrados

        while opcao_consultar != 'N':
            detalhes = int(input('Digite o ID correspondente ao cliente (0 para cancelar): '))

            if detalhes == 0:
                print('Operação cancelada.\n')
                opcao_consultar = 'N'
            else:
                # Realizando a busca na tabela com filtro pelo ID
                bd.cursor.execute(f"""SELECT * FROM clientes WHERE id = {detalhes}""")

                # Verificando se o ID escolhido é valido
                if bd.cursor.fetchone() is None:
                    print('ID inválido.\n')
                else:
                    bd.cursor.execute(f"""SELECT * FROM clientes WHERE id = {detalhes}""")
                    # Armazenando os dados em uma variável
                    resultado = bd.cursor.fetchall()
                    for index in resultado:
                        print(f'''
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

                while opcao_consultar != 'N' or opcao_consultar != 'S':
                    opcao_consultar = input('Deseja consultar outro cliente? (S/N): ').upper()
                    if opcao_consultar == 'N' or opcao_consultar == 'S':
                        print()
                        break
                    else:
                        print('Opção inválida.\n')

    # Procurando clientes cadastrados pelo nome
    @staticmethod
    def procurar():
        resultado = ''
        opcao_procurar = ''

        while opcao_procurar != 'N':
            nome = input('Digite o nome do cliente a ser procurado: ')

            # Realizando a busca na tabela com filtro pelo nome
            bd.cursor.execute(f"""SELECT * FROM clientes WHERE nome like "%{nome}%" """)

            # Verificando se o nome digitado está na tabela
            if bd.cursor.fetchone() is None:
                print('Nenhum cliente cadastrado com o nome selecionado.\n')
            else:
                print()
                bd.cursor.execute(f"""SELECT * FROM clientes WHERE nome like "%{nome}%" """)
                # Armazenando os dados em uma variável
                resultado = bd.cursor.fetchall()

            if resultado != '':
                # Imprimindo a formatação da tabela
                print(40 * "=")
                print(f'{"TABELA DE CLIENTES":^40}')
                print(40 * "=")
                print(f'{"ID":<5}{"NOME":<30}{"IDADE":>5}')
                print(40 * "-")

                # Imprimindo a lista de clientes em formato de tabela
                for index in resultado:
                    print(f'{index[0]:<5}{index[1]:<30}{index[2]:>5}')
                print(40 * "-")
                print()

            while opcao_procurar != 'N' or opcao_procurar != 'S':
                opcao_procurar = input('Deseja procurar novamente? (S/N): ').upper()
                if opcao_procurar == 'N' or opcao_procurar == 'S':
                    print()
                    break
                else:
                    print('Opção inválida.\n')

    # Atualizando o cadastro de clientes
    def atualizar(self):
        id_atualizar = ''  # Variável que irá interromper o loop de atualização
        self.mostrar_clientes()  # Mostra a lista de clientes cadastrados

        while id_atualizar != 0:
            id_atualizar = int(input('Digite o ID do cliente para atualizar (0 para cancelar): '))

            if id_atualizar == 0:
                print('Operação cancelada.\n')
                break
            else:
                # Realizando a busca na tabela com filtro pelo ID
                bd.cursor.execute(f"""SELECT * FROM clientes WHERE id = {id_atualizar}""")

                # Verificando se o ID escolhido é valido
                if bd.cursor.fetchone() is None:
                    print('ID inválido.')
                else:
                    # Armazenando os dados em uma variável
                    bd.cursor.execute(f"""SELECT * FROM clientes WHERE id = {id_atualizar}""")
                    resultado = bd.cursor.fetchall()

                    # Mostrando as opções de atualização do cadastro
                    for index in resultado:
                        print(f'''
[X] ID: {index[0]}
[1] Nome: {index[1]}
[2] Idade: {index[2]}
[3] Sexo: {index[3]}
[4] Endereço: {index[4]}
[5] Cidade: {index[5]}
[6] UF: {index[6]}
[7] Telefone: {index[7]}
[8] E-mail: {index[8]}
[0] CANCELAR
''')

                        while True:
                            opcao_atualizar = int(input('Digite o número da opção para atualizar o cadastro: '))
                            if opcao_atualizar < 0 or opcao_atualizar > 8:
                                print('Opção inválida.\n')
                            else:
                                break

                        if opcao_atualizar == 1:
                            Atualizar = input('Nome: ')
                            bd.cursor.execute(f"""UPDATE clientes SET nome = "{Atualizar}" 
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 2:
                            Atualizar = int(input('Idade: '))
                            bd.cursor.execute(f"""UPDATE clientes SET idade = {Atualizar}
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 3:
                            Atualizar = input('Sexo: ')
                            bd.cursor.execute(f"""UPDATE clientes SET sexo = "{Atualizar}" 
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 4:
                            Atualizar = input('Endereco: ')
                            bd.cursor.execute(f"""UPDATE clientes SET endereço = "{Atualizar}" 
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 5:
                            Atualizar = input('Cidade: ')
                            bd.cursor.execute(f"""UPDATE clientes SET cidade = "{Atualizar}" 
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 6:
                            Atualizar = input('UF: ')
                            bd.cursor.execute(f"""UPDATE clientes SET uf = "{Atualizar}" 
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 7:
                            Atualizar = int(input('Telefone: '))
                            bd.cursor.execute(f"""UPDATE clientes SET telefone = {Atualizar}
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 8:
                            Atualizar = input('Email: ')
                            bd.cursor.execute(f"""UPDATE clientes SET email = "{Atualizar}" 
                                                WHERE id = {id_atualizar}""")

                        if opcao_atualizar == 0:
                            print('Operação cancelada.')
                        else:
                            # Enviando as alterações para a tabela
                            bd.connect.commit()
                            print('Cadastro atualizado com sucesso.')
                print()

    # Apagando clientes cadastrados
    def apagar(self):
        opcao_apagar = ''  # Variável que irá interromper o loop de apagar
        self.mostrar_clientes()  # Mostra a lista de clientes cadastrados

        while opcao_apagar != 'N':
            id_apagar = int(input('Digite o ID do cliente para apagar (0 para cancelar): '))

            if id_apagar == 0:
                print('Operação cancelada.\n')
                break
            else:
                # Realizando a busca na tabela com filtro pelo ID
                bd.cursor.execute(f"""SELECT * FROM clientes WHERE id = {id_apagar}""")

                # Verificando se o ID escolhido é valido
                if bd.cursor.fetchone() is None:
                    print('ID inválido.\n')
                else:
                    bd.cursor.execute(f"""SELECT * FROM clientes WHERE id = {id_apagar}""")
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

                    while True:
                        opcao_confirmar = input('Deseja apagar o cadastro selecionado? (S/N): ').upper()
                        if opcao_confirmar != 'S' and opcao_confirmar != 'N':
                            print('Opção inválida.\n')
                        else:
                            if opcao_confirmar == 'N' or opcao_confirmar == 'S':
                                if opcao_confirmar == 'S':

                                    # Apagando as informações do cadastro selecionado
                                    bd.cursor.execute(f"""DELETE FROM clientes WHERE id = {id_apagar}""")

                                    # Enviando as alterações para a tabela
                                    bd.connect.commit()
                                    print('Cadastro apagado com sucesso.\n')
                                else:
                                    print('Operação cancelada.\n')
                                opcao_apagar = 'N'
                                break
