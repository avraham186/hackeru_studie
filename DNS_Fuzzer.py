#! usr/bin/env python
from scapy.all import *
dns = send(IP(dst="1.1.1.1")/UDP()/fuzz(DNS()), LOOP=1
