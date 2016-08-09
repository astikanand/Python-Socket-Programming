#!/usr/bin/python
import socket,pickle

serverSocket = socket.socket()

host = socket.gethostname()
port = 8888
serverSocket.bind((host,port))

serverSocket.listen(5)

while True:
    clientSocket, addr = serverSocket.accept()
    print "Got Connection from", str(addr)

    clientSocket.send("Thanks for connecting!!")
    dict = {}

    while True:
       if clientSocket.recv(1024)!= "y":
           break

       command = clientSocket.recv(1024)
       response = pickle.loads(command)

       if response[0]=="set":
           dict[response[1]]=response[2]
           clientSocket.send("Key Value set successful")
       elif response[0]=="get" and dict.has_key(response[1]):
           clientSocket.send(dict[response[1]])
       else:
           clientSocket.send("Error occurred check again!!!")

    f = open("myfile.dat", "w+")
    f.write(str(dict))
    f.close()
    clientSocket.close()
    print "Connection closed from", str(addr)
