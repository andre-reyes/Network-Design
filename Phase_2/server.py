from socket import *
from rdt import *
import time
from tqdm import tqdm


def server():
    local_port = 9876         # Port number chosen from range of values (49152-65535) for private/temporary purposes
    bufferSize = 1024          # 
    filename = "receivedFile.bmp" # default filename
    packet_list = []

    #create server socket
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(("",local_port))
    print("The server is ready to receive on port {}".format(local_port))

    # First receive file info
    filename, client_address = server_socket.recvfrom(bufferSize)
    file_size, client_address = server_socket.recvfrom(bufferSize)
    print('\nDownloading: ' + filename.decode() + ', ' + 'File size: ' + file_size.decode() + ' Bits')
    file_size = int(file_size.decode())



    #infinite loop to always be listening to port for packets
    # with tqdm(total=file_size, unit='b', unit_scale=True, unit_divisor=1000) as progress_bar:

    while True:
        packet, client_address = server_socket.recvfrom(bufferSize)
        start = time.monotonic_ns()

        if packet == b'<EDF>':
            server_socket.sendto("received file!".encode(), client_address)
            server_socket.close()
            break
        else:
            packet_list.append(packet)
            # progress_bar.update(bufferSize)

    rdt_rcv(packet_list, filename.decode())
    end = time.monotonic_ns()
    print(f'{(end-start)/1000000000}' + 'ns')

if __name__ ==  '__main__':
    server()
