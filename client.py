import socket
from unicodedata import name
c = socket.socket()
c.connect(('localhost',9999))
print(c.recv(1024))
name = input('Enter Your name:')
c.send(bytes(name,'utf-8'))