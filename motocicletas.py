from dados import BancoDados

bd = BancoDados()


# Construindo a classe motocicletas
class Motocicletas:

    # Cadastrando motocicletas
    @staticmethod
    def cadastrar():
        opcao_cadastrar = ''  # Variável que irá interromper o loop de cadastro

        while opcao_cadastrar != 'N':
            # Solicitando os dados de cadastro da motocicleta
            Marca = input('Marca: ')
            Modelo = input('Modelo: ')
            Ano = int(input('Ano: '))
            Cilindrada = int(input('Cilindrada: '))
            Preco = float(input('Preço: '))

            # Armazenando os dados de cadastro nos campos da tabela
            bd.cursor.execute("""INSERT INTO motocicletas (marca, modelo, ano, cilindrada, preco, id_dono, nome_dono) 
            VALUES (?, ?, ?, ?, ?, 0, "Nenhum")""", (Marca, Modelo, Ano, Cilindrada, Preco))

            # Enviando os dados para o banco de dados
            bd.connect.commit()

            print('\nMotocicleta cadastrada com sucesso!')

            # Verificação para cadastro de outras motocicletas
            while opcao_cadastrar != 'N' or opcao_cadastrar != 'S':
                # Colocar .upper() no final do input converte a resposta para letras maiúsculas
                opcao_cadastrar = input('Deseja cadastrar outra motocicleta? (S/N): ').upper()
                print()
                if opcao_cadastrar == 'N' or opcao_cadastrar == 'S':
                    break
                else:
                    print('Opção inválida.\n')

    # Mostrando tabela de motocicletas cadastradas
    @staticmethod
    def mostrar_motocicletas():
        # Imprimindo a formatação da tabela
        print(54 * "=")
        print(f'{"TABELA DE MOTOCICLETAS":^54}')
        print(54 * "=")
        print(f'{"ID":<5}{"MARCA":<14}{"MODELO":<14}{"ANO":<6}{"PREÇO":>15}')
        print(54 * "-")

        # Selecionando todas as informações da tabela do banco de dados
        bd.cursor.execute("""SELECT * FROM motocicletas""")

        # Armazenando as informações em uma variável
        resultado = bd.cursor.fetchall()

        # Imprimindo a lista de motocicletas em formato de tabela
        for index in resultado:
            preco = str(f'R${index[5]:,.2f}')
            print(f'{index[0]:<5}{index[1]:<14}{index[2]:<14}{index[3]:<6}{preco:>15}')
        print(54 * "-")
        print()

    # Consultando detalhes das motocicletas cadastradas
    def consultar(self):
        opcao_consultar = ''  # Variável que irá interromper o loop de consulta
        self.mostrar_motocicletas()  # Mostra a lista de motocicletas cadastrados

        while opcao_consultar != 'N':
            detalhes = int(input('Digite o ID correspondente à motocicleta (0 para cancelar): '))

            if detalhes == 0:
                print('Operação cancelada.\n')
                opcao_consultar = 'N'
            else:
                # Realizando a busca na tabela com filtro pelo ID
                bd.cursor.execute(f"""SELECT * FROM motocicletas WHERE id = {detalhes}""")

                # Verificando se o ID escolhido é valido
                if bd.cursor.fetchone() is None:
                    print('ID inválido.\n')
                else:
                    bd.cursor.execute(f"""SELECT * FROM motocicletas WHERE id = {detalhes}""")
                    # Armazenando os dados em uma variável
                    resultado = bd.cursor.fetchall()
                    for index in resultado:
                        print(f'''
ID: {index[0]}
Marca: {index[1]}
Modelo: {index[2]}
Ano: {index[3]}
Cilindradas: {index[4]}
Preço: R${index[5]:,.2f}
ID cliente dono: {index[6]}
Nome cliente dono: {index[7]}
''')

                while opcao_consultar != 'N' or opcao_consultar != 'S':
                    opcao_consultar = input('Deseja consultar outra motocicleta? (S/N): ').upper()
                    if opcao_consultar == 'N' or opcao_consultar == 'S':
                        print()
                        break
                    else:
                        print('Opção inválida.\n')

    @staticmethod
    def procurar():
        resultado = ''
        opcao_procurar = ''

        while opcao_procurar != 'N':
            nome = input('Digite a marca da motocicleta a ser procurada: ')

            # Realizando a busca na tabela com filtro pelo nome
            bd.cursor.execute(f"""SELECT * FROM motocicletas WHERE marca like "%{nome}%" """)

            # Verificando se o nome digitado está na tabela
            if bd.cursor.fetchone() is None:
                print('Nenhuma motocicleta cadastrada com a marca selecionada.\n')
            else:
                print()
                bd.cursor.execute(f"""SELECT * FROM motocicletas WHERE marca like "%{nome}%" """)
                # Armazenando os dados em uma variável
                resultado = bd.cursor.fetchall()

            if resultado != '':
                # Imprimindo a formatação da tabela
                print(54 * "=")
                print(f'{"TABELA DE MOTOCICLETAS":^54}')
                print(54 * "=")
                print(f'{"ID":<5}{"MARCA":<14}{"MODELO":<14}{"ANO":<6}{"PREÇO":>15}')
                print(54 * "-")

                # Imprimindo a lista de motocicletas em formato de tabela
                for index in resultado:
                    preco = str(f'R${index[5]:,.2f}')
                    print(f'{index[0]:<5}{index[1]:<14}{index[2]:<14}{index[3]:<6}{preco:>15}')
                print(54 * "-")
                print()

            while opcao_procurar != 'N' or opcao_procurar != 'S':
                opcao_procurar = input('Deseja procurar novamente? (S/N): ').upper()
                if opcao_procurar == 'N' or opcao_procurar == 'S':
                    print()
                    break
                else:
                    print('Opção inválida.\n')

    # Atualizando cadastro de motocicletas
    def atualizar(self):
        id_atualizar = ''  # Variável que irá interromper o loop de atualização
        self.mostrar_motocicletas()  # Mostra a lista de motocicletas cadastradas

        while id_atualizar != 0:
            id_atualizar = int(input('Digite o ID da motocicleta para atualizar (0 para cancelar): '))

            if id_atualizar == 0:
                print('Operação cancelada.\n')
                break
            else:
                # Realizando a busca na tabela com filtro pelo ID
                bd.cursor.execute(f"""SELECT * FROM motocicletas WHERE id = {id_atualizar}""")

                # Verificando se o ID escolhido é valido
                if bd.cursor.fetchone() is None:
                    print('ID inválido.')
                else:
                    # Armazenando os dados em uma variável
                    bd.cursor.execute(f"""SELECT * FROM motocicletas WHERE id = {id_atualizar}""")
                    resultado = bd.cursor.fetchall()

                    # Mostrando as opções de atualização do cadastro
                    for index in resultado:
                        print(f'''
[X] ID: {index[0]}
[1] Marca: {index[1]}
[2] Modelo: {index[2]}
[3] Ano: {index[3]}
[4] Cilindradas: {index[4]}
[5] Preço: R${index[5]:,.2f}
[0] CANCELAR
''')

                        while True:
                            opcao_atualizar = int(input('Digite o número da opção para atualizar o cadastro: '))
                            if opcao_atualizar < 0 or opcao_atualizar > 8:
                                print('Opção inválida.\n')
                            else:
                                break

                        if opcao_atualizar == 1:
                            Atualizar = input('Marca: ')
                            bd.cursor.execute(f"""UPDATE motocicletas SET marca = "{Atualizar}" 
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 2:
                            Atualizar = input('Modelo: ')
                            bd.cursor.execute(f"""UPDATE motocicletas SET modelo = "{Atualizar}"
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 3:
                            Atualizar = int(input('Ano: '))
                            bd.cursor.execute(f"""UPDATE motocicletas SET ano = {Atualizar} 
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 4:
                            Atualizar = int(input('Cilindradas: '))
                            bd.cursor.execute(f"""UPDATE motocicletas SET cilindrada = {Atualizar} 
                                                WHERE id = {id_atualizar}""")
                        elif opcao_atualizar == 5:
                            Atualizar = float(input('Preço: R$'))
                            bd.cursor.execute(f"""UPDATE motocicletas SET preco = {Atualizar} 
                                                WHERE id = {id_atualizar}""")

                        # Enviando as alterações para a tabela
                        bd.connect.commit()

                        if opcao_atualizar == 0:
                            print('Operação cancelada.')
                        else:
                            print('Cadastro atualizado com sucesso.')
                    print()

    # Apagando motocicletas cadastradas
    def apagar(self):
        opcao_apagar = ''  # Variável que irá interromper o loop de apagar
        self.mostrar_motocicletas()  # Mostra a lista de motocicletas cadastradas

        while opcao_apagar != 'N':
            id_apagar = int(input('Digite o ID da motocicleta para apagar (0 para cancelar): '))

            if id_apagar == 0:
                print('Operação cancelada.\n')
                break
            else:
                # Realizando a busca na tabela com filtro pelo ID
                bd.cursor.execute(f"""SELECT * FROM motocicletas WHERE id = {id_apagar}""")

                # Verificando se o ID escolhido é valido
                if bd.cursor.fetchone() is None:
                    print('ID inválido.\n')
                else:
                    bd.cursor.execute(f"""SELECT * FROM motocicletas WHERE id = {id_apagar}""")
                    # Armazenando os dados em uma variável
                    resultado = bd.cursor.fetchall()
                    for index in resultado:
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
                    while True:
                        opcao_confirmar = input('Deseja apagar o cadastro selecionado? (S/N): ').upper()
                        if opcao_confirmar != 'S' and opcao_confirmar != 'N':
                            print('Opção inválida.\n')
                        else:
                            if opcao_confirmar == 'N' or opcao_confirmar == 'S':
                                if opcao_confirmar == 'S':

                                    # Apagando as informações do cadastro selecionado
                                    bd.cursor.execute(f"""DELETE FROM motocicletas WHERE id = {id_apagar}""")

                                    # Enviando as alterações para a tabela
                                    bd.connect.commit()
                                    print('Cadastro apagado com sucesso.\n')
                                else:
                                    print('Operação cancelada.\n')
                                opcao_apagar = 'N'
                                break
