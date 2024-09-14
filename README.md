# Network Design: Principles, Protocols & Applications
Network design course repo for Summer 2023 with Professor Vinod Vokkarane
The TCP/IP stack has five layers, namely application, transport, network, link, and physical.

## [Phase 1](Phase_1/)
Implements the standard user datagram protocol (UDP) sockets. The intention is to transfer a message (Say “HELLO”) from the UDP client to the UDP server and then  ECHO the message back from the UDP server to the UDP client. Note that the client and server process can reside on the same host, but have to use different port numbers.  Make sure that your program can send and receive messages in both directions.
  - [x] UDP sending  
  - [x] UDP recieving
  - [x] Extra: Implement multithreading

## [Phase 2](Phase_2/)
To transfer a file between a UDP client process and a UDP server process. This is done by providing reliable data transfer (RDT) 1.0 service using the UDP connection developed in Phase 1. Ultimately sending and recieving data using packets, one at a time.
  - [x] Create packets
  - [x] Send packets
  - [x] recieve packets
  - [x] verify checksum
  - [x] repack into file

## [Phase 3](Phase_3/)
Uses the UDP sockets from Phase 2 to implement an RDT2.2 protocol that has sequence numbers, checksum and ACKs.
  - [x] Sequence numbers 
  - [x] Checksum
  - [x] ACKs

## [Phase 4](Phase_4/)
Implements RDT3.0 by adding a countdown timer feature onto the RDT2.2 that was done in Phase 3.
  - [x] Countdown timer
