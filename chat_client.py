import socket
import sys
import select

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 5555))

data = my_socket.recv(1024)
print "received:\n%s" %  data

user_name = sys.stdin.readline().strip()
my_socket.send(user_name)
data = my_socket.recv(1024)
print data

# print my_socket.getsockname()

running = True
while running:
    inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])

    for s in inputready:
        if s == my_socket:
            msg = s.recv(1024)
            if msg:
                print msg
            else:
                print "Disconnected from Server!"
                running = False
        if s == sys.stdin:
            msg = sys.stdin.readline()
            my_socket.sendall(msg)


my_socket.close()