# DesignFile.md

## Title and Authors

* Phase 4

* Andre Reyes

</br>


## Purpose of the phase
---------------------------------------------------------------------------

### **Phase 4**
The purpose of phase 4 is to implement RDT3.0 by adding a countdown timer feature onto the RDT2.2 that was done in Phase 3
</br>

## Code Explanation
-------------------------------------------------------------------------
## Introduction
    Overall the flow of the program takes input from the user on the desired file and error/loss rate. Then, rdt_send() turns the data into a byte data list that is then packaged in the UDP header style including SEQ and checksum. The program then takes the packeged packets and attempts to send them to the server.

    The server then attempts to read the information and tests against the header SEQ and checksum to verify the data/packet is good. Once the okay is made it then sends an acknowledgement to the sender to move on to the next packet.

    This cycle repeats until all packets sent. If the packet or ACK loss option is selected, the sender starts a timeout to wait for ack or from reciever, if none recieved (ie packet lost or ack lost) then the sender will attempt to resend packet.

## Detailed Description
### **Imports**
![imports.png](images/imports.png "Imported Libraries")

* Time is imported to allow tracking of send/receive time
* socket imports all to make it easier on the eyes when implementing methods
* struct is used as a way to pack the data into packets that include SEQ/ACK/checksum
* sys is used primarily for helper methods for file handling
* random is used to corrupt the data with random bits witha random chance

</br>

### **server(): Part 1**
![server_part_1.png](images/server_part_1.png "Server Function part 1")
* server() is responsible for creating the sockets and listening for the client data. 
* The server socket first receives corruption information sent from the client before starting file transfer.
</br>

### **server(): Part 2**

![server_part_2.png](images/server_part_2.png "Server Function part 2")
* When data is recieved from the client, it is tested on end conditions. otherwise it takes the packet information and appends it to a list
* Once the end condition is met, it takes the new packeet list and sends it to rdt_rcv where it will be iterated through onto a file write as binary
* After taking in the corruption option, the server then attempts corrupts the data
* Once done the server tests it's data against the received data checksum/seq
* if all is good with the data and it is not corrupt it will append the good packet to a list

</br>

### **server(): Part 3**
![server_part_3.png](images/server_part_3.png "Server Function part 3")
* updated server(): Part 2 to include loss handling,
* before attempting to add the packet to the list and continue to the next this if/else statement first tests to see if that packet will be "lost"
</br>

### **UDP_client.py: extract()**
![extract.png](images/extract.png "extract function")
* extract is the receiving side of the UDP-client.py and is responsible for writing the packet_list sent from the server along with the filename and appended onto a file write function
* the `with open() as ____:` is used as a safe way to open/close files without having to stat the close() method

</br>

### **client()**
![client.png](images/client.png "Client Function")
* The client function is similar to the server function but does so in the opposite way.
* It waits for user input, once user inputs filename
it then converts the file to a list of binary values broken up in the specified buffer: 1024 bits


</br>

### **UDP_client.py: rdt_send()**
![rdt_send.png](images/rdt_send.png "rdt send function")
* rdt_send is responsible for all the network communication from the client to the server.

* Creates the sockets for communication and then sends initial file information based on the user's input file.

* Then iterates in a loop in order to send the individual packets to a list
* Finally, set up for ack packet retrieval and iterate through packet list to ensure only one packet is sent and handled by the server at a time


</br>

### **UDP_client.py: rdt_send(): Part 2 - Timeout**
![send_timer.png](images/send_timer.png "rdt send function")
* isACK loop is modified from Phase 3 to include a timeout of the socket
* try/except is used here otherwise when socket times out it ends program, this ensures there is error handling to repeat timed_out loop
* within the try/except, the loss rate is tested and does nothing by passing to loop again to retrieve data again
</br>

### **UDP_client.py: rdt_send(): Part 3 - End**
![send_timer.png](images/rdt_send_2.png "rdt send function")
* once ack is received finally, it tests for data accuracy/corruption and the ends loop
* Once loop ends it will change sequence number to the oppoosite and continue 
* Also sends a <EDF> **E**n**D** of **F**ile flag to signify to the server it is done receiving. This was chosen due to the lack of knowledge if anywhere in the packet list there were any similar flags of EOF or END, so a combination of the two was mad arbitrarily.
</br>

### **UDP_client.py: make_packets()**
![make_packet.png](images/make_packet.png "Make packet function")
* This function is called from rdt_send() in order to create a packet list without cluttering the main send function
* This could also be used in other ways to append various forms of data such as the ACK packet sent from the server with
* The SEQ number is passed at all times in order to keep track within sender/receiver sides

</br>

### **UDP_client.py: corrupt_ack() & corrupt_data()**
![corrupt.png](images/corrupt.png "corrupt functions")
* These functions take in the data/ack and then checks if the packets should be corrupted or not based on error_chance and random values
* random method randbytes(# bits) creates a random string of bytes and then creates a new "data packet" to send back to receiver

</br>
### **UDP_client.py: Timeout **
![send_timer.png](images/send_timer.png "timeout handling")

</br>


### **UDP_client.py: corrupt_menu()**
![corrupt_menu.png](images/corrupt_menu.png "corrupt menu function")
* Simply takes in the user's input in order to push this info to the sender/receiver

</br>

## Execution Example
---------------------------------------------------------------------------
### **Command**
![start_command.png](images/commands.png "Run command")

</br>

### **User Input and Results**
![result1.png](images/results.png "Result after command")

</br>

