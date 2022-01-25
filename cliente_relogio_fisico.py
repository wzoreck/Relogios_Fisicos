import socket
from random import randint
from datetime import datetime, timedelta
from time import sleep

def Main():
    host = '127.0.0.1'
    porta = 2802
    
    random_segundos = randint(30, 120)
    data_hora_atual = datetime.now() - timedelta(seconds=random_segundos)
    t0 = data_hora_atual.strftime("%H:%M:%S")
    
    print("Segundos descontados para gerar atraso: ", random_segundos)
    print("Horário setado no cliente (T0): ", t0)

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (host, porta) 

    cliente_socket.settimeout(20)
    cliente_socket.connect(dest)

    cliente_socket.send(t0.encode('ascii'))

    try:
        resposta, servidor = cliente_socket.recvfrom(1024)
        horarios = resposta.decode().split(", ")
        
        t3 = datetime.now() - timedelta(seconds=random_segundos)
        
        print('Resposta do Servidor [T0, T1, T2]: ', horarios)
        print(f'T3: {t3.strftime("%H:%M:%S")}')
        
        horarios_split = []
        for horario in horarios:
            horarios_split.append(horario.split(":"))
        
        ano = int(datetime.now().year)
        mes = int(datetime.now().month)
        dia = int(datetime.now().day)
        t0 = datetime(ano, mes, dia, int(horarios_split[0][0]), int(horarios_split[0][1]), int(horarios_split[0][2]))
        t1 = datetime(ano, mes, dia, int(horarios_split[1][0]), int(horarios_split[1][1]), int(horarios_split[1][2]))
        t2 = datetime(ano, mes, dia, int(horarios_split[2][0]), int(horarios_split[2][1]), int(horarios_split[2][2]))
        defasagem = ((t1 - t0) + (t2 - t3)) / 2
        print(f'Defasagem: {defasagem}')
        print(f'Horario atual ajustado: {(t3 + timedelta(seconds=defasagem.total_seconds())).strftime("%H:%M:%S")}')
    except: 
        print('Ocorreu um erro...')

    cliente_socket.close()

if __name__ == '__main__': 
    Main()