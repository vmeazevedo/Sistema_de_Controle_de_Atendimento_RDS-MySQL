import mysql.connector
from mysql.connector import errorcode
from mysql.connector import cursor
from PyQt5 import uic, QtWidgets

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
        sql = ("SELECT CONCAT_WS('  ||  ',ID, Nome, CPF, Email, Telefone, Procedimento, Responsável) FROM Pacientes")
        cursor.execute(sql)
        for (x) in cursor:
            print(x)
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

def inserir_dados():
    cursor = db_connection.cursor()
    Nome = formulario.campo_1.text().title()
    cpf = formulario.campo_2.text()
    Email = formulario.campo_3.text().lower()
    Telefone = formulario.campo_4.text()
    Procedimento = formulario.campo_5.text().capitalize()
    Responsável = formulario.campo_6.text().title()

    # Realizando a inserção dos dados em nosso banco de dados
    sql = "INSERT INTO Pacientes (Nome, CPF, Email, Telefone, Procedimento, Responsável) VALUES ('%s', '%s','%s', '%s', '%s', '%s')" % (str(Nome), str(cpf), str(Email), str(Telefone), str(Procedimento), str(Responsável))
    cursor.execute(sql)
    db_connection.commit()
    print("\nDados inseridos com sucesso")

    # Reinicializando os campos para ficarem em branco
    formulario.campo_1.setText("")
    formulario.campo_2.setText("")
    formulario.campo_3.setText("")
    formulario.campo_4.setText("")
    formulario.campo_5.setText("")
    formulario.campo_6.setText("")

def consultar_base():
    segunda_tela.show()
    cursor = db_connection.cursor()
    # sql = ("SELECT CONCAT_WS('  ||  ',ID, Nome, CPF, Email, Telefone, Procedimento, Responsável) FROM Pacientes")
    sql = ("SELECT * FROM Pacientes")
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()
      

    segunda_tela.tb_dados.setRowCount(len(dados_lidos))
    segunda_tela.tb_dados.setColumnCount(7)

    segunda_tela.tb_dados.setItem(0,0, QtWidgets.QTableWidgetItem("ID"))
    segunda_tela.tb_dados.setItem(0,1, QtWidgets.QTableWidgetItem("Nome"))
    segunda_tela.tb_dados.setItem(0,2, QtWidgets.QTableWidgetItem("CPF"))
    segunda_tela.tb_dados.setItem(0,3, QtWidgets.QTableWidgetItem("E-mail"))
    segunda_tela.tb_dados.setItem(0,4, QtWidgets.QTableWidgetItem("Telefone"))
    segunda_tela.tb_dados.setItem(0,5, QtWidgets.QTableWidgetItem("Procedimento"))
    segunda_tela.tb_dados.setItem(0,6, QtWidgets.QTableWidgetItem("Responsável"))

    for i in range(1, len(dados_lidos)):
        for j in range(0,7):
            segunda_tela.tb_dados.setItem(i,j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("consulta_base.ui")
formulario.botao_inserir.clicked.connect(inserir_dados)
formulario.botao_consulta.clicked.connect(consultar_base)
formulario.show()
app.exec()

