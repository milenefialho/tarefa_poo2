import sys
import socket
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from CADASTRO import Tela_Cadastro
from CADUSUARIO import Tela_CadastroU
from CADASTRARQUARTO import Tela_CadastroQuarto
from CANCELARRESERVA import Tela_CancelarReserva
from LOGIN import Tela_Login
from RESERVARQUARTO import Tela_ReservarQuarto
from TELAINICIALGERENTE import Tela_InicialGerente
from VERQUARTO import Tela_VerQuarto
from VERRESERVAS import Tela_VerReserva




class Ui_Main(QtWidgets.QWidget):
    """
    Classe responsavel por definir a interface grafica principal da aplicacao
    
    Essa classe ira tratar da interface grafica em si e tambem criar todas as aplicacoes que sera necessaria para a execucao do programa

    Methods
    -------
    setupUi(Main)
        Configura a interface grafica da janela principal
    """
    
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)
        
        self.QtStack = QtWidgets.QStackedLayout()
        
        self.stack0=QtWidgets.QMainWindow()
        self.stack1=QtWidgets.QMainWindow()
        self.stack2=QtWidgets.QMainWindow()
        self.stack3=QtWidgets.QMainWindow() 
        self.stack4=QtWidgets.QMainWindow()
        self.stack5=QtWidgets.QMainWindow()
        self.stack6=QtWidgets.QMainWindow()
        self.stack7=QtWidgets.QMainWindow()
        self.stack8=QtWidgets.QMainWindow()
        
        
        self.Login = Tela_Login()
        self.Login.setupUi(self.stack0)
        
        self.TelaInicialGerente = Tela_InicialGerente()
        self.TelaInicialGerente.setupUi(self.stack1)
        
        self.CadUsuario = Tela_Cadastro()
        self.CadUsuario.setupUi(self.stack2)
        
        self.CadQuarto = Tela_CadastroQuarto()
        self.CadQuarto.setupUi(self.stack3)
        
        self.VerQuarto = Tela_VerQuarto()
        self.VerQuarto.setupUi(self.stack4)
        
        self.ReservarQuarto = Tela_ReservarQuarto()
        self.ReservarQuarto.setupUi(self.stack5)
        
        self.VerReserva = Tela_VerReserva()
        self.VerReserva.setupUi(self.stack6)
        
        self.CancelarRerseva = Tela_CancelarReserva()
        self.CancelarRerseva.setupUi(self.stack7)
        
        self.CadUsuarioU = Tela_CadastroU()
        self.CadUsuarioU.setupUi(self.stack8)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3) 
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        
        
