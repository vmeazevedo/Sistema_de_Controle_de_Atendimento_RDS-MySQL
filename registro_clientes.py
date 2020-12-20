import mysql.connector
from mysql.connector import errorcode
from mysql.connector import cursor

###############################################################################################################
# MySQL Workbench - Realizar a criação da base e da tabela.
###############################################################################################################
'''
create database Registro;
use Registro;
CREATE TABLE Pacientes (
  ID int auto_increment,
  Nome varchar(50) not null,
  cpf varchar(50) not null,
  Email varchar(200) not null,
  Telefone varchar(20) not null,
  Data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  Procedimento varchar(255) not null,
  Responsável varchar(100) not null,
  primary key (id)
  ) engine=innodb;
'''
###############################################################################################################


###############################################################################################################
# Conexão da instância RDS - Amazon Web Service
###############################################################################################################
# Preencher os campos de conexão abaixo
host = 'localhost'      # Endpoint da instância RDS na cloud da AWS
user = 'root'           # Username criado na hora de realizar a instância RDS
password = ''           # Password criado na hora de realizar a instância RDS
database = 'Registro'   # Database criada no MySQL

try:
	db_connection = mysql.connector.connect(host = host, user = user, password = password, database = database)
	print("\nConexão com a base de dados realizada!\n")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("\nA base de dados não existe.")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("\nUsername ou o password está errado.")
	else:
		print(error)
###############################################################################################################

def menu():
    print("===================================================")
    print("         Sistema de Controle de Atendimento        ")
    print("===================================================\n")

    print("Opções:")
    print("1 - Cadastro de novo atendimento")
    print("2 - Visualizar os atendimentos realizados")
    print("3 - Realização de consulta por item")
    print("4 - Alteração de dados cadastrados\n")
    flag = True
    while True:
        choose = input(str("Informe a operação desejada: "))
        if choose == "1":
            print("Cadastro de novo atendimento selecionado.\n")
            inserir()
        elif choose == "2":
            print("Visualização dos atendimentos realizados selecionado.\n")
            consulta_base()
        elif choose == "3":
            print("Realização de consulta por item selecionada.\n")
            consulta_item()
        elif choose == "4":
            print("Alteração de dados cadastrados selecionado.\n")
            update()
        else:
            print("AVISO: Digite somente o número de uma das opções apresentados.\n")

def inserir():
    # Declaração de variável
    cursor = db_connection.cursor()
    
    flag = True
    while True:
        # input manual dentro do INSERT
        print("Por favor, preencha os campos abaixo conforme solicitado.")
        Nome = input(str("Nome: ")).title()
        cpf = input(str("CPF: "))
        Email = input(str("E-mail: ")).lower()
        Telefone = input(str("Tel: "))
        Procedimento = input(str("Procedimento: ")).capitalize()
        Responsável = input(str("Responsável: ")).title()

        sql = "INSERT INTO Pacientes (Nome, CPF, Email, Telefone, Procedimento, Responsável) VALUES ('%s', '%s','%s', '%s', '%s', '%s')" % (Nome, cpf, Email, Telefone, Procedimento, Responsável)
        cursor.execute(sql)
        print("\nDados inseridos com sucesso")

        response = input(str("Gostaria de adicionar mais um registro? [S/N]? ")).lower()
        print("\n")
        if response == 's':
            flag = True
        else:
            break
    cursor.close()
    db_connection.commit()
    menu()

def consulta_base():
    flag = True
    while True:
        cursor = db_connection.cursor()
        # Apresentando o header da base de dados
        sql = ("SELECT * FROM Pacientes")
        cursor.execute(sql)
        print(cursor.column_names)
        rows = cursor.fetchall()
    
        # Apresentando a base de dados completa
        sql = ("SELECT ID, Nome, CPF, Email, Telefone, Procedimento, Responsável FROM Pacientes")
        cursor.execute(sql)
        for (ID, Nome, cpf, Email, Telefone, Procedimento, Responsável) in cursor:
            print(ID, Nome, cpf, Email, Telefone, Procedimento, Responsável)
        print("\n")

        response = input(str("Gostaria de realizar a consulta novamente? [S/N]? ")).lower()
        print("\n")
        if response == 's':
            flag = True
        else:
            break
    cursor.close()
    db_connection.commit()
    menu()

