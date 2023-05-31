from socket import *
from UDP_client import *
import time

def server():
    local_port = 9876         # Port number chosen from range of values (49152-65535) for private/temporary purposes
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
