# Andre Reyes
# Network Design SU23
# Phase 2 - send/recieve UDP data packets using file data
# server.py is the server side, split from the original mtchat.py in phase 1
#
# REQUIREMENTS: client.py, server.py, UDP_client.py
#           2 directories:
#               'send_files\' that stores files for client to send to server
#               'received_files\' that places received files from client
'''
    In Phase 2, the intention is to transfer a file (say BMP) between a 
    UDP client process and a UDP server process. In Phase 2, we will provide 
    reliable data transfer (RDT) service assuming that the underlying layer is 
    perfectly reliable using UDP connection developed in Phase 1.

'''

'''
    Application Example:
    1. Client sends file to UDP_client module where it will be split into individual packets
    2. packets are then packaged in a list and sent one by one to the server
    3. server receives packets and places them in a temporary list
    4. Server then iterates over the packet list object and saves it to a predetermined directory
'''

from UDP_client import *
import os.path



def client():
    send_path = 'send_files\\'
    
    print ("the Client has connected to {}".format(host))


    while True:
        # Get user input
        filename = input('\nEnter filename (default is test_file.bmp): ')
        file_path = os.path.join(send_path, filename)
        
        if not os.path.exists(file_path) or not filename:
            no_file_found = input('Error: file not found. would you like use the default name test_file.bmp (y or n)? ')
            if no_file_found == 'y'.lower():
                filename = 'test_file.bmp'
            else:
                continue

        file_path = os.path.join(send_path, filename)
        with open(file_path, "rb") as data:       
            rdt_send(data, filename)
        

if __name__ ==  '__main__':
    client()