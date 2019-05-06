#!/usr/bin/python

from socket import *
s = socket()
s.bind(("0.0.0.0", 8086))
s.listen(3)
print "server is up"
var1, var2 = s.accept()
print "this is the client addres", var2
data = var1.recv(2048)
print "this is the data: ", data
var1.send("some data")
var1.close()
s.close()
