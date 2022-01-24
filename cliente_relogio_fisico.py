import socket
from random import randint
from datetime import datetime, timedelta

def Main():
    host = '127.0.0.1'
    port = 2802
    
    random_seconds = randint(30, 120)
    now = datetime.now() - timedelta(seconds=random_seconds)
    current_time = now.strftime("%H:%M:%S")
    
    print("Segundos descontados para gerar atraso: ", random_seconds)
    print("Horário setado no cliente: ", current_time)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (host, port) 

    client_socket.settimeout(5)
    client_socket.connect(dest)

    client_socket.send(current_time.encode('ascii'))

    try:
        resposta, servidor = client_socket.recvfrom(1024)
        print('Resposta do Servidor: ', resposta.decode())
    except: 
        print('Ocorreu um erro...')

    client_socket.close() #Fecha a conexão com o servidor

if __name__ == '__main__': 
	Main()