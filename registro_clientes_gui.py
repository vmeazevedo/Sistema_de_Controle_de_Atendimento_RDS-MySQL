import mysql.connector
from mysql.connector import errorcode
from mysql.connector import cursor
from PyQt5 import uic, QtWidgets

###############################################################################################################
# Conexão da instância RDS - Amazon Web Service
###############################################################################################################
# Preencher os campos de conexão abaixo
host = 'localhost'      # Endpoint da instância RDS na cloud da AWS
user = 'root'           # Username criado na hora de realizar a instância RDS
password = ''           # Password criado na hora de realizar a instância RDS

try:
	db_connection = mysql.connector.connect(host = host, user = user, password = password)
	print("\nConexão com a base de dados realizada!\n")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("\nA base de dados não existe.")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("\nUsername ou o password está errado.")
	else:
		print(error)

cursor = db_connection.cursor()
# Criando a database e a tabela
cursor.execute("CREATE DATABASE IF NOT EXISTS Registro")
cursor.execute("use Registro")
cursor.execute("CREATE TABLE IF NOT EXISTS Pacientes (ID int auto_increment, Nome varchar(50) not null, cpf varchar(50) not null, Email varchar(200) not null, Telefone varchar(20) not null, Data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, Procedimento varchar(255) not null, Responsável varchar(100) not null, primary key (id))")

###############################################################################################################

def apresentar_formulario():
    formulario.show()

def inserir_dados():
    # Inicializa a variavel do cursor
    cursor = db_connection.cursor()
    # Inicializa as variaveis de texto
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
    # Chama a segunda tela 
    segunda_tela.show()
    # Inicializa a variavel do cursor
    cursor = db_connection.cursor()
    # Query para apresentar todos os dados da base
    sql = ("SELECT * FROM Pacientes")
    cursor.execute(sql)
    # Salvando o resultado da query em uma variável
    dados_lidos = cursor.fetchall()
    # Informando o tamanho das linhas e colunas da base
    segunda_tela.tb_dados.setRowCount(len(dados_lidos))
    segunda_tela.tb_dados.setColumnCount(8)
    # Criando um header para a base
    # segunda_tela.tb_dados.setItem(0,0, QtWidgets.QTableWidgetItem("ID"))
    # segunda_tela.tb_dados.setItem(0,1, QtWidgets.QTableWidgetItem("Nome"))
    # segunda_tela.tb_dados.setItem(0,2, QtWidgets.QTableWidgetItem("CPF"))
    # segunda_tela.tb_dados.setItem(0,3, QtWidgets.QTableWidgetItem("E-mail"))
    # segunda_tela.tb_dados.setItem(0,4, QtWidgets.QTableWidgetItem("Telefone"))
    # segunda_tela.tb_dados.setItem(0,5, QtWidgets.QTableWidgetItem("Data"))
    # segunda_tela.tb_dados.setItem(0,6, QtWidgets.QTableWidgetItem("Procedimento"))
    # segunda_tela.tb_dados.setItem(0,7, QtWidgets.QTableWidgetItem("Responsável"))
    # Realizando um loop para preencher os campos da tabela com os valores da base de dados
    for i in range(0, len(dados_lidos)):
        for j in range(0,8):
            segunda_tela.tb_dados.setItem(i,j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def apresentar_pesquisar():
    pesquisar_item.show()

def busca_por_item():
    resultado_por_item.show()
    cursor = db_connection.cursor()
    if pesquisar_item.sl_nome.isChecked():
        nome = pesquisar_item.campo_1.text().title()
        # Query para apresentar os dados pesquisados
        sql = ("SELECT * from Pacientes WHERE Nome ='%s'") % (str(nome))
        cursor.execute(sql)
        # Salvando o resultado da query em uma variável
        dados_lidos = cursor.fetchall()
        
        # Informando o tamanho das linhas e colunas da base
        resultado_por_item.tb_dados.setRowCount(len(dados_lidos))
        resultado_por_item.tb_dados.setColumnCount(8)
        # Realizando um loop para preencher os campos da tabela com os valores da base de dados         
        for i in range(0, len(dados_lidos)):
            for j in range(0,8):
                resultado_por_item.tb_dados.setItem(i,j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        
        pesquisar_item.campo_1.setText("")

        

    elif pesquisar_item.sl_cpf.isChecked():
        print("nome")
    elif pesquisar_item.sl_email.isChecked():
        print("nome")
    elif pesquisar_item.sl_telefone.isChecked():
        print("nome")
    elif pesquisar_item.sl_procedimento.isChecked():
        print("nome")
    elif pesquisar_item.sl_responsavel.isChecked():
        print("nome")


app=QtWidgets.QApplication([])

# Load das telas criadas
tela_inicial=uic.loadUi("tela_inicial.ui")
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("consulta_base.ui")
pesquisar_item=uic.loadUi("busca_item.ui")
resultado_por_item=uic.loadUi("pesquisa_por_item.ui")

# Botões das telas
tela_inicial.botao_cadastro.clicked.connect(apresentar_formulario)
formulario.botao_inserir.clicked.connect(inserir_dados)
tela_inicial.botao_consulta.clicked.connect(consultar_base)
tela_inicial.botao_pesquisa.clicked.connect(apresentar_pesquisar)
pesquisar_item.botao_buscar.clicked.connect(busca_por_item)
tela_inicial.show()
app.exec()

