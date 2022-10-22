#This is where you can write your commands
import socket
from tools import *
import boot_up
import sys
import os
import variables
import time

def command_center(command):
    if "send_global" in command:
        update_global(command)
    elif "exit" in command:
        sys.exit()
    else:
        print("Command Not Found")

def update_global(com):
    args = com.split()
    x = find_variables_and_statuses()
    #print(x)
    if len(args) > 1 and args[1] == "-c":
        while True:
            try:
                new = variables.find_new_vars_and_stats(x)
                #print(new)
                con = get_config()
                send_post_to_global(server_route="/recieve", request_data={"device_id":con["device_id"],"new_variables": new[0], "new_statuses": new[1], "variables_to_update":x[0], "status":x[1], "username":con["username"], "password":con["password"]})
            except KeyboardInterrupt:
                break
            time.sleep(5)
    else:
        try:
            new = variables.find_new_vars_and_stats(x)
            #print(new)
            con = get_config()
            send_post_to_global(server_route="/recieve", request_data={"device_id":con["device_id"],"new_variables": new[0], "new_statuses": new[1], "variables_to_update":x[0], "status":x[1], "username":con["username"], "password":con["password"]})
        except KeyboardInterrupt:
            return False
    