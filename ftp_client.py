from socket import *
import os

# Loop to keep the client running
while True:
    # Get user input to connect to the server
    user_input = input("Type: \"CONNECT <server_address> <server_port>\" to begin: ")

    if user_input.startswith("CONNECT"):
        # Get the server address and port number from the user input 
        command, server_address, server_port = user_input.split()
        server_port = int(server_port)
        # Create a TCP client socket
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((server_address,server_port))
        # Loop to keep the client running while connected to server
        while True:
            # Get user input for the command to send to the server
            user_input = input("Enter command:")
            
            #end connection if user enters QUIT
            if user_input.startswith("QUIT"):
                break

            #send command and recieve and print server response
            elif user_input.startswith("LIST"):
                client_socket.send(user_input.encode())
                response = client_socket.recv(1024).decode()
                print("Server response:\n", response)

            #send filename to server and recieve and write file
            elif user_input.startswith("RETRIEVE"):
                client_socket.send(user_input.encode())
                user_input = user_input.split()
                filename = user_input[1]
                response = client_socket.recv(1024)
                with open(filename, 'wb') as file:
                    file.write(response)
                print("Retrieved " + filename + "from server.\n")

            #send filename and file to server
            elif user_input.startswith("STORE"):
                client_socket.send(user_input.encode())
                user_input = user_input.split()
                filename = user_input[1]
                if os.path.isfile(filename):
                    with open(filename, 'rb') as file:
                        client_socket.send(file.read())
                    print(filename + " stored in server\n")
                else:
                    print("File not found")
            
            #if user enters invalid command
            else:
                print("Invalid Command")

    #end connection if user enters QUIT and close socket
    if user_input.startswith("QUIT"):
        print("Disconnecting from server...")
        #send quit to server
        client_socket.send(user_input.encode())
        #close socket
        client_socket.close()
        print("Client program terminated.")
        break
    else:
        print("Invalid Command. Try again.")




