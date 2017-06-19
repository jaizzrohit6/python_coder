#!/usr/bin/python
import socket
var=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
var.bind(("",8760))
ap=[]
extract=var.recvfrom(100)
print extract[0]
ip_port=extract[1]
ip=ip_port[0]

port=ip_port[1]

while 1:

	ss=raw_input("enter msg:")
	var.sendto(ss,(ip,port))	
	message=var.recvfrom(100)
	print message[0]
	


