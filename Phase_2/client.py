from socket import *
from rdt import *
import os.path



def client():
    send_path = 'send_files\\'
    
    print ("the Client has connected to {}".format(host))


    while True:
        # Get user input
        filename = input('Enter filename(default is test_file.bmp): ')
        file_path = os.path.join(send_path, filename)
        
        if not os.path.exists(file_path) or not filename:
            filename = 'test_file.bmp'

        file_path = os.path.join(send_path, filename)
        with open(file_path, "rb") as data:       
            rdt_send(data, filename)
        

if __name__ ==  '__main__':
    client()