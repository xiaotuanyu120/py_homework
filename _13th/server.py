import socket

class Chatroom(object):
    '''This is a chatroom'''
    def __init__(self, maxconnect):
        '''you can setting server host/port and max connection here'''
        self.host = ''
        self.port = 10001
        self.maxconn = maxconnect

    def open_room(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(self.maxconn)

    def close_room(self):
        self.s.close()

    def online_accept(self):
        conn, addr = self.s.accept()
        self.online_user.append(conn)

    def msg_receive(self):
        while True:
            msg =  self.s.recv(1024)
            if not msg:
                break
            return msg

    def broadcast(self, msg):
        for conn in self.online_user:
            conn.sendall(msg)


if __name__ == '__main__':
    chatroom = Chatroom(5)
    chatroom.open_room()
    print "open chatroom"
    while True:
        chatroom.online_accept()
        msg = chatroom.msg_receive()
        chatroom.broadcast(msg)