'''
Realizar o tratamento de exceção das entrada de dados da consulta por item.
'''
def consulta_item():
    flag = True
    while True:
        cursor = db_connection.cursor()
        print("1 - Nome")
        print("2 - CPF")
        print("3 - E-mail")
        print("4 - Telefone")
        print("5 - Procedimento")
        print("6 - Responsável")
        choose = input(str("Selecione o tipo de consulta, exemplo(Consulta por Nome): "))
        if choose == "1":
            nome = input(str("Digite o nome que está procurando: ")).title()
            sql = ("SELECT * from Pacientes WHERE Nome ='%s'") % (nome)
            cursor.execute(sql)
                        
            for (Nome) in cursor:
                print("\nApresentando dados solicitados:")
                lista = ['ID','Nome','E-mail','Telefone','Data de Atendimento','Procedimento','Responsável']
                print(lista)
                print(Nome)
            print("\n")

            response = input(str("Gostaria de realizar a consulta novamente? [S/N]? ")).lower()
            print("\n")
            if response == 's':
                flag = True
            else:
                cursor.close()
                db_connection.commit()
                menu()

        if choose == "2":
            cpf = input(str("Digite o CPF que está procurando: "))
            sql = ("SELECT * from Pacientes WHERE cpf ='%s'") % (cpf)
            cursor.execute(sql)
                        
            for (cpf) in cursor:
                print("\nApresentando dados solicitados:")
                lista = ['ID','Nome','E-mail','Telefone','Data de Atendimento','Procedimento','Responsável']
                print(lista)
                print(cpf)
            print("\n")

            response = input(str("Gostaria de realizar a consulta novamente? [S/N]? ")).lower()
            print("\n")
            if response == 's':
                flag = True
            else:
                cursor.close()
                db_connection.commit()
                menu()

        if choose == "3":
            email = input(str("Digite o e-mail que está procurando: ")).lower()
            sql = ("SELECT * from Pacientes WHERE Email ='%s'") % (email)
            cursor.execute(sql)
                        
            for (email) in cursor:
                print("\nApresentando dados solicitados:")
                lista = ['ID','Nome','E-mail','Telefone','Data de Atendimento','Procedimento','Responsável']
                print(lista)
                print(email)
            print("\n")

            response = input(str("Gostaria de realizar a consulta novamente? [S/N]? ")).lower()
            print("\n")
            if response == 's':
                flag = True
            else:
                cursor.close()
                db_connection.commit()
                menu()

        if choose == "4":
            telefone = input(str("Digite o telefone que está procurando: "))
            sql = ("SELECT * from Pacientes WHERE Telefone ='%s'") % (telefone)
            cursor.execute(sql)
                        
            for (telefone) in cursor:
                print("\nApresentando dados solicitados:")
                lista = ['ID','Nome','E-mail','Telefone','Data de Atendimento','Procedimento','Responsável']
                print(lista)
                print(telefone)
            print("\n")

            response = input(str("Gostaria de realizar a consulta novamente? [S/N]? ")).lower()
            print("\n")
            if response == 's':
                flag = True
            else:
                cursor.close()
                db_connection.commit()
                menu() 

        if choose == "5":
            procedimento = input(str("Digite o procedimento que está procurando: ")).capitalize()
            sql = ("SELECT * from Pacientes WHERE Procedimento ='%s'") % (procedimento)
            cursor.execute(sql)
                        
            for (procedimento) in cursor:
                print("\nApresentando dados solicitados:")
                lista = ['ID','Nome','E-mail','Telefone','Data de Atendimento','Procedimento','Responsável']
                print(lista)
                print(procedimento)
            print("\n")

            response = input(str("Gostaria de realizar a consulta novamente? [S/N]? ")).lower()
            print("\n")
            if response == 's':
                flag = True
            else:
                cursor.close()
                db_connection.commit()
                menu()  

        if choose == "6":
            responsavel = input(str("Digite o responsável que está procurando: ")).title()
            sql = ("SELECT * from Pacientes WHERE Responsável ='%s'") % (responsavel)
            cursor.execute(sql)
                        
            for (responsavel) in cursor:
                print("\nApresentando dados solicitados:")
                lista = ['ID','Nome','E-mail','Telefone','Data de Atendimento','Procedimento','Responsável']
                print(lista)
                print(responsavel)
            print("\n")

            response = input(str("Gostaria de realizar a consulta novamente? [S/N]? ")).lower()
            print("\n")
            if response == 's':
                flag = True
            else:
                cursor.close()
                db_connection.commit()
                menu()                

