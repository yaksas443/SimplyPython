#!/usr/bin/env python
import socket
import struct
import binascii

#To check the protocol value look at the includes /usr/include/linux/if_ether.h 

rawSocket =  socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
pkt = rawSocket.recvfrom(2048)

ethernetHeader =  pkt[0][0:14]

#First six bytes - destination MAC addess
#Next six bytes - source MAC address
#Last 2 bytes - Ether type
# ! - unpacking in network byte order
#6s - take 6 unsigned characters togther


eth_hdr = struct.unpack("!6s6s2s",ethernetHeader)

print "Destination MAC: " + binascii.hexlify(eth_hdr[0])
print "Source MAC: " + binascii.hexlify(eth_hdr[1])
print "EtherType: " + binascii.hexlify(eth_hdr[2])

# IP header 20 bytes long

ipHeader = pkt[0][14:34]

ip_hdr = struct.unpack("!12s4s4s",ipHeader)

#First 12 bytes - not relevant
#Next 4 bytes - source IP address
#Next 4 bytes - destination IP address

print "Soruce IP address: " + socket.inet_ntoa(ip_hdr[1])
print "Destination IP address: " + socket.inet_ntoa(ip_hdr[2])

tcpHeader = pkt[0][34:54]

tcp_hdr = struct.unpack("!HH16s",tcpHeader)

print "Source port is: " + str(tcp_hdr[0])
print "Destination port is: " + str(tcp_hdr[1])


