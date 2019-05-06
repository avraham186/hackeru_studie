#!usr/bin/env python

from scapy.all import *
send(IP(dst="192.168.1.33")/fuzz(ICMP()), loop=1)
