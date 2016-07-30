#!/usr/bin/python

import socket,pickle

# create socket object
clientSocket = socket.socket()

# Request Connection
host = socket.gethostname()
port = 8888
clientSocket.connect((host,port))

# Get connection confirmation
print clientSocket.recv(1024)

while True:
    # Ask user input whether to continue or exit
    msg = raw_input("\nEnter Yes to continue or No to exit : ")

    # send user response to server if response is no then client
    # get disconnected from server
    clientSocket.send(msg)

    # If yes continue fetching data from server
    if (msg == "Yes" or msg == "y" or msg=="yes"):

        # Ask user to enter list elements
        data = raw_input("Enter the list to sort: ")

        # split and map user input to int to get list
        myList = map(int, data.split())

        # list cant be send to sockets so dump it before sending using dumps()
        clientSocket.send(pickle.dumps(myList))

        # received dumped sorted list from server
        data1 = clientSocket.recv(1024)

        # befor printing undump or load data using loads()
        print pickle.loads(data1)

    # close connection if answer is not yes
    else:
        print "Thank for connecting. See You soon!"
        break

clientSocket.close()
