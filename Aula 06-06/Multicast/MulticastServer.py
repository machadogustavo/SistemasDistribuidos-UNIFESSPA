import threading
import socket

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        #Tentar nova conexão
        server.bind(("",7777))

    except:
        return
    
    while True:
        #Laço para aceitar novas conexões

def messageModified(client):

def broadcast(msg, client):

def deleteClient(cliente):


main()