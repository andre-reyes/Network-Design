#Andre Reyes
#Network Design SU23
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


server_name = "localhost" # can also be 127.0.0.1
server_port = 65309
bufferSize = 2048

#create socket for client
client_socket = socket(AF_INET, SOCK_DGRAM)

#grab message from user and send it to server
message = input('Input lowercase sentence: ')
client_socket.sendto(message.encode(),(server_name, server_port))
modified_message, server_address = client_socket.recvfrom(bufferSize)
address, port = server_address

#display message for user to see on client side
print ("message from server: {} \nserver address: {} \nserver port: {}".format(modified_message.decode(), address, port))
client_socket.close()