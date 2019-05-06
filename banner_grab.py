#!/usr/bin.python
from socket import *
s = socket()
s.connect(("10.0.0.13", 21))
s.send("\r\n")
banner = s.recv(2048)

print banner
s.close()
