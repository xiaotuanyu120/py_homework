import socket
import json

s = socket.socket()

host = '182.254.152.182'
port = 10003

data_pack = json.dumps({
    'key': 'aming-linux-the5fire',
    'data': {
           'name': 'ZHAO PEIWU',
           'words': 'Can I come in?'
    }
})

s.connect((host, port))
s.send(data_pack)
data = s.recv(1024)
s.close()
print 'Recived', repr(data)
