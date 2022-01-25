import socket
import threading
from time import sleep
from random import randint
from datetime import datetime
   
def workerThread(socket):
    while True: 
        t0 = socket.recv(1024)
        
        now = datetime.now()
        t1 = now.strftime("%H:%M:%S")
        
        t0 = t0.decode()
        if not t0: break
        print('O cliente enviou: ', t0)
        
        sleep(randint(5, 10))
        
        now = datetime.now()
        t2 = now.strftime("%H:%M:%S")
        
        print(f'T0: {t0} T1: {t1} T2: {t2}')
        
        horarios = f'{t0}, {t1}, {t2}'
        
        try:
            socket.send(horarios.encode('ascii'))
        except:
            print('Erro ao responder.')
    socket.close() 
  
def Main(): 
    host = "" 
    porta = 2802

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    servidor_socket.bind((host, porta)) 
    servidor_socket.listen() 
  
    print("Servidor inicializado na porta " + str(porta))

    while True: 
        s, addr = servidor_socket.accept() 
        print('\nCliente Conectado:', addr[0], ':', addr[1])  
        tw = threading.Thread(target=workerThread, args=[s])
        tw.start()

if __name__ == '__main__': 
    Main() 