from socket import *

host = "localhost"
port = 9876
buffer = 1024

def client(host, port):
    
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.connect((host, port))
    print ("the Client has connected to {}".format(host))

    while True:
        message = input('Input lowercase sentence (Enter "q" or "Q" to end): ')    
        client_socket.sendto(message.encode(),(host, port))
        modified_message, server_address = client_socket.recvfrom(buffer)
        address, port = server_address   

        
        if modified_message.decode().lower() == 'q':
            client_socket.close()
            print("The client has ended.")
            break
        else:
            print ("\tmessage from server: {} \n\tserver address: {} \n\tserver port: {}\n".format(modified_message.decode(), address, port))
        

if __name__ ==  '__main__':
    client(host, port)from socket import *
from rdt import *
host = "localhost"
port = 9876
buffer = 1024

def client(host, port):
    
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.connect((host, port))
    print ("the Client has connected to {}".format(host))


    while True:
        # Get user input
        # filename = input('Enter filename: ')
        # if filename == '':
        #     filename = 'test_file.bmp'

        filename = 'test_file.bmp'
        data = open("Net-Design\\Phase_2\\src\\" + filename, "rb")       
        rdt_send(data)
        
        # End condition here
        # if modified_message.decode().lower() == 'q':
        #     client_socket.close()
        #     print("The client has stopped.")
        #     break
        # else:
        

if __name__ ==  '__main__':
    client(host, port)