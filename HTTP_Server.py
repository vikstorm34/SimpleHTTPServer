from socket import *
from threading import Thread
import os.path
from os import path
import sys  # In order to terminate the program


class ConnectionThread(Thread):

    def __init__(self, IP, PORT):
        Thread.__init__(self)
        self.IP = IP
        self.PORT = PORT

    def run(self):

        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            print("File Exists: " + str(path.exists(filename[1:])))

            f = open(filename[1:])
            outputdata = f.read()

            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n", "UTF-8"))
            connectionSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)

HOST = '10.10.62.135'
PORT = 8765
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

threads = []

print('Ready to serve...')
while True:
    connectionSocket, addr = serverSocket.accept()
    print('  Local Server:  Accepting connection to ' + str(addr))

    nextThread = ConnectionThread(addr[0], addr[1])
    nextThread.start()
    threads.append(nextThread)

    for thread in threads:
        thread.join()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
