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
        if filename == '':
            filename = 'test_file.bmp'

        else:
            data = open("send_files\\" + filename, "rb")       
            rdt_send(data, filename)
        
        
        

if __name__ ==  '__main__':
    client(host, port)