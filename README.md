# gbpb-asgmt3

##ftp_server.py
The server can be run by typing python3 ftp_server.py in terminal.
It should always be runnning in order for the client to connect.
While it is running, the client can connect and send commands to the server.
If command is "LIST", it will list all files in current directory.
If command is "RETRIEVE", it will retrieve the given file from the server
If command is "STORE", it will store the file sent by the client in the server.
If command is "QUIT", the client socket is closed. 
##ftp_client.py
The client can be run by typing python3 ftp_client.py in the terminal as long as the server is running.
The client takes the users inputs as commands.
If the command is "CONNECT", the client will connect for the server, which will allow other commands to be run.
If command is "LIST", the command is sent to the server and the response recieved from the server is printed out.
If command is "RETRIEVE", the user input is sent to the server and the file retrieved is written when returned.
If command is "STORE", the file is read to the server.
If command is "QUIT", the client socket closes and the program terminates.
