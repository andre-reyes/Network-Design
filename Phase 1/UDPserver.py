#Andre Reyes
#Phase one - send/recieve UDP messages

'''
    This is Phase one of the five phase project for Newtork Design SU23
    Description: In Phase 1 of the project, each student has to individually implement the standard user datagram protocol (UDP) sockets. 
    The intention is to transfer a message (Say “HELLO”) from the UDP client to the UDP server and then  ECHO the message back from the UDP server to the UDP client. 
    Note that the client and server process can reside on the same host, but have to use different port numbers. 
'''

'''
    Application Example:
    1. client reads a line of characters (data) from its keyboard and sends
    data to server
    2. server receives the data and converts characters to uppercase
    3. server sends modified data to client
    4. client receives modified data and displays line on its screen
'''

from socket import *
HOST = ''                  # Symbolic name meaning all available interfaces
local_port = 65309         # Port number chosen from range of values (49152-65535) for private/temporary purposes
local_ip = "192.168.0.183"

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((HOST,local_port))
print("The server is ready to recieve")
while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper()
    server_socket.sendto(modified_message.encode(), client_address)