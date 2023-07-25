from serMulthread import SerMulthread
import socket
import sys


class Servidor():
    """
    Classe responsavel por iniciar o servidor e lidar com as conexoes com o cliente
    
    Essa classe ira iniciar o servidor na qual esse servidor sempre ficara esperando uma comunicao por parte do cliente 
    
    Methods
    -------
    run()
        Esse metodo configura o servidor, aguarda novas conexões e cria uma nova thread para cada cliente conectado
    """
    
    def __init__(self):
        self.run()
        
    def run(self):
        """
        Metodo responsavel por executar toda as funcionalidade do servidor
        
        Esse metodo configura o servidor, aguarda novas conexões e cria uma nova thread para cada cliente conectado.
        """
       
        host = '0.0.0.0'
        port = 9092
        addr = (host, port)
        serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #ligar o socket no endereco passado
        serv_socket.bind(addr)
        print('servidor iniciado')
        print('aguardando nova conexao...')
        while True:
            # o sockte esta aguardando o usuario enviar informacoes
            serv_socket.listen(1)
            '''quando cliente se conectar as informacoes do socket e do endereco do
             cliente sao enviadas para o servidor multhread'''
             
            clientsock, clienteAddress = serv_socket.accept() 
            print('conectado')
            """ Ta criando uma nova thread """
            newthread = SerMulthread(clienteAddress,clientsock)
            """ Depois que a thread e criada chama o start(executar o run do arquivo serMulthread) """
            newthread.start()
        
if __name__ == '__main__':
    servidor = Servidor()
    sys.exit()
