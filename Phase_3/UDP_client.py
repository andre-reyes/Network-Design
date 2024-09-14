# UDP_client.py is the sending side of rdt simply accepts data from the upper layer via the rdt_send(data) event,
# creates a packet containing the data (via the action make_pkt(data) ) and sends the packet into the
# channel. In practice, the rdt_send(data) event would result from a procedure call (for example, to
# rdt_send() ) by the upper-layer application.

from socket import *
import os.path
import struct
import sys
import random

host = "localhost"
port = 9876
packet_size = 1018 # 1024 bytes - 6 bytes for header
sequence_number = 0 # counter for packet number


# sending side


def rdt_send(data, corrupt_option, error_chance): 
    '''Called from client side to Send data to rdt module for parsing into packets'''

    # create client socket
    udp_client = socket(AF_INET, SOCK_DGRAM)
    udp_client.connect((host, port))
    print ("the Client has connected to {}".format(host))
    
    # send corruption data to server before starting
    udp_client.sendto(str(corrupt_option).encode(), (host, port))
    udp_client.sendto(str(error_chance).encode(), (host, port))

    # make initial packet list
    packet_list = []
    payload = data.read(packet_size)
    while payload:
        packet_list.append(payload)
        payload = data.read(packet_size)

    
####################### send packet one at a time and wait for ACK response from server ###############################

    SEQ = 0 # start at seq 0, will flip to 1 after ack1 received from server 
    for i in range(len(packet_list)):
    # packet_list, checksum = make_packets(data, SEQ)
        isACK = False
        packet = make_packets(packet_list[i], SEQ)
        


        while isACK == False:
            udp_client.sendto(packet, (host, port))
            # print('Sending packet {}'.format(i))

            #wait for ACK from server
            rcv_packet = udp_client.recv(packet_size)
            rcv_SEQ, rcv_checksum, ACK = struct.unpack('!3H', rcv_packet)
            # print('send seq {}, rcv_checksum {}, ACK {}'.format(SEQ, rcv_checksum, ACK))
            
            if corrupt_option == '2':
                ACK = corrupt_ack(ACK, int(error_chance))
            ACK_checksum = get_checksum(ACK)
            
            if rcv_checksum != ACK_checksum:
                # print('ACK corrupted, Resending packet {}...'.format(i))
                packet = make_packets(packet_list[i], SEQ)
            elif rcv_SEQ != SEQ:
                # print('ACK is same as last ACK, Resending packet {}...'.format(i))
                packet = make_packets(packet_list[i], SEQ)
            else:
                isACK = True

        if (SEQ == 0): 
            SEQ = 1
        elif (SEQ == 1): 
            SEQ = 0
        
    # send EOF tag to let server know it's done
    end_of_file = struct.pack('!2H', 0, 0) + b'<EDF>'
    udp_client.sendto(end_of_file, (host, port))

    print('Packets sent...')


################################# Helper Functions ########################################    
def get_checksum(packet_byte_array):
    '''takes in the data and creates a checksum then flips bits using negate operator 
    and returns w/ mask to ensure only 8 bits are returned'''
    result = 0
    
    if type(packet_byte_array) == int:
        return ~packet_byte_array & 0xFF
    else:
        for num in packet_byte_array:
            result += num
            if result >= 256:
                result -=255 # subtract 256 and add one

    checksum =  ~result & 0xFF #negate and mask to maintain 8 bits   

            
    return checksum

def make_packets(data_or_ack, SEQ): # Creates a packet containing the data
    '''returns byte packet of:\n 
    | SEQ | checksum | payload/ack |'''
    
    checksum = get_checksum(data_or_ack)
    header = struct.pack('!2H', SEQ, checksum)

    # since ack is an int it is added to header data differently
    if type(data_or_ack) == int:
        packet = header + struct.pack('!H', data_or_ack)
    else:
        packet = header + data_or_ack
        
    return packet
    

def corrupt_ack(ACK, error_chance = 0):
    '''Corrupts the ack packet data, Returns corrupted ACk'''
    rand = random.randint(0,100)
    corrupted_ACK = ACK

    # Option 2 - ACK packet bit-error\n
    if rand < error_chance:
        corrupted_ACK = random.randint(0,255)

    return corrupted_ACK


def corrupt_data(data, error_chance):
    '''Corrupts the data packet, Returns corrupted data file'''

    rand = random.randint(0,100)
    corrupted_data = data

    # Option 3 - Data packet bit-error
    if rand < error_chance:
        rand_bytes = random.randbytes(128)
        corrupted_data = rand_bytes + data[127:]
    return corrupted_data

def extract(packet_list):
    '''Extract packets that were saved to a list into a file'''
    file_path = "received_files\\received_file.jpg"
    for packet in packet_list:
        with open(file_path, 'ab') as data:
            data.write(packet)
    print('\nFile saved to: .\\' + file_path)

        
def corruption_choice():
    '''Display options for user to cause issue with packets. 
    returns error chance based on user input 0-100%'''

    print('\nPlease select from the options below:\n\nOption 1 - No bit-errors\nOption 2 - ACK packet bit-error\nOption 3 - Data packet bit-error\n')
    
    while True:    
        option = input('Enter choice here: ')
        match option:
            case '1':
                print('Option 1 - No bit-errors\n')
                error_chance = 0
                break
            case '2':
                print('Option 2 - ACK packet bit-error\n')
                error_chance = input('Enter percentage of packet error between 0-100: ')
                break
            case '3':
                print('Option 3 - Data packet bit-error')
                error_chance = input('Enter percentage packet of error between 0-100: ')
                break
            case _:
                print('\nerror: Make a valid choice\n')
                continue               
    return option, error_chance   

