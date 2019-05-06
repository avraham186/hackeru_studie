#!/usr/bin/env python
	#imports
from scapy.all import *
from socket import *
	#create a new socket instance using udp (sock dgram)
#socket, AF_INET, SOCK_DGRAM
sock = socket(AF_INET, SOCK_DGRAM)
	#we connect to 1.1.1.1 dns server on port 53
sock.connect(("1.1.1.1", 53))
	#we built an legal  dns packet
dnsQ = DNS(rd=1, qd=DNSQR(qname="ynaet.co.il"))
	#cast it to a string (in order to send out)
dnsstring = str(dnsQ)
	#sending the string packet
sock.send(dnsstring)
	#and reciving the respons and casting it back to dns
ls(DNS(sock.recv((4096))))
