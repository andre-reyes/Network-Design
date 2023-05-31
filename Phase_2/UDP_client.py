# UDP_client.py is the sending side of rdt simply accepts data from the upper layer via the rdt_send(data) event,
# creates a packet containing the data (via the action make_pkt(data) ) and sends the packet into the
# channel. In practice, the rdt_send(data) event would result from a procedure call (for example, to
# rdt_send() ) by the upper-layer application.

from socket import *
from time import sleep
import os.path

host = "localhost"
port = 9876
packet_size = 1024 # 1024 bits == 1 Kb
sequence_number = 0 # counter for packet number


# sending side

def rdt_send(data, filename): # Called from client side to Send data to rdt module for parsing into packets
    udp_client = socket(AF_INET, SOCK_DGRAM)
    udp_client.connect((host, port))
    

    # gather info for file
    packet_list = make_packets(data)
    file_path = os.path.join('.\\send_files', filename)
    file_size = os.path.getsize(file_path)

    # send data and then send EOF tag to let server know it's done
    print('Sending '+ filename + '...')
    udp_client.sendto(str(filename).encode(), (host, port))
    udp_client.sendto(str(file_size).encode(), (host, port))
    
    for packet in packet_list:
        udp_client.sendto(packet, (host, port))

    udp_client.sendto(b'<EDF>', (host, port))

    # Verify to client file was received
    server_message = udp_client.recv(packet_size)
    print(server_message.decode())
    

def make_packets(data): # Creates a packet containing the data
    packet_list = []
    packet = data.read(packet_size)
   
    while packet:
        packet_list.append(packet)
        packet = data.read(packet_size)
    return packet_list
    

# Receiving side 

def rdt_rcv(packet_list, filename):
    file_path = "received_files\\" + filename
    for packet in packet_list:
        with open(file_path, 'ab') as data:
            data.write(packet)
    print('\nFile saved to: .\\' + file_path)


    
              