def update():
    flag = True
    # Loop para realização de mais de uma correção
    while True:
        cursor = db_connection.cursor()
        print("1 - Nome")
        print("2 - E-mail")
        print("3 - Telefone")
        choose = input(str("Selecione o campo para alteração: "))
        if choose == "1":
            cpf = input(str("\nInforme o CPF do usuário: "))
            nome = input(str("Digite o nome corrigido: ")).title()
            # Update do nome utilizando o CPF como primary key
            sql = ("update Pacientes set Nome = '%s' where cpf='%s'") % (nome, cpf)
            cursor.execute(sql)
            # Realizando um select para comprovar a alteração do campo
            sql = ("SELECT Nome from Pacientes WHERE Nome ='%s'") % (nome)
            cursor.execute(sql)
            for (nome) in cursor:
                print("\nNome alterado com sucesso:", nome ,"\n")
            # Confirmação se o usuário gostaria de corrigir outro campo
            response = input(str("Gostaria de corrigir algum outro campo? [S/N]? ")).lower()
            print("\n")
            if response == 's':
                flag = True
            else:
                cursor.close()
                db_connection.commit()
                menu()

        if choose == "2":
            cpf = input(str("\nInforme o CPF do usuário: "))
            email = input(str("Digite o email corrigido: ")).lower()
            # Update do e-mail utilizando o CPF como primary key
            sql = ("update Pacientes set Email = '%s' where cpf='%s'") % (email, cpf)
            cursor.execute(sql)
            # Realizando um select para comprovar a alteração do campo
            sql = ("SELECT Email from Pacientes WHERE Email ='%s'") % (email)
            cursor.execute(sql)
            for (nome) in cursor:
                print("\nE-mail alterado com sucesso:", email ,"\n")
            # Confirmação se o usuário gostaria de corrigir outro campo
            response = input(str("Gostaria de corrigir algum outro campo? [S/N]? ")).lower()
            print("\n")
            if response == 's':
                flag = True
            else:
                cursor.close()
                db_connection.commit()
                menu()

        if choose == "3":
            cpf = input(str("\nInforme o CPF do usuário: "))
            telefone = input(str("Digite o telefone corrigido: "))
            # Update do e-mail utilizando o CPF como primary key
            sql = ("update Pacientes set Telefone = '%s' where cpf='%s'") % (telefone, cpf)
            cursor.execute(sql)
            # Realizando um select para comprovar a alteração do campo
            sql = ("SELECT Telefone from Pacientes WHERE Telefone ='%s'") % (telefone)
            cursor.execute(sql)
            for (nome) in cursor:
                print("\nTelefone alterado com sucesso:", telefone ,"\n")
            # Confirmação se o usuário gostaria de corrigir outro campo
            response = input(str("Gostaria de corrigir algum outro campo? [S/N]? ")).lower()
            print("\n")
            if response == 's':
                flag = True
            else:
                cursor.close()
                db_connection.commit()
                menu()


menu()