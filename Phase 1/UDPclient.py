from socket import *


server_name = "localhost" #or 127.0.0.1
server_port = 12000
bufferSize = 2048
client_socket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence: ')
client_socket.sendto(message.encode(),(server_name, server_port))
modified_message, server_address = client_socket.recvfrom(bufferSize)
address, port = server_address
print ("message from server: {} \nserver address: {} \nserver port: {}".format(modified_message.decode(), address, port))
client_socket.close()