import mysql.connector
from mysql.connector import errorcode
from mysql.connector import cursor

# No MySQL Workbench criar uma conexão e após isso realizar a criação da base e das tabelas
'''
create database Registro;
use Registro;
CREATE TABLE Pacientes (
  ID int auto_increment,
  Nome varchar(50) not null,
  cpf varchar(50) not null,
  Email varchar(200) not null,
  Telefone varchar(20) not null,
  Endereço varchar(100) not null,
  Data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  Procedimento varchar(255) not null,
  Responsável varchar(100) not null,
  primary key (id)
  ) engine=innodb;
'''

###############################################################################################################
# CONEXÃO 
###############################################################################################################
try:
	db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='Registro')
	print("\nDatabase connection made!\n")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("\nDatabase doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("\nUser name or password is wrong")
	else:
		print(error)
###############################################################################################################

def menu():
    print("====================================")
    print("         Sistema de Controle        ")
    print("====================================\n")

    print("Menu:")
    print("1 - Inserir dados")
    print("2 - Consultar dados")
    print("3 - Consulta por item")
    print("4 - Alterar dados cadastrais\n")
    flag = True
    while True:
        choose = input(str("Indique a operação desejada: "))
        if choose == "1":
            print("Inserção de dados selecionado.\n")
            inserir()
        elif choose == "2":
            print("Consulta da base selecionada.\n")
            consulta_base()
        elif choose == "3":
            print("Consulta por item selecionada.\n")
            consulta_item()
        elif choose == "4":
            print("Atualização de dados selecionado.\n")
            update()
        else:
            print("AVISO: Digite somente o número de uma das opções apresentados.\n")

def inserir():
    # Declaração de variável
    cursor = db_connection.cursor()
    
    flag = True
    while True:
        # input manual dentro do INSERT
        Nome = input(str("Nome: "))
        cpf = input(str("CPF: "))
        Email = input(str("E-mail: "))
        Telefone = input(str("Tel: "))
        Endereço = input(str("Endereço: "))
        Procedimento = input(str("Procedimento: "))
        Responsável = input(str("Responsável: "))

        sql = "INSERT INTO Pacientes (Nome, CPF, Email, Telefone, Endereço, Procedimento, Responsável) VALUES ('%s', '%s', '%s','%s', '%s', '%s', '%s')" % (Nome, cpf, Email, Telefone, Endereço,Procedimento, Responsável)
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
        sql = ("SELECT ID, Nome, CPF, Email, Telefone, Endereço, Procedimento, Responsável FROM Pacientes")
        cursor.execute(sql)
        for (ID, Nome, cpf, Email, Telefone, Endereço, Procedimento, Responsável) in cursor:
            print(ID, Nome, cpf, Email, Telefone, Endereço, Procedimento, Responsável)
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

def consulta_item():
    flag = True
    while True:
        cursor = db_connection.cursor()
        print("1 - Nome")
        print("2 - CPF")
        print("3 - E-mail")
        print("4 - Telefone")
        print("5 - Endereço")
        print("6 - Procedimento")
        print("7 - Responsável")
        choose = input(str("Selecione o tipo de consulta, exemplo(Consulta por Nome): "))
        if choose == "1":
            nome = input(str("Digite o nome que está procurando: "))
            sql = ("SELECT * from Pacientes WHERE Nome ='%s'") % (nome)
            cursor.execute(sql)
                        
            for (Nome) in cursor:
                print("\nApresentando dados solicitados:")
                lista = ['ID','Nome','E-mail','Telefone','Endereço','Data de Atendimento','Procedimento','Responsável']
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
                lista = ['ID','Nome','E-mail','Telefone','Endereço','Data de Atendimento','Procedimento','Responsável']
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
            email = input(str("Digite o E-mail que está procurando: "))
            sql = ("SELECT * from Pacientes WHERE email ='%s'") % (email)
            cursor.execute(sql)
                        
            for (email) in cursor:
                print("\nApresentando dados solicitados:")
                lista = ['ID','Nome','E-mail','Telefone','Endereço','Data de Atendimento','Procedimento','Responsável']
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



def update():
    flag = True
    while True:
        cursor = db_connection.cursor()
        print("1 - Nome")
        print("2 - CPF")
        print("3 - E-mail")
        print("4 - Telefone")
        print("5 - Endereço")
        print("6 - Procedimento")
        print("7 - Responsável")
        choose = input(str("Selecione o campo para alteração: "))
        if choose == "1":
            cpf = input(str("Informe o CPF: "))
            nome = input(str("Digite o novo nome: "))
            sql = ("update Pacientes set Nome = '%s' where cpf='%s'") % (nome, cpf)
            cursor.execute(sql)
            cursor.close()
            db_connection.commit()

            response = input(str("Gostaria de adicionar mais um registro? [S/N]? ")).lower()
            print("\n")
            if response == 's':
                flag = True
            else:
                break
    menu()
        
        # sql = ("SELECT id, name, cpf FROM user")
        # cursor.execute(sql)
        # for (id, name, cpf) in cursor:
        #     print(id, name, cpf)
        # cursor.close()
        # db_connection.commit()

menu()