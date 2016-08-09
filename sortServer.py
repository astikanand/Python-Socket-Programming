#!/usr/bin/python

import socket,pickle

# Create socket object
serverSocket = socket.socket()

# Bind host and port
host = socket.gethostname()
port = 8888
serverSocket.bind((host,port))

# Keep in listening state
serverSocket.listen(5)


while True:
    # accept connections now
    clientSocket, addr = serverSocket.accept()
    print "Got Connection from", str(addr)

    # send connection confirmation message
    clientSocket.send("Thank You for connecting")

    # while msg from client to use server
    while True:

        if clientSocket.recv(1024)!="y":
            break
            
        # received the dump list
        myList = clientSocket.recv(4096)

        # Undump or load list received from client
        data = pickle.loads(myList)

        # sort the list
        data.sort()
        data.reverse()

        # dump and send it
        clientSocket.send(pickle.dumps(data))

    # close the connection
    print "Connection closed from", str(addr)
    clientSocket.close()
