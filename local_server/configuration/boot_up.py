#makes sure all parameters are set to run.
from configuration.tools import *
import subprocess
import json
from configuration.errors import *
import sys
information = {}

def set_global_server():
    print("Preparing global server conncections.")
    server = find_nearest_server()
    if server == None:
       raise NoServerAvailableError()
    else:
        information.update({"nearest_server": server})
        print(f"SERVER SET to {server}")



def login_credentials():
    login = {}
    print("Checking Login Credentials")
    f = open("configuration/config.json", "r")
    stuff = json.loads(f.read())
    in_config = None
    try:
        login["username"] = stuff["username"]
        login["password"] = stuff["password"]
        in_config = True
    except KeyError:
        username = input("Enter the Username: ")
        password = input("Enter the Password: ")  
        in_config = False
    
    information.update({"username": login["username"]})
    information.update({"password": login["password"]})
    k = open("configuration/config.json", "w")
    k.write(json.dumps(information))
    k.close()
    
    d_id = input("Set Device ID: ")
    information.update({"device_id":d_id})
    update_config(information)
    #send message to global servers about login info
    grab_config() #updates information in tools.py
    check_if_registered()
          
        
    

def startup():
    try:
        set_global_server()
    except NoServerAvailableError:
        print("No server could be connected.")
        sys.exit()

    login_credentials()  
