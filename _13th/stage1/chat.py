import socket

# server ip and port setting
host = ''
port = 10001

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind object to the host and port
s.bind((host, port))

# start listen
s.listen(1)

# when connected
conn, addr = s.accept()
print 'Connected by', addr

# start talk
while True:
    data = conn.recv(1024)
    if not data:break
    conn.sendall(data)
s.close()
