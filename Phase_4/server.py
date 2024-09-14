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
import struct


def server():
    local_port = 9876         # Arbitrary port number
    bufferSize = 1024         # size of file per packet
    packet_list = []          # initialize list to store packets as the come in
    last_SEQ = 1 #start at 1 since first packet will always be 0
    ACK = 0xFF

    # Create server socket
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('',local_port))
    print("The server is ready to receive on port {}".format(local_port))

    # receive corruption option data before starting 
    corrupt_option = server_socket.recv(packet_size)
    error_chance = server_socket.recv(packet_size)
    corrupt_option = int(corrupt_option.decode())
    error_chance = int(error_chance.decode())
    ######

    # Start of server receive of client file
    while True:
        packet, client_address = server_socket.recvfrom(bufferSize)
        rcv_SEQ, rcv_checksum = struct.unpack('!2H', packet[:4])
        payload = packet[4:]

        if payload == b'<EDF>':
            print('Download complete.')
            extract(packet_list)

            
            server_socket.close()
            break

        else:
            if corrupt_option == 3:
                payload = corrupt_data(payload, error_chance)

            # print statment for clarity on packet exchange   
            # print('seq {}, checksum {}'.format(rcv_SEQ, rcv_checksum))

            data_checksum = get_checksum(payload)

            if last_SEQ == rcv_SEQ:
                # print('SEQ are the same last_SEQ: {} rcv_SEQ: {}'.format(last_SEQ, rcv_SEQ))
                ACK_packet = make_packets(ACK, rcv_SEQ)
                server_socket.sendto(ACK_packet, client_address) 
                
            elif  data_checksum != rcv_checksum:
                # print('seq {}, checksum {} current: {}'.format(rcv_SEQ, rcv_checksum, data_checksum))
                ACK_packet = make_packets(ACK, last_SEQ)
                server_socket.sendto(ACK_packet, client_address) 
                
            # packet passes checksum and seq test
            else:
                if corrupt_option == 5 and random.randint(0, 100) < error_chance:
                    # Do nothing to "lose" packet
                    print('data packet lost')
                    pass

                else:
                    packet_list.append(payload)
                    ACK_packet = make_packets(ACK, rcv_SEQ)
                    server_socket.sendto(ACK_packet, client_address)
                    last_SEQ = rcv_SEQ
    
    # Restart server receive
    server()


if __name__ ==  '__main__':
    server()
