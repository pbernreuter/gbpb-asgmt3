from socket import *
import os

while True:
    user_input = input("Type: \"CONNECT <server_address> <server_port>\" to begin")
    if user_input.startswith("CONNECT"):
        command, server_address, server_port = user_input.split()
        server_port = int(server_port)
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((server_address,server_port))
        while True:
            user_input = input("Enter command:")
            if user_input.startswith("QUIT"):
                print("Disconnecting from server...")
                #send quit to server
                #close socket
                client_socket.close()
                break
            elif user_input.startswith("LIST"):
                client_socket.send(user_input.encode())
            elif user_input.startswith("RETRIEVE"):
                #retrive
                client_socket.send(user_input.encode())
            elif user_input.startswith("STORE"):
                #store
                client_socket.send(user_input.encode())
            else:
                print("Invalid Command")




