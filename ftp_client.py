from socket import *
import os

while True:
    user_input = input("Type: \"CONNECT <server_address> <server_port>\" to begin: ")
    if user_input.startswith("CONNECT"):
        command, server_address, server_port = user_input.split()
        server_port = int(server_port)
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((server_address,server_port))
        while True:
            user_input = input("Enter command:")
            if user_input.startswith("QUIT"):
                break
            elif user_input.startswith("LIST"):
                client_socket.send(user_input.encode())
                response = client_socket.recv(1024).decode()
                print("Server response:\n", response)
            elif user_input.startswith("RETRIEVE"):
                client_socket.send(user_input.encode())
                user_input = user_input.split()
                filename = user_input[1]
                response = client_socket.recv(1024).decode()
                with open(filename, 'wb') as file:
                    file.write(response)
                print("Retrieved " + filename + "from server.\n")
                client_socket.send(user_input.encode())
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
            else:
                print("Invalid Command")
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




