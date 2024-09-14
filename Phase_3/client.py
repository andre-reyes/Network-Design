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
    In Phase 3, Implement: Sequence Numbers (to identify duplicates), 
    Checksum (implement your own (Do not use Java/Python built-in function!), 
    similar to UDP), and ACKs (remember, RDT 2.2 is a NAK-free protocol). 

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
import time



def client():
    while True:
        # Get user input
        send_path = 'send_files\\'
        print('\nFile list:\n')
        file_list = os.scandir(send_path)
        for entry in file_list:
            if entry.is_file():
                print(entry.name)
        filename = input('\nEnter filename (default is test_file.jpg): ')
        file_path = os.path.join(send_path, filename)
        
        if not os.path.exists(file_path) or not filename:
            no_file_found = input('Error: file not found. would you like use the default name test_file.jpg (y or n)? ')
            if no_file_found.lower() == 'y':
                filename = 'test_file.jpg'
            else:
                continue
        corrupt_option, error_chance = corruption_choice()
        # Start send to server       
        file_path = os.path.join(send_path, filename)
        with open(file_path, "rb") as data:      
            transfer_start = time.monotonic_ns()
            rdt_send(data, corrupt_option, error_chance)
            transfer_end = time.monotonic_ns()
            cycle_timer_in_milliseconds = (transfer_end-transfer_start)/1000000 
            print('File sent in: ' + f'{cycle_timer_in_milliseconds:.0f}' + ' ms\n')
        

if __name__ ==  '__main__':
    client()