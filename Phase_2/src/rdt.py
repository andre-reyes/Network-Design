# The sending side of rdt simply accepts data from the upper layer via the rdt_send(data) event,
# creates a packet containing the data (via the action make_pkt(data) ) and sends the packet into the
# channel. In practice, the rdt_send(data) event would result from a procedure call (for example, to
# rdt_send() ) by the upper-layer application.


packet_size = 1024 # 1024 bits == 1 Kb
sequence_number = 0 # counter for packet number


# sending side
def rdt_send(data): # Called from client side to Send data to rdt module for parsing into packets
    packet_list = make_packets(data)
    print(packet_list)
    
    

def make_packets(data): # Creates a packet containing the data
    packet_list = []
    packet = data.read(packet_size)
   
    
    while packet:
        packet_list.append(packet)
        packet = data.read(packet_size)
    return packet_list
    


# Receiving side 

def extract(packet, data): # extract packet from data              
    pass
def deliver_data(data): # send to server
    pass
def rdt_recv(packet): # called from the server side to recieve a paket
    while packet:
        data = open("Net-Design\\Phase_2\\src\\test\\testn.bmp", 'ab')
        data.write(packet)
        data.close()
    deliver_data(data)
              
              
    # extract(packet, data) 
    # deliver_data(data)
    
def rdt_send():
    pass
def rdt_recv():
    pass
def deliver_data():
    pass
def make_pkt(data):
# Creates a packet containing the data
    pass
def udt_send()
# To transfer packet over unreliable channel to reciever
    pass
