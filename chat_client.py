import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("10.1.10.242", 5555))

data = my_socket.recv(1024)
print "received:\n%s" %  data
my_socket.close()