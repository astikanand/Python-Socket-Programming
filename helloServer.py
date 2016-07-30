#!/usr/bin/python

#Import modules for working of application
import socket

#Create a socket object: the end point for communication
#SOCK_STREAM for TCP
serverSocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

#Get local machine name
host = socket.gethostname()

#Set port number for communication b/w 1024 to 65655
port = 8180

#bind port and host to give it a unique phone number for communication
serverSocket.bind((host,port))

#queue upto 5 requests
serverSocket.listen(5)

# Server ready to serve client
while True:
    #establish a connection
    clientSocket, addr = serverSocket.accept()

    #print a message on server terminal to show connection from client
    print "Got a connection from ", str(addr)

    #create a message to send to client
    message = "Hello! Thank You for connecting."+"\r\n"

    #message to send to client
    clientSocket.send(message)

    #close the connection
    clientSocket.close()
