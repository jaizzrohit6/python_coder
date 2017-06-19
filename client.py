#!/usr/bin/python2
import socket
var=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.0.102"
s_port=8760
while 3>2 :
	#s_msg=var.recvfrom(100)
	#print s_msg[0]
	msg=raw_input("enter any maessage  :")
	var.sendto(msg,(s_ip,s_port))
	s_msg=var.recvfrom(100)
  	print s_msg[0]

