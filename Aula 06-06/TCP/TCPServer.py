from socket import * 

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM) #Socket para estabelecer conexão com o cliente
serverSocket.bind(("",serverPort))

serverSocket.listen(1) #Somente um cliente por vez pode se conectar


print('Servidor está pronto para receber conexão :)')

while 1:
    connectionSocket, addr = serverSocket.accept() #Socket criado para troca de dados com o cliente
    sentence = connectionSocket.recv(1024) #Recebendo Senteça enviada pelo cliente
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()