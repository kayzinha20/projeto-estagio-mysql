import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    port = "3306",
    database = "projeto",
)
cursor = mydb.cursor()
def inserir_dados(nome,cargo,salario):
    cursor.execute(f'insert into funcionario (nome,cargo,salario) values ("{nome}","{cargo}",{salario})')
    mydb.commit()
def ler_dados():
    cursor.execute(f'select * from funcionario ')
    resul = cursor.fetchall()
    for i in resul:
        print(i)
def atualizar_dados(nome,cargo,salario):
    cursor.execute(f'update funcionario set nome="{nome}",cargo="{cargo}",salario = {salario} where id={id}')
    mydb.commit()
def excluir_dados(id):
    cursor.execute(f'delete from funcionario  where id= {id}')
    mydb.commit()
def menu():
    print("-"*30)
    print("login(i): Inserir os dados")
    print("login(l): Ler os dados ")
    print("login(a): Atualizar os dados")
    print("login(e): Excluir os dados")
    print("login(sair): Encerrar programa")
    print("-"*30)
while True:
    menu()
    login = input("login: ")
    if login == "i":
        print("Caro funcionário por favor insira seus Dados.")
        nome = input("Informe seu nome:")
        cargo = input("Informe seu Cargo:")
        salario= float(input("informe seu salário:"))
        inserir_dados(nome,cargo,salario)
        print("="*70)
        print(f"Dados Inseridos. Bem-vindo(a) {nome} novo funcionario(a)!")
    elif login == "l":
        print("Dados Cadastrados: ")
        ler_dados()
    elif login == "a":
        id = int(input("Digite o id do funcionario a atualizar:"))
        nome = input("Digite o novo nome do funcionário:")
        cargo = input("Digite o novo cargo do funcionário:")
        salario = float(input("Digite o novo salario do funcionário:"))
        atualizar_dados(nome,cargo,salario)
        print("Dados do funcionario alterado com sucesso!")
    elif login == "e":
        id = input("Digite o id do funcionário a ser deletado:")
        excluir_dados(id)
        print("Funcionário deletado com sucesso.")
    elif login == "sair":
        print("Programa finalizado!")
        break
    else:
        print("Esse Login não existe.")
        print("="*30)