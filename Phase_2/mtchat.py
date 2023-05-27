# Andre Reyes
# Network Design SU23
# Phase 1 - send/recieve UDP data packets
# mtchat.py - multi threaded chat
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


from threading import Thread
from socket import *
from time import sleep

def main():
# main function that handles creating and running 
# threads for the server and client processes.


    PORT = 65309         # chosen from range of values (49152-65535) for private/temporary purposes
    BUFFER = 2048        # size for the message, anything outside the range is lost in UDP packets

    print ("Creating threads...")
    server_thread = Thread(target=server, args=(BUFFER, PORT,))
    client_thread = Thread(target=client, args=(BUFFER, PORT,))
    
    print ("Starting threads...")
    server_thread.start()
    sleep(0.1)
    client_thread.start()

    client_thread.join()
    server_thread.join()
    
    print ("threads complete...")


def server(buffer, port):
# server  creates a new socket and allows 
# sending data to/from the client socket.

    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(("",port))
    print("The server is ready to receive on port {}".format(port))

    while True:
        message, client_address = server_socket.recvfrom(buffer)

        if message.decode().lower() == 'q':
            server_socket.sendto('q'.encode(), client_address)
            server_socket.close()
            print("The server has ended.")
            break
        else:
            modified_message = message.decode().upper() + "\n\tclient port: {}".format(client_address[1])
            server_socket.sendto(modified_message.encode(), client_address)


def client(buffer, port):
# Client  creates a socket to send and 
# recieve a message from/to the server.

    HOST = "localhost" # localhost == 127.0.0.1

    client_socket = socket(AF_INET, SOCK_DGRAM)
    
    while True:
        message = input('Input lowercase sentence (Enter "q" or "Q" to end): ')    
        client_socket.sendto(message.encode(),(HOST, port))
        modified_message, server_address = client_socket.recvfrom(buffer)
        address, port = server_address   

        
        if modified_message.decode().lower() == 'q':
            client_socket.close()
            print("The client has ended.")
            break
        else:
            print ("\tmessage from server: {} \n\tserver address: {} \n\tserver port: {}\n".format(modified_message.decode(), address, port))
        


if __name__ ==  '__main__':
    main()



