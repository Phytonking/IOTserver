#This is where you can write your commands
import socket
from configuration.tools import *
import configuration.boot_up
import sys
import os
import time

variables_to_delete = []
statuses_to_delete=[]
variables_to_add = []
statuses_to_add = []
variables_to_update = []


def update_global(status):
    global variables_to_add, variables_to_delete, statuses_to_add, statuses_to_delete, variables_to_update
    add_variable_or_status_files()
    #x = find_variables_and_statuses()
    #print(x)
    try:
        con = get_config()
        send_post_to_global(server_route="/recieve", request_data={"device_id":con["device_id"],"new_variables": variables_to_add, "new_statuses": statuses_to_add, "variables_to_update":variables_to_update, "variables_to_delete":variables_to_delete, "statuses_to_delete":statuses_to_delete, "status":status, "username":con["username"], "password":con["password"]})
        update_variable_files()
        del variables_to_add, statuses_to_add, variables_to_delete, statuses_to_delete, variables_to_update
    except KeyboardInterrupt:
        return False


def delete_variable_or_status(dType, name):
    args = com.split()
    if dType == "-v":
        directory = os.listdir("device-information")
        if f"{name}.var" in directory:
            variables_to_delete.append(name)
            print(f"{name} marked for deletion, run \"send_global\" for changes to take place")
        else:
            print(f"Could not find variable {name}")
    elif dType == "-s":
        directory = os.listdir("device-information")
        if f"{name}.stat" in directory:
            statuses_to_delete.append(name)
            print(f"{name} marked for deletion, run \"send_global\" for changes to take place")
        else:
            print(f"Could not find status {name}")
    else:
        print("Invalid Input")

def add_variable_or_status(dType, name, value):
    global variables_to_add, variables_to_delete, statuses_to_add, statuses_to_delete, variables_to_update
    if dType == "-v":
        variables_to_add.append({f"{name}":f"{value}"})
    elif dType == "-s":
        statuses_to_add.append({"name":f"{name}"})
    else:
        print("Invalid Input")


def add_variable_or_status_files():
    global variables_to_add, variables_to_delete, statuses_to_add, statuses_to_delete, variables_to_update
    for v in variables_to_add:
        try:
            new_variable_file = open(f"device-information/{list(v.keys())[0]}.var", "x")
            new_variable_file.write(f"{list(v.keys())[0]}:{v[list(v.keys())[0]]}")
            new_variable_file.close()
        except FileExistsError:
            continue
    for s in statuses_to_add:
        try:
            fil = s["name"]
            new_status_file = open(f"device-information/{fil}.stat", "x")
            new_status_file.write(f"name:{fil}")
            new_status_file.close()
        except FileExistsError:
            continue


def update_variable(variable, value):
    global variables_to_add, variables_to_delete, statuses_to_add, statuses_to_delete, variables_to_update
    #l = input("set value: ")
    variables_to_update.append({f"{variable}":f"{value}"})


def update_variable_files():
    global variables_to_add, variables_to_delete, statuses_to_add, statuses_to_delete, variables_to_update
    for v in variables_to_update:
        try:
            new_variable_file = open(f"device-information/{list(v.keys())[0]}.var", "w")
            new_variable_file.write(f"{list(v.keys())[0]}:{v[list(v.keys())[0]]}")
            new_variable_file.close()
        except FileNotFoundError:
            print("could not process variable")
            continue