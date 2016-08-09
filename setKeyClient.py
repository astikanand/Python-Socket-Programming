#!/usr/bin/python
import socket,pickle

clientSocket = socket.socket()

host = socket.gethostname()
port = 8888

clientSocket.connect((host,port))

print clientSocket.recv(1024)

while True:
    msg = raw_input("\nEnter y to continue or n to exit : ")
    clientSocket.send(msg)

    if msg == "y":
        # ask user input
        ask = raw_input("Enter the command : ")
        command = map(str, ask.split())

        if command[0]=="set":
            clientSocket.send(pickle.dumps(command))
            print clientSocket.recv(1024)
        elif command[1]=="get":
            clientSocket.send(pickle.dumps(command))
            print "For Key = ", command[1]
            print "Value = ", clientSocket.recv(1024)
        else:
            clientSocket.send(pickle.dumps(command))
            print clientSocket.recv(1024)
    else:
        print "Thanks for connecting. See You again!!"
        break
clientSocket.close()
