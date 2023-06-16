from socket import * #Importando módulo socket

serverName = 'localhost' #Endereçamento Servidor

serverPort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM) #Primeira determina IPV4 e outro Protocolo TCP

clientSocket.connect((serverName,serverPort)) #Estabelecendo conexão ao servidor, Endereço+Porta

sentence = input('Input lowercase sentence: ') #Mensagem a ser enviada
sentenceBytes = sentence.encode("utf-8") #Convertendo mensagem para Bytes

clientSocket.send(sentenceBytes) #Enviado sentença convertida

modifiedSentence = clientSocket.recv(1024) #Resposta do servidor

print('From Server: ', modifiedSentence) #Printando resposta

clientSocket.close() #Encerrando conexão por parte do cliente

