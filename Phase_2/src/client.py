from socket import *
from rdt import *
host = "localhost"
port = 9876
buffer = 1024

def client(host, port):
    
    
    print ("the Client has connected to {}".format(host))


    while True:
        # Get user input
        filename = input('Enter filename(default: just hit enter): ')
        # if filename == '':
        #     filename = 'test_file.bmp'

        filename = 'test_file.bmp'
        # End condition here
        if filename.lower() == 'q':
            # client_socket.close()
            print("The client has stopped.")
            break
        else:
            data = open("Net-Design\\Phase_2\\src\\" + filename, "rb")       
            rdt_send(data)
        
        
        

if __name__ ==  '__main__':
    client(host, port)