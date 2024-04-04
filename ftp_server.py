#Parker Bernreuter & Gabe Baksa
#04/06/2021

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

            # List the files in the server directory
            if message[0] == "LIST":
                # Send the list of files in the current directory
                file_list = '\n'.join(os.listdir('.'))
                clientSocket.send(file_list.encode())
            
            # Retrieve the file requested by the client
            elif message[0] == "RETRIEVE":
                #Get the filename from the message
                filename = message[1]
                #Check if the file exists in the server directory
                if os.path.isfile(filename):
                    #Send the file to the client
                    with open(filename, 'rb') as file:
                        clientSocket.send(file.read())
                else:
                    clientSocket.send("File not found".encode())

            # Store the file sent by the client
            elif message[0] == "STORE":
                #Get filename and file data
                filename = message[1]
                file_data = clientSocket.recv(1024)
                #Write the file data to the server directory
                with open(filename, 'wb') as file:
                    file.write(file_data)

            # Close the connection if the client sends a QUIT message 
            elif message[0] == "QUIT":
                clientSocket.close()
                break

# Close the server socket and terminate the program
except KeyboardInterrupt:
    print("Server terminated by user.")
    serverSocket.close()

    