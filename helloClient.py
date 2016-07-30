#!usr/bin/python3.5

# import modules for working of application
import socket

# create a socket object : the end point of communication
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set the port number
port = 8180

# connect to hostname on port
clientSocket.connect((host,port))

# receive 1024 bytes at max
print clientSocket.recv(1024)

# close the connection
clientSocket.close()
