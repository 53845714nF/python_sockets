#! /usr/bin/env python3
"""
Client that sends data to a TCP socket.
Which is available on localhost port 1337.
"""

from socket import socket, AF_INET, SOCK_STREAM
from os import getenv

HOST = getenv('HOST', '127.0.0.1')
PORT = getenv('PORT', '1337')

with socket(AF_INET, SOCK_STREAM) as tcp_socket:
    tcp_socket.connect((HOST, int(PORT)))
    tcp_socket.sendall(b'Hello, world')
