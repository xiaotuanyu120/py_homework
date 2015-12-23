import socket
import time

host = ''
port = 10001

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quitting = False
print 'Server started'

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        if 'Quit' in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)
        print str(data) + '\nFrom' + str(addr) + time.ctime(time.time())
        for client in clients:
            s.sendto(data, client)
    except:
        pass
s.close()
