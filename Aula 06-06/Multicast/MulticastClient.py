import threading
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost',7777))

    except:
        return print('\nNão foi possível se conectar ao servidor!\n')
    
    username = input('Usuário> ')
    print('\nConectado')

    threadOne = threading.Thread(target=receiveMessages, args=[client])
    threadTwo = threading.Thread(target=sendMessages, args=[client, username])

    threadOne.start()
    threadTwo.start()

    def receiveMessages(client):
        while True:
            try:
                msg = client.recv(2048).decode("utf-8")
            except:
                print('\nNão foi possível permanecer conectado no servidor\n')
                print('\npressione <ENTER> para continuar...')
                client.close()
            

    def sendMessages(client, username):
        while True:
            try:
                msg = input('\nDigite sua mensagem: ')
                client.send(f'<username> {msg}'.encode("utf-8"))
            except:
                return
        
main()