# Network Project 1
# Zhuo Chen
# 2019.1.15

import sys
import socket

HOST= sys.argv[1]
PORT = int(sys.argv[2])

while True:
    message = input("Type a message to send: ")
    if message != "":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(str.encode(message))
            data = s.recv(1024)
            print('Received', data.decode('utf-8'))
    
