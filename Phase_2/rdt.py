# The sending side of rdt simply accepts data from the upper layer via the rdt_send(data) event,
# creates a packet containing the data (via the action make_pkt(data) ) and sends the packet into the
# channel. In practice, the rdt_send(data) event would result from a procedure call (for example, to
# rdt_send() ) by the upper-layer application.

from socket import *
host = "localhost"
port = 9876
packet_size = 1024 # 1024 bits == 1 Kb
sequence_number = 0 # counter for packet number


# sending side
def rdt_send(data): # Called from client side to Send data to rdt module for parsing into packets
    udp_client = socket(AF_INET, SOCK_DGRAM)
    udp_client.connect((host, port))

    packet_list = make_packets(data)
    for packet in packet_list:
        udp_client.sendto(packet, (host, port))
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

def rdt_recv(packet): # called from the server side to recieve a packet
    with open("received_files\\testn.bmp", 'ab') as data:
        data.write(packet)
    
              

