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



from socket import *
from UDP_client import *
import time

def server():
    local_port = 9876         # Arbitrary port number
    bufferSize = 1024         # size of file per packet
    packet_list = []          # initialize list to store packets as the come in


    # Create server socket
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('',local_port))
    print("The server is ready to receive on port {}".format(local_port))

    # Receive file info
    filename, client_address = server_socket.recvfrom(bufferSize)
    file_size, client_address = server_socket.recvfrom(bufferSize)
    filename = filename.decode()
    file_size = int(file_size.decode())/1000
    print('\nDownloading: ' + filename + ', ' + 'File size: ' + str(file_size) + ' KB')



    #infinite loop to always be listening to port for packets
    while True:
        packet, client_address = server_socket.recvfrom(bufferSize)
        transfer_start = time.monotonic_ns()

        if packet == b'<EDF>':
            print('Download complete.')
            server_socket.sendto("Server received file!\n".encode(), client_address)
            rdt_rcv(packet_list, filename)
            server_socket.close()
            break

        else:
            packet_list.append(packet)

    # End sequence
    transfer_end = time.monotonic_ns()
    cycle_timer_in_milliseconds = (transfer_end-transfer_start)/1000000 
    print('done in: ' + f'{cycle_timer_in_milliseconds:.0f}' + ' ms\n')
    server()


if __name__ ==  '__main__':
    server()
