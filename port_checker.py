#!/usr/bin/python

from socket import *
ports = [80,
443,
9111,
8585,
21,
23,
22,
]


for i in ports:
	print i

	try:

		s = socket()
		s.connect(("10.0.0.13", i))
		print "this port is open"
		s.send("\r\n")
		banner = s.recv(2048)
		print banner
		s.close()

	except:
		print "close"
