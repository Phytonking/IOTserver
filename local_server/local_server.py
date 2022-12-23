#from flask import flask
import socket
from command_manager import command_center
from configuration.tools import *
import configuration.boot_up as BU
import sys
import os
import time
import autonomous

BU.startup()
running = True
#check variables and statuses
print("PYTHONIOT SYSTEM v.0.0.1 ")
if sys.argv[1] == "--commands" or sys.argv[1] == "-c":
    while running:
        inp = input(">>> ")
        command_center(inp)
elif sys.argv[1] == "--autonomous" or sys.argv[1] == "-a":
    autonomous.main()
else:
    print("Invalid input")
    print("Run program by using: python3 local_server.py <command-ticker>")

            
    

        











"""
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
except OSError:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     
 
# put the socket into listening mode
s.listen(5)    
print("socket is listening") 

#NEVER DOUBT YOURSELF
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
        
"""