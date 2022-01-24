import socket
import threading
from time import sleep
from random import randint
from datetime import datetime
   
def workerThread(s):
    while True: 
        t0 = s.recv(1024)
        
        now = datetime.now()
        t1 = now.strftime("%H:%M:%S")
        
        t0 = t0.decode()
        if not t0: break
        print('O cliente enviou: ', t0)
        
        sleep(randint(5, 10))
        
        now = datetime.now()
        t2 = now.strftime("%H:%M:%S")
        
        print(f'T0: {t0} T1: {t1} T2: {t2}')
        
        times = f'{t0}, {t1}, {t2}'
        
        try:
            s.send(times.encode('ascii'))
        except:
            print('Erro ao responder.')
    s.close() 
  
def Main(): 
    host = "" 
    port = 2802

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind((host, port)) 
    server_socket.listen() 
  
    print("Servidor inicializado na porta " + str(port))

    while True: 
        s, addr = server_socket.accept() 
        print('\nCliente Conectado:', addr[0], ':', addr[1])  
        tw = threading.Thread(target=workerThread, args=[s])
        tw.start()

if __name__ == '__main__': 
    Main() 