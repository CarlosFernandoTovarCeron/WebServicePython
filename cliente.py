#!/usr/bin/python

import socket
import sys

try: 
    # esta estructura permite capturar comportamientos anomalos
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg: # si es del tipo socket.error
	print "Failed to create socket. Error code: " + str(msg[0]) + ", error message: " + msg[1] 
	sys.exit()

print "Socket created"

host = "www.google.com"
# defina una variable port y almacene alli el numero 80
port = 80


try:
	# Connect the socket to the server
	remote_ip = socket.gethostbyname(host)
except socket.gaierror:
	print "Hostname could not be resolved. Exiting"
	sys.exit()

print ("La direccion IP de %s es %s" %(host,remote_ip))

endpoint = (remote_ip, port)

s.connect(endpoint)

print "Socket connected to " + host + " on ip " + remote_ip

# Datos a enviarse
message = "GET / HTTP/1.1\r\n\r\n"

try:
	 s.sendall(message.encode('utf-8'))
except socket.error:
	print "Send failed"
	sys.exit()

print "Message send successfullly"

# Recibiendo datos
reply = s.recv(160)
print reply
s.close()
