#Andre Reyes
#Network Design SU23
#Phase one - send/recieve UDP messages
#mtchat.py - multi threaded chat
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

def server(buffer, port):

    #create server socket
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(("",port))

    print("The server is ready to receive on port {}".format(port))
    

    #infinite loop to always be listening to port while active
    while bool:
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
    server_name = "localhost" # can also be 127.0.0.1

    # create socket for client
    client_socket = socket(AF_INET, SOCK_DGRAM)

    # grab message from user and send it to server
    # 
    while True:
        message = input('Input lowercase sentence (Enter "q" or "Q" to end): ')    
        client_socket.sendto(message.encode(),(server_name, port))
        modified_message, server_address = client_socket.recvfrom(buffer)
        address, port = server_address   
        if modified_message.decode().lower() == 'q':
            client_socket.close()
            print("The client has ended.")
            break
        else:
            print ("\tmessage from server: {} \n\tserver address: {} \n\tserver port: {}\n".format(modified_message.decode(), address, port))
        

if __name__ ==  '__main__':
    PORT = 65309         # Port number chosen from range of values (49152-65535) for private/temporary purposes
    BUFFER = 2048

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



