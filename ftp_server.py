from socket import * 
import os

# Create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number and bind it to server socket
serverSocket.bind(('', 6789))

# Listen for 1 connection at a time
serverSocket.listen(1)  

try:
    # Loop to keep the server running
    while True:
    
        # Set up a new connection from the client
        clientSocket, addr = serverSocket.accept()

        while True:
            # Receive message from the client
            message = clientSocket.recv(1024).decode()
            message = message.split()

            if message[0] == "LIST":
                # Send the list of files in the current directory
                file_list = '\n'.join(os.listdir('.'))
                clientSocket.send(file_list.encode())
            
            elif message[0] == "RETRIEVE":
                filename = message[1]
                if os.path.exists(filename) and os.path.isfile(filename):
                    with open(filename, 'rb') as file:
                        clientSocket.send(file.read())
                else:
                    clientSocket.send("File not found".encode())

            elif message[0] == "STORE":
                filename = message[1]
                file_data = clientSocket.recv(1024)
                with open(filename, 'wb') as file:
                    file.write(file_data)

            elif message[0] == "QUIT":
                clientSocket.close()
                break

except KeyboardInterrupt:
    print("Server terminated by user.")
    serverSocket.close()

    