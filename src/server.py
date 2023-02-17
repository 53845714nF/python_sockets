#! /usr/bin/env python3

"""
Server that provides a TCP socket on localhost port 1337.
"""

from socket import socket, AF_INET, SOCK_STREAM
from os import getenv

HOST = getenv('HOST','127.0.0.1')
PORT = getenv('PORT', '1337')

with socket(AF_INET, SOCK_STREAM) as tcp_socket:
    tcp_socket.bind((HOST, int(PORT)))
    tcp_socket.listen()
    conn, addr = tcp_socket.accept()

    print(f'Connected by {addr}')
    print(f'{conn}')
