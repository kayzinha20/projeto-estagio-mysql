import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port="3306",
        database="projeto",
    )


def inserir_dados(connection, nome, cargo, salario):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO funcionario (nome,cargo,salario) VALUES (%s, %s, %s)", (nome, cargo, salario))
    connection.commit()
    print("Dados inseridos com sucesso!")
    print(f"""
    Nome: {nome}
    Cargo: {cargo}
    Salario: {salario:.2f} R$
    """)


def ler_dados(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM funcionario")
    linhas = cursor.fetchall()
    print("Lista de cadastros:")
    for funcionario in linhas:
        print(funcionario)


def atualizar_dados(connection, nome, cargo, salario, id_funcionario):
    cursor = connection.cursor()
    cursor.execute("UPDATE funcionario SET nome = %s, cargo = %s, salario = %s WHERE id = %s",
                   (nome, cargo, salario, id_funcionario))
    connection.commit()
    if cursor.rowcount == 1:
        print("Cadastro atualizado com sucesso!")
    else:
        print("ERRO: ID do funcionário não foi encontrado no sistema")


def excluir_dados(connection, id_funcionario):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM funcionario WHERE id = %s", (id_funcionario,))
    connection.commit()
    if cursor.rowcount == 1:
        print("Funcionário excluído com sucesso!")
    else:
        print("ERRO: Id do funcionário não foi encontrado no sistema")


menu = """Bem vindo caro administrador!
Selecione uma operação:
    1-Cadastrar Funcionário
    2-Visualizar Cadastros
    3-Atualizar Cadastro
    4-Excluir Cadastro
    5-Mostrar esse menu novamente
    6-Sair
"""
print(menu)
while True:
    escolha = input("Digite a operação desejada-> ")
    if escolha == "1":
        nome_input = input("Informe o nome do funcionário: ")
        cargo_input = input("Informe o cargo do funcionário: ")
        salario_input = float(input("Informe o salário do funcionário: "))
        inserir_dados(get_connection(), nome_input, cargo_input, salario_input)
    elif escolha == "2":
        ler_dados(get_connection())
    elif escolha == "3":
        id_input = int(input("Informe o ID do funcionario que deseja atualizar: "))
        nome_input = input("Informe o novo nome do funcionário: ")
        cargo_input = input("Informe o novo cargo do funcionário: ")
        salario_input = float(input("Informe o novo salario do funcionário: "))
        atualizar_dados(get_connection(), nome_input, cargo_input, salario_input, id_input)
    elif escolha == "4":
        id_input = input("Informe o ID do funcionário a ser deletado: ")
        excluir_dados(get_connection(), id_input)
    elif escolha == "5":
        print(menu)
    elif escolha == "6":
        print("Programa finalizado!")
        break

    else:
        print("Operação Inválida! Tente novamente!")
