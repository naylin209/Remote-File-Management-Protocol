Remote controlling protocols such as Telnet and SSH are used to remotely run commands on other devices without the need to physical direct interaction with these devices. In this project you will design and develop a simple application layer protocol that help folders and files management on servers. 
You have to write Python3 code to implement the Remote File Management Protocol (RFMP) which is designed to serve a remote controlling application.  
RFMP has three phases: setup phase, operation phase, and closing phase. 

Packets to be sent in order:

1) SS: Start Packet: asks user whether it's a secure communication or not [0 for not secure, 1 for secure] and sends packet type, protocol name, version and secure as a packet
   Client --> Server
   
2) CC: Confirmation Packet: confirming that a packet has been sent, if not secure it sends back only the packet type (CC) but if secure it sends (CC, public key)
   Public key will later be used to encrypt & decrypt the session key
   Server --> Client
   
3) EC: Encryption Packet: if it is secure, it will return the packet as (packet type (EC), algorithm used, session key, public key)
   
