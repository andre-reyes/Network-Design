from socket import *
from rdt import *
import time
from tqdm import tqdm


def server():
    local_port = 9876         # Port number chosen from range of values (49152-65535) for private/temporary purposes
    bufferSize = 1024          # 
    filename = "receivedFile.bmp" # default filename
    packet_list = []
    cycle_counter = 0


    #create server socket
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(("",local_port))
    print("The server is ready to receive on port {}".format(local_port))

    #receive file info
    filename, client_address = server_socket.recvfrom(bufferSize)
    file_size, client_address = server_socket.recvfrom(bufferSize)
    file_size = int(file_size.decode())/1000
    print('\nDownloading: ' + filename.decode() + ', ' + 'File size: ' + str(file_size) + ' KB')



    #infinite loop to always be listening to port for packets
    while True:
        packet, client_address = server_socket.recvfrom(bufferSize)
        start = time.monotonic_ns()

        if packet == b'<EDF>':
            server_socket.sendto("Server received file!".encode(), client_address)
            # server_socket.close()
            break
        else:
            packet_list.append(packet)

    rdt_rcv(packet_list, filename.decode())
    end = time.monotonic_ns()
    cycle_counter += 1
    cycle_timer = (end-start)/1000000 #converts nanoseconds to milliseconds

    print('done in: ' + f'{cycle_timer:.0f}' + ' ms')

if __name__ ==  '__main__':
    server()
