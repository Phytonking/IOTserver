# Import socket module
import socket	
import time		

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 2424			

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
s.send("request".encode())
try:
    while True:
        print(s.recv(1024).decode())
except KeyboardInterrupt:

    
# close the connection
    s.close()	
	