class Main(QMainWindow,Ui_Main):
    """
    Classe principal que define a janela principal da aplicacao
    
    Essa classe ira contem todas as funcoes necessarias para executar cada aplicacao do sistema
    
    Attributes
    ----------
    parent : object
        Inicializa a janela principal e configura a interface grafica

    Methods
    -------
    abrirTelaCadastra()
        Altera a pagina atual para a tela de cadastro de usuario
    VoltarLogin()
        Altera a pagina atual para a tela de login
    VoltarInicialGerente()
        Altera a pagina atual para a tela inicial do administrador
    telaCadastrarQ()
        Altera a pagina atual para a tela de cadastro de quartos
    CadastrarQuarto()
        Executa a ação de cadastrar um quarto
    cadastraUnico()
        Redireciona para a tela de cadastro de usuario unico
    cadastraUnicoU()
        Redireciona para a tela de cadastro de usuario unico
    realizarReserva()
        Redireciona para a tela de realizacao de reserva
    visualizarQuarto()
        Redireciona para a tela de visualizacao dos quartos
    verTelaReserva()
        Redireciona para a tela de visualizacao das reservas
    cancelarReserva()
        Redireciona para a tela de cancelamento de reserva
    abrirTelaSair()
        Fecha a aplicacao
    fazercadastro()
        Executa a acao de cadastro de um usuario
    login()
        Executa a acao de login de um usuario
    fazerReserva()
        Executa a ação de realizacao de reserva de quarto
    fazercadastroU()
        Executa a acao de cadastro de um usuario unico
    deleteReserva()
        Executa a acao de exclusao de reserva
    conexao()
        Estabelece a conexao com o servidor
    enviarDados(dados)
        Envia uma string para o servidor
    recebeDados()
        Recebe os dados do servidor e retorna uma lista
    """
    
    def __init__(self, parent = None):
        """
        Parameters
        ----------
        parent : object
            Inicializa a janela principal e configura a interface grafica
        """
        super(Main,self). __init__(parent)
        self.setupUi(self)
        
        self.inserido = []
        
        self.aux = 1
        
        self.id_usuario = None
        self.socket = self.conexao()
        
        self.Login.pushButton.clicked.connect(self.login)
        self.Login.pushButton_2.clicked.connect(self.abrirTelaCadastra)
        
        
        
        self.TelaInicialGerente.pushButton_2.clicked.connect(self.cadastraUnicoU)
        self.TelaInicialGerente.pushButton_3.clicked.connect(self.telaCadastrarQ)
        self.TelaInicialGerente.pushButton_8.clicked.connect(self.realizarReserva)
        self.TelaInicialGerente.pushButton_4.clicked.connect(self.verTelaReserva)
        self.TelaInicialGerente.pushButton_5.clicked.connect(self.cancelarReserva)
        self.TelaInicialGerente.pushButton_6.clicked.connect(self.abrirTelaSair)
        self.TelaInicialGerente.pushButton_7.clicked.connect(self.VoltarLogin)
        self.TelaInicialGerente.pushButton_9.clicked.connect(self.visualizarQuarto)
        
        
        self.ReservarQuarto.pushButton.clicked.connect(self.fazerReserva)
        self.ReservarQuarto.pushButton_2.clicked.connect(self.VoltarInicialGerente)
        
        self.VerQuarto.pushButton_2.clicked.connect(self.realizarReserva)
        self.VerQuarto.pushButton.clicked.connect(self.VoltarInicialGerente)
        
        self.CadQuarto.pushButton_2.clicked.connect(self.CadastrarQuarto)
        self.CadQuarto.pushButton.clicked.connect(self.VoltarInicialGerente)
        
        self.CancelarRerseva.pushButton.clicked.connect(self.deleteReserva)
        self.CancelarRerseva.pushButton_2.clicked.connect(self.VoltarInicialGerente)
        
            
    
        self.CadUsuario.pushButton_2.clicked.connect(self.fazercadastro)
        self.CadUsuario.pushButton_3.clicked.connect(self.VoltarLogin)
        
        self.VerReserva.pushButton.clicked.connect(self.VoltarInicialGerente)
        
        self.CadUsuarioU.pushButton_2.clicked.connect(self.fazercadastroU)
        self.CadUsuarioU.pushButton_3.clicked.connect(self.VoltarInicialGerente)
    
    def abrirTelaCadastra(self):
        """
        Altera a pagina atual para a tela de cadastro de usuario
        
        ...
        """
        self.QtStack.setCurrentIndex(2) 

    def VoltarLogin(self):
        """
        Altera a pagina atual para a tela de login
        
        ...
        """
        self.QtStack.setCurrentIndex(0)
        
        
    def VoltarInicialGerente(self):
        """
        Altera a pagina atual para a tela inicial do administrador
        
        ...
        """
        self.QtStack.setCurrentIndex(1)
        
    def telaCadastrarQ(self):
        """
        Altera a pagina atual para a tela de cadastro de quartos
        
        ...
        """
        self.QtStack.setCurrentIndex(3)
    
        
    def CadastrarQuarto(self):
        """
        Esse metodo e responsavel por executa a ação de cadastrar um quarto
        
        Ele ira criar uma tela na qual o administrador podera cadastrar um quarto no sistema
        """
        numQuarto = self.CadQuarto.lineEdit.text()
        descricao = self.CadQuarto.lineEdit_2.text()
        valor = self.CadQuarto.lineEdit_3.text()
        if '' in [numQuarto,descricao,valor]:
            QMessageBox.information(None,'POOII','Preencha todas as informações!')
        else:
            dados = ('(3)-%s-%s-%s' %(numQuarto,descricao,valor))
            print(dados)
            print('tentando enviar os dados')
            self.enviarDados(dados)
            recebe = self.recebeDados()
            if recebe[0] == '1' :
                QMessageBox.information(None,'POOII','Quarto Cadastrado com sucesso!')
                self.CadQuarto.lineEdit.setText('')
                self.CadQuarto.lineEdit_2.setText('')
                self.CadQuarto.lineEdit_3.setText('')
                print(recebe)
            else: 
                QMessageBox.information(None,'POOII',recebe[1])
        
    def cadastraUnico(self):
        """
        Redireciona para a tela de cadastro de usuario (adm)
        
        ...
        """
        self.QtStack.setCurrentIndex(3)

    def cadastraUnicoU(self):
        """
        Redireciona para a tela de cadastro de usuario (hospede)
        
        ...
        """
        self.QtStack.setCurrentIndex(8)
        
    def realizarReserva(self):
        """
        Redireciona para a tela de realizacao de reserva
        
        ...
        """
        self.QtStack.setCurrentIndex(5)
    
    def visualizarQuarto(self):
        """
        Redireciona para a tela de visualizacao dos quartos
        
        Esse metodo e responsavel por mostrar uma tabela com informacoes dos quartos ja existentes no sistema

        """
        dados = '(7)'
        self.enviarDados(dados)
        recebe = self.recebeDados()
        self.VerQuarto.tableWidget.setRowCount(len(recebe)) #adicionar a quantidade de linha que a tabela vai ter antes de adicionar 
        linha = 0
        for quarto in recebe:
            aux = quarto.split(',')
            self.VerQuarto.tableWidget.setItem(linha,0,QtWidgets.QTableWidgetItem(aux[0]))
            self.VerQuarto.tableWidget.setItem(linha,1,QtWidgets.QTableWidgetItem(aux[1]))
           
            linha+=1
        self.QtStack.setCurrentIndex(4)
    
    def verTelaReserva(self):
        """
        Redireciona para a tela de visualizacao das reservas
        
        Esse metodo e responsavel por mostrar uma tabela com informacoes das reservas ja existentes no sistema
        """
        dados = '(6)'
        self.enviarDados(dados)
        recebe = self.recebeDados()
        self.VerReserva.tableWidget.setRowCount(len(recebe)) #adicionar a quantidade de linha que a tabela vai ter antes de adicionar 
        linha = 0
        for reserva in recebe:
            aux = reserva.split(',') 
            self.VerReserva.tableWidget.setItem(linha,0,QtWidgets.QTableWidgetItem(aux[0]))
            self.VerReserva.tableWidget.setItem(linha,1,QtWidgets.QTableWidgetItem(aux[1]))
            self.VerReserva.tableWidget.setItem(linha,2,QtWidgets.QTableWidgetItem(aux[2]))
            linha+=1
        self.QtStack.setCurrentIndex(6)
    
    def cancelarReserva(self):
        """
        Redireciona para a tela de cancelamento de reserva
        
        ...
        """
        self.QtStack.setCurrentIndex(7)
            
    
            
    def abrirTelaSair(self):
        """
        Fecha a aplicacao
        
        Esse metodo e responsavel por encerrar a execucao do programa quando desejado  
        """
        return exit()
    
    def fazercadastro(self):
        """
        Executa a acao de cadastro de um usuario
        
        Esse metodo e responsavel por realizar o cadastrado do usuario(administrador ou hospede) no banco de dados 
        """
        nome = self.CadUsuario.lineEdit_3.text()
        cpf =  self.CadUsuario.lineEdit_4.text()
        data_nas = self.CadUsuario.dateEdit.text()
        cidade = self.CadUsuario.lineEdit_2.text()
        estado = self.CadUsuario.lineEdit_5.text()
        usuario = self.CadUsuario.lineEdit_6.text()
        senha = self.CadUsuario.lineEdit_7.text()
        
        dados = ('(1)-%s-%s-%s-%s-%s-%s-%s' %(nome,cpf,data_nas,cidade,estado,usuario,senha))
        self.enviarDados(dados)
        recebe = self.recebeDados()
        if recebe[0] == '0':
            mensagem = recebe[1]
            QMessageBox.information(None,'POOII',mensagem)
        else:
            QMessageBox.information(None,'POOII','Cadastro realizado com sucesso!')
            self.CadUsuario.lineEdit_3.setText('')
            self.CadUsuario.lineEdit_4.setText('')
            self.CadUsuario.lineEdit_2.setText('')
            self.CadUsuario.lineEdit_5.setText('')
            self.CadUsuario.lineEdit_6.setText('')
            self.CadUsuario.lineEdit_7.setText('')
            self.VoltarInicialGerente()
        
    def login(self):
        """
        Executa a acao de login de um usuario
        
        Esse metodo e responsavel por realizar o login do usuario(administrador) paea que o mesmo possa ter acesso ao sistema e seus servicos 
        """
        usuario = self.Login.lineEdit.text()
        senha = self.Login.lineEdit_2.text()
        
        dados = ('(2)-%s-%s' %(usuario,senha))
        self.enviarDados(dados)
        recebe = self.recebeDados()
        if recebe[0]== '1':
            self.id_usuario = recebe[2]
            QMessageBox.information(None,'POOII','Login efetuado com sucesso!')
            self.Login.lineEdit.setText('')
            self.Login.lineEdit_2.setText('')
            self.QtStack.setCurrentIndex(1)
        else:
            mensagem = recebe[1]
            QMessageBox.information(None,'POOII',mensagem)

          
        
    def fazerReserva(self):
        """
        Executa a ação de realizacao de reserva de quarto
        
        Esse metodo e responsavel por realizar uma reserva de um quarto que ja esta cadastrado no sistema
        """
        cpf = self.ReservarQuarto.lineEdit_2.text()
        numero_quarto = self.ReservarQuarto.lineEdit.text()
        atual = datetime.now()
        data = atual.strftime('%d/%m/%Y')
        if '' in [cpf,numero_quarto,data]:
            QMessageBox.information(None,'POOII','Preencha todas as informações!')
        else:
            dados = ('(4)-%s-%s-%s' %(cpf,numero_quarto,data))
            self.enviarDados(dados)
            recebe = self.recebeDados()
            if recebe[0]=='0':
                mensagem = recebe[1]
                QMessageBox.information(None,'POOII',mensagem)
            else:
                QMessageBox.information(None,'POOII','Reserva realizada com sucesso!')
                self.ReservarQuarto.lineEdit_2.setText('')
                self.ReservarQuarto.lineEdit.setText('')
                
            
        
    def fazercadastroU(self):
        """
        Executa a acao de cadastro de um usuario
        
        Essa metodo e responsavel por realizar o cadastro do usuario no sistema, tanto o administrador como o hospede
        """
        nome = self.CadUsuarioU.lineEdit_3.text()
        cpf =  self.CadUsuarioU.lineEdit_4.text()
        data_nas = self.CadUsuarioU.dateEdit.text()
        cidade = self.CadUsuarioU.lineEdit_2.text()
        estado = self.CadUsuarioU.lineEdit_5.text()
            
        dados = ('(5)-%s-%s-%s-%s-%s' %(nome,cpf,data_nas,cidade,estado))
        print(dados)
        self.enviarDados(dados)
        recebe = self.recebeDados()
        if recebe[0]=='1':
            QMessageBox.information(None,'POOII','Usuário cadastrado com sucesso!')
            self.CadUsuarioU.lineEdit_3.setText('')
            self.CadUsuarioU.lineEdit_4.setText('')
            self.CadUsuarioU.lineEdit_2.setText('')
            self.CadUsuarioU.lineEdit_5.setText('')
            self.VoltarInicialGerente()
        else:
            mensagem = recebe[1]
            QMessageBox.information(None,'POOII',mensagem)
            
    def deleteReserva(self):
        """
        Executa a acao de exclusao de reserva
        
        Esse metodo e responsavel por excluir uma reserva ja existente no banco de dados
        """
        numero = self.CancelarRerseva.lineEdit.text()
        if '' in [numero]:
            QMessageBox.information(None,'POOII','O campo tem que ser preenchido!')
        else:
            dados = ('(8)-%s'%(numero))
            print(dados)
            self.enviarDados(dados)
            recebe = self.recebeDados()
            if recebe[0] == '1':
                QMessageBox.information(None,'POOII','Reserva deletada com sucesso!')
                self.CancelarRerseva.lineEdit.setText('')
            else:
                QMessageBox.information(None,'POOII','Reserva não existente!')
    
        
            
    #ele cria a conexao de um socket(prover a comunicacao de duas portas)
    def conexao(self):
        """
        Estabelece a conexao com o servidor  antes de iniciar a comunicacao
        
        Esse metodo e responsavel por criar o socket que sera usado para a comunicacao com o servidor
        
        Returns
        -------
        object
            Retorna o objeto de socket criado
        
        
        """
        ip = '10.180.43.191'
        port = 9092
        addr = ((ip,port))
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect(addr)
        return cliente_socket
    
    
    def enviarDados(self,dados):
        """ Metodo para envia dados ao cliente
        
        Esse metodo envia um dado ao cliente em formato de string
        
        Parameters
        ----------
        dados : str
            Serao os dados a serem enviados
        """
        self.socket.send(dados.encode()) 

    def recebeDados(self):
        """ Metodo para recebe dados do cliente
        
        Esse metodo recebe um dado do cliente, em seguida converter a string recebida em uma lista 
        
        Returns
        ------
        list
            Ele retorna uma lista de contendo os dados
        """
        dadosRec = self.socket.recv(1024).decode()
        dados = dadosRec.split('-')
        return dados 
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())