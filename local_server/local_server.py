#from flask import flask
import socket
from tools import *
import boot_up
import sys


boot_up.startup()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server socket has been activated")
except socket.gaierror:
    print("ERROR: Socket could not be activated")
    sys.exit()

port = 2424
#host = "0.0.0.0" # uncomment this code to run program on that ip_address. 

try:
    s.bind((host, port))        
    print(f"socket running on: {host}:{port}")
except NameError:
    print("HOST NOT FOUND: Redirecting to local host")
    s.bind(("", port))
    print(f"Running on 127.0.0.1:{port}")  
 
# put the socket into listening mode
s.listen(5)    
print("socket is listening") 


while True:
    c, addr = s.accept()    
    print('Got connection from', addr)
    data = c.recv(1024).decode()
    print("data recived")
    x = connect_to_global()
    if x:
        c.send("Great!".encode())
        print("data sent")
    else:
        print("data not sent")    
