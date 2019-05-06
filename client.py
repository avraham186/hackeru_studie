#!/usr/bin/python
from socket import *
s = socket()
ip = "192.168.1.111"
s.connect((ip, 8086))
s.send("hi")
data = s.recv(2048)
print data
s.close()
