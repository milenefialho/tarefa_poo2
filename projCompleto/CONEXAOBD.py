
import mysql.connector as mysql

class Conexaobd():
    """
    Classe responsavel por fazer a conexao entre o cliente e o servidor 
    
    Essa classe encapsula a funcionalidade de conexao e execucao de comandos no banco de dados MySQL, fornecendo metodos para conectar, desconectar e executar consultas e insercoes.
    
    Attributes
    ----------
    host : str
        O endereco do host do banco de dados (por padrao, 'localhost')
    database : str
        O nome da base de dados 
    user : str
        O nome de usuário para autenticação no banco de dados (por padrao, 'root')
    passwd : str
        Senha para acessar o banco de dados
    conexao : object
        Usado para estabelecer a conexao com o banco de dados
    cursor : object
        Usado para executar comandos SQL
        
    Methods
    -------
    conecta()
        Estabelece a conexao com o banco de dados usando as informacoes fornecidas nos atributos. Cria um objeto de conexao e um objeto de cursor
    desconecta()
        Encerra a conexao com o banco de dados e realiza o commit das transacoes pendentes
    executaSELECT(sql)
        Executa uma consulta SELECT no banco de dados usando o comando SQL(faz uma selecao)
    executaINSERT(sql)
        Executa uma operacao de insercao no banco de dados usando o comando SQL(faz uma insercao)
          
    """
    
    def __init__(self,host = 'localhost',database = 'oasis_hotel',user ='root', passwd = 'Mile#123'):
        """
        Parameters
        ----------
        host : str
        database : str
        user : str
        passwd : str
        conexao : object
        cursor : object
        """
        
        self.host = host
        self.user = user
        self.pwd = passwd
        self.db = database
        self.conexao = None
        self.cursor = None
        
    
    def conecta(self):
        """ 
        Estabelecer a conexao com o banco de dados
        
        Esse metodo e responsavel por estabelecer a conexao com o banco de dados usando as informacoes fornecidas nos atributos.
        
        """
        self.conexao = mysql.connect(host = self.host, database=self.db, user=self.user, password=self.pwd)
		# self.conexao = sqlite3.connect(self.db)
        self.cursor = self.conexao.cursor()
       
         
    def desconecta(self):
        """
        Encerra a conexao com o banco de dados 
        
        Esse metodo e responsavel por encerrar a conexao com o banco de dados e realiza o commit das transacoes pendentes
        """
        self.conexao.commit()
        self.conexao.close()
        
    def executaSELECT(self,sql):
        """
        Usado para fazer uma selecao especifica dentro do banco(buscar)
        
        Esse metodo e responsavel por executa uma consulta SELECT no banco de dados usando o comando SQL(faz uma selecao)
        
        Parameters
        ----------
        sql : str
            Variavel que representa o comando SQL que ele vai executar 

        
        Returns
        -------
        list 
            Ele retorna uma lista com os resultados da consulta
        """
        self.conecta()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.desconecta()
        return resultado


    def executaINSERT(self,sql):
        """
        Usado para inserir elementos no banco de dados 
        
        Esse metodo e responsavel por executa uma operação de inserção no banco de dados usando o comando SQL(faz uma insercao)
        
        Parameters
        ----------
        sql : str
            Variavel que representa o comando SQL que ele vai executar 
            
        """
        self.conecta()
        try:
            self.cursor.execute(sql)
            self.conexao.commit()
            self.conexao.close()
        except:
            print("Erro!")
            self.desconecta()