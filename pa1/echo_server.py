# Network Project 1
# Zhuo Chen
# 2019.1.15

import sys
import socket
from _thread import *

HOST= '127.0.0.1'
PORT = int(sys.argv[1])

def client_thread(conn):
    with conn: 
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        start_new_thread(client_thread,(conn,))
