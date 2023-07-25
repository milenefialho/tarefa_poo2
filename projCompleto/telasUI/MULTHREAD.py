import socket
import sys
from CONEXAOBD import Conexaobd
import threading
import socket


class Multhread():
    
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.cAddress = clientAddress
        self.csocket = clientsocket
        self.sinc = threading.Lock()
        self.banco = Conexaobd()
	
    
        
        while True:
            try:
                info = cliente.recv(1024).decode()  # Recebi info do cliente
                editarInfo = list(info.split('-'))
                confirma=""
                if editarInfo[0] == '(1)':
                    consulta = ("SELECT * FROM Pessoa WHERE cpf = '%s';"%(editarInfo[2]))
                    pessoa = conexao.executaSELECT(consulta)
                    if pessoa == []:
                        consulta = ("INSERT INTO Pessoa (nome,cpf,data_nas,cidade,estado,usuario,senha) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(editarInfo[1],editarInfo[2],editarInfo[3],editarInfo[4],editarInfo[5],editarInfo[6],editarInfo[7]))
                        conexao.executaINSERT(consulta)
                        confirma = '1-Seja bem vindo!-'+editarInfo[2]
                    else:
                        confirma = '0-Já existe pessoa com esse CPF!'
                            
                elif editarInfo[0] == '(2)':
                    usuario = editarInfo[1]
                    senha = editarInfo[2]
                    consulta = f"select * from Pessoa where usuario = '{usuario}'"
                    resultUsuario = conexao.executaSELECT(consulta)
                    if resultUsuario != []: # Quer dizer que o usuario existe
                        if resultUsuario[0][7] == senha:
                            confirma = "1-Deu certo logar-" + str(resultUsuario[0][0])
                        else:
                            confirma = '0- Senha Incorreta' 
                    else:
                        confirma = "0- Não foi possivel Logar"
                elif editarInfo[0] == '(3)':
                    numQuarto = int(editarInfo[1])
                    descricao = editarInfo[2] 
                    valor = float(editarInfo[3])
                    consulta = f"select * from Quarto where numero = {numQuarto}"
                    resultQuarto = conexao.executaSELECT(consulta)
                    if resultQuarto == []:
                        consulta = ("INSERT INTO Quarto (numero,descricao,valor) VALUES (%d,'%s',%f)"%(numQuarto,descricao,valor))
                        print(consulta)
                        conexao.executaINSERT(consulta)
                        confirma = "1-Quarto cadastrado"
                    else:
                        confirma = "0-Existe quarto ja cadastrado"
                elif editarInfo[0]== '(4)':
                    cpf = editarInfo[1]
                    numero_quarto = int(editarInfo[2])
                    inicio_data = editarInfo[3]
                    consulta = f"select id from Usuario where cpf= '{cpf}'"
                    resultUse = conexao.executaSELECT(consulta)
                    if resultUse == []:
                        confirma = "0-Não existe pessoa cadastrada com esse CPF!"
                    else:
                        pessoa_id = int(resultUse[0][0])
                        consulta = f"select * from Reserva where numero_quarto = {numero_quarto}"
                        resultReserva = conexao.executaSELECT(consulta)
                        if resultReserva == []:
                            #vai ver se o quarto existe
                            consulta = f"select * from  Quarto where numero = {numero_quarto}"
                            resultQ = conexao.executaSELECT(consulta)
                            if resultQ != []:
                                consulta = ("INSERT INTO Reserva (cpf,numero_quarto,pessoa_id,inicio_data) VALUES ('%s',%d,%d,'%s')"%(cpf,numero_quarto,pessoa_id,inicio_data))
                                conexao.executaINSERT(consulta)
                                confirma = '1-Reserva realizada com sucesso!'
                            else:
                                confirma = '0-Esse quarto não existe!'
                        else:
                            confirma = '0-Esse quarto já estar reservado!'
                elif editarInfo[0] == '(5)':
                    consulta = ("SELECT * FROM Usuario WHERE cpf = '%s';"%(editarInfo[2]))
                    pessoa = conexao.executaSELECT(consulta)
                    if pessoa == []:
                        consulta = ("INSERT INTO Usuario (nome,cpf,data_nas,cidade,estado) VALUES ('%s','%s','%s','%s','%s')"%(editarInfo[1],editarInfo[2],editarInfo[3],editarInfo[4],editarInfo[5]))
                        conexao.executaINSERT(consulta)
                        confirma = 'Seja bem vindo!-' + editarInfo[2] 
                        confirma = '1-Usuário cadastrado com sucesso!'
                    else:
                        confirma = '0-Esse usuário já estar cadastrado!'
                elif editarInfo[0] == '(6)':
                    consulta = ("SELECT numero_quarto,cpf,inicio_data FROM Reserva")
                    resultverR = conexao.executaSELECT(consulta)
                    # O que vai para o cliente 
                    confirma = '' # vazio pq ainda vai entrar no for e sera formatado
                    cont = 1 #para nao pegar espaco vazio .. Questao de formatacao 
                    tam = len(resultverR)
                    for reserva in resultverR:
                        if cont == tam:
                            #formatR MINHA string para adicionar na tabela. vai fazer a separar 
                            # por virgula no cliente
                            confirma += f'{reserva[0]},{reserva[1]},{reserva[2]}'
                        else:
                            confirma += f'{reserva[0]},{reserva[1]},{reserva[2]}-'

                        cont+=1
                
                elif editarInfo[0] == '(7)':
                    consulta = ("SELECT numero,descricao FROM Quarto")
                    resultverQ = conexao.executaSELECT(consulta)
                    confirma = ''
                    cont = 1
                    tam = len(resultverQ)
                    for quarto in resultverQ:
                        if cont == tam: 
                            
                            confirma += f'{quarto[0]},{quarto[1]}'
                        else:
                            confirma += f'{quarto[0]},{quarto[1]}-'

                        cont+=1
                elif editarInfo[0]=='(8)':
                    num = int(editarInfo[1])
                    consulta = f"SELECT * FROM  Reserva WHERE numero_quarto = {num}"
                    resultC = conexao.executaSELECT(consulta)
                    if resultC != []:
                        consulta = f"DELETE FROM Reserva WHERE numero_quarto = {num}"
                        conexao.executaINSERT(consulta)
                        confirma = '1-Reserva deletado!'
                    else:
                        confirma = '0-Quarto inexistente!'
                        
                cliente.send(confirma.encode())  
            except:
                serv_socket.close()
                break		
            
		
    