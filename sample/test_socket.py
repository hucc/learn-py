# -*- coding: utf-8 -*-
import socket

_author__ = 'HuCC'

HOST = '192.168.0.37'
PORT = 50000
BUFFER = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.send('hello, tcpServer!')
while True:
    buf = socket.recv(1024)
    if not len(buf):
        break
    print buf
sock.close()
