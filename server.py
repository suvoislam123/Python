import socket
s = socket.socket()
print('socket Created')
s.bind(('localhost',9999))
s.listen(3)
while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print('client connected with address: {} and name {}'.format(addr,name))
    c.send(bytes('Welcome to python programming by Shuvo','utf-8'))
    c.close()
    