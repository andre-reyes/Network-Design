# Reliable Data Transfer over as Perfectly Reliable Channel: rdt1.0
# from tqdm import tqdm
# from time import sleep
from socket import *

from rdt import *
host = "localhost"
port = 9876
buffer = 1024

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.connect((host, port))
print ("the Client has connected to {}".format(host))

def main():
    filename = input('Enter filename (default is test_file.bmp): ')
    if filename == '':
        filename = 'test_file.bmp'
    while True: 
        with open("Net-Design\\Phase_2\\src\\" + filename, "rb") as data:    
            packet = rdt_send(data)
            client_socket.sendto(packet,(host, port))

if __name__ ==  '__main__':
    main()