import socket
import threading
import time

t_lock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            t_lock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            t_lock.release()

host = ''
port = 0

server = ('', 10001)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

r_thread = threading.Thread(target = receving, args=('RecvThread', s))
r_thread.start()

alias = raw_input("Name: ")
message = raw_input(alias + '-> ')
while message != 'q':
    if message != '':
        s.sendto(alias + ': ' + message, server)
    t_lock.acquire()
    message = raw_input(alias + '-> ')
    t_lock.release()
    time.sleep(0.2)

shutdown = True
r_thread.join()
s.close()
