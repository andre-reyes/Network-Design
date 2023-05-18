from threading import Thread
from socket import *
from time import sleep

buffer = 2048

def server():
    local_port = 65309         # Port number chosen from range of values (49152-65535) for private/temporary purposes
    bufferSize = 2048          # 

    #create server socket
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(("",local_port))

    print("The server is ready to receive on port {}".format(local_port))
    

    #infinite loop to always be listening to port while active
    while bool:
        message, client_address = server_socket.recvfrom(bufferSize)
        modified_message = message.decode().upper() + "\n\tclient port: {}".format(client_address[1])
        server_socket.sendto(modified_message.encode(), client_address)

        

def client():
    server_name = "localhost" # can also be 127.0.0.1
    server_port = 65309
    bufferSize = 2048

    # create socket for client
    client_socket = socket(AF_INET, SOCK_DGRAM)

    # grab message from user and send it to server
    # 
    while True:
        message = input('Input lowercase sentence: ')
        client_socket.sendto(message.encode(),(server_name, server_port))
        modified_message, server_address = client_socket.recvfrom(bufferSize)
        address, port = server_address

        print ("\tmessage from server: {} \n\tserver address: {} \n\tserver port: {}\n".format(modified_message.decode(), address, port))

            

if __name__ ==  '__main__':
    print ("Creating threads...")
    server_thread = Thread(target=server)
    client_thread = Thread(target=client)
    
    print ("Starting threads...")
    server_thread.start()
    sleep(0.1)
    client_thread.start()

    client_thread.join()
    server_thread.join()
    
    print ("threads complete...")
    server_thread.end()
    client_thread.end()


