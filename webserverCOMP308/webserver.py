from socket import *
import os

serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the server socket to the specified IP address and port
serverSocket.bind(('127.0.1.1', serverPort))

# Display the IP address and port the server is running at
print("Server is running at {}:{}".format('127.0.1.1', serverPort))

serverSocket.listen(1)
print('The web server is up on port:', serverPort)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1].decode()[1:]

        if os.path.isfile(filename):
            with open(filename, "rb") as file:
                outputdata = file.read()
                connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')
                connectionSocket.sendall(outputdata)
        else:
            # Send 404 Not Found response with an HTML page
            html_content = "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1></body></html>"
            response = "HTTP/1.1 404 Not Found\r\n\r\n" + html_content
            connectionSocket.send(response.encode())
        
        connectionSocket.close()

    except Exception as e:
        print("Error:", e)
        connectionSocket.send(b'HTTP/1.1 500 Internal Server Error\r\n\r\n')
        connectionSocket.close()

serverSocket.close()
