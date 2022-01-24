import socket 
import threading 
   
def workerThread(s):
    while True: 
        client_time = s.recv(1024)
        if not client_time: break
        print('O cliente enviou: ', client_time.decode())
        try:
           s.send(client_time)
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
        print('Cliente Conectado:', addr[0], ':', addr[1])  
        tw = threading.Thread(target=workerThread, args=[s])
        tw.start()

if __name__ == '__main__': 
    Main() 