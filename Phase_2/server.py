from socket import *
from rdt import *
local_port = 9876         # Port number chosen from range of values (49152-65535) for private/temporary purposes
bufferSize = 1024          # 

#create server socket
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("",local_port))

print("The server is ready to receive on port {}".format(local_port))

#infinite loop to always be listening to port while active
while True:
     = server_socket.recv(bufferSize)
    packet, client_address = server_socket.recvfrom(bufferSize)

    rdt_recv(packet)
    server_socket.sendto("received packet!".encode(), client_address)