#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331    # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
arr = data.split()
hashfunc = arr[12]
print(hashfunc)
val = arr[15]
print(val)
while "Find" in data:
	print(data)
	h = hashlib.new(hashfunc)
	h.update(val)
	out = h.hexdigest()
	s.send(bytes(out + "\n"))
	data = s.recv(1024)
	if "Find" in data:
		arr = data.split()
		hashfunc = arr[4]
		print(hashfunc)
		val = arr[7]
		print(val)

print(data)

# close the connection
s.close()
