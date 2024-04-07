from socket import *

serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the server socket to the specified IP address and port
serverSocket.bind(('', serverPort))

# Get the IP address corresponding to the hostname
ip_address = gethostbyname(gethostname())

# Display the IP address and port the server is running at
print("Server is running at {}:{}".format(ip_address, serverPort))

serverSocket.listen(1)
print('the web server is up on port:', serverPort)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        
        f = open(filename[1:])
        outputdata = f.read()
        
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
        connectionSocket.close()

serverSocket.close()
