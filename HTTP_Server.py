# import socket module
from socket import *


import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
# Fill in start
HOST = '10.10.63.19'
PORT = 8765
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
# Fill in end
print('Ready to serve...')
while True:
    # Establish the connection


    connectionSocket, addr = serverSocket.accept()
    print('  Local Server:  Accepting connection to ' + str(addr))
    size = 1024
    try:
        message = connectionSocket.recv(size)

        print(message)

        filename = message.split()[1]
        print("file " + str(filename[1:]))
        f = open(filename[1:])
        outputdata = f.read()  # Fill in start #Fill in end
        print("here")
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send(('HTTP/1.1 200 OK\r\n\r\n').encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send(("404 NOT FOUND").encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
