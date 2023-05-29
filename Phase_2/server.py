from socket import *
from rdt import *
local_port = 9876         # Port number chosen from range of values (49152-65535) for private/temporary purposes
bufferSize = 1024          # 
filename = "receivedFile.bmp" # default filename
packet_list = []

#create server socket
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("",local_port))

print("The server is ready to receive on port {}".format(local_port))
filename, client_address = server_socket.recvfrom(bufferSize)
file_size, client_address = server_socket.recvfrom(bufferSize)
print('Downloading: ' + filename.decode() + file_size.decode())
#infinite loop to always be listening to port while active
while True:
    packet, client_address = server_socket.recvfrom(bufferSize)
    if packet == b'<EDF>':
        server_socket.sendto("received file!".encode(), client_address)
        server_socket.close()
        break
    else:
        packet_list.append(packet)
rdt_rcv(packet_list)
    