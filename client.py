#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

try:
    METHOD = sys.argv[1]
    SIPNAME_SERVER = sys.argv[2].split('@')[0]
    ip_server = sys.argv[2].split('@')[1]
    IP_SERVER = ip_server.split(':')[0]
    PUERTO_SERVER = int(ip_server.split(':')[1])
    
except IndexError:
    sys.exit("Usage: client.py ip metodo receptor@IPreceptor:puertoSIP")
# Contenido que vamos a enviar
LINE = METHOD + " sip:" + SIPNAME_SERVER + "@" + IP_SERVER + " SIP/2.0\r\n"

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((IP_SERVER, PUERTO_SERVER))

    print("Enviando: " + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

    print('Recibido -- ', data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
