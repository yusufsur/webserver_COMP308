import sys
from socket import *

def http_client(server_host, server_port, filename):
    # Create a socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    
    # Connect to the server
    clientSocket.connect((server_host, server_port))
    
    # Send HTTP GET request
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    clientSocket.send(request.encode())
    
    # Receive and display the server response
    response = clientSocket.recv(4096).decode()
    print(response)
    
    # Close the socket
    clientSocket.close()

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python client.py server_host server_port filename")
        sys.exit(1)
    
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
    
    # Request an existing file
    http_client(server_host, server_port, filename)

    # Request a non-existing file
    http_client(server_host, server_port, "NonExistingFile.html")
