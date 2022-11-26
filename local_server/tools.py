import requests
import json
import subprocess
import os
import sys
from errors import *
import re

information = None
def grab_config():
    file = open("config.json", "r")
    global information
    information = json.loads(file.read())

def update_config(x):
    fil = open("config.json", "w")
    fil.write(json.dumps(x))
    fil.close()


def get_data_ID():
    f = open("config.json", "rt")
    info = json.loads(f.read())
    print(info["device_id"])
    return info["device_id"]

def get_config():
    file = open("config.json", "r")
    global information
    information = json.loads(file.read())
    return information    

def find_nearest_server():
    servers_raw = open("servers.txt","rt")
    servers = servers_raw.read().split("\n")
    if "" in servers:
        servers.remove("")
    print(servers) 
    average_ping = 0.0
    server_ping_averages = []
    result = None
    for y in servers:
        average_ping = 0.0
        for x in range(0,65):
            try:
                result = subprocess.run(['ping', '-c', '1', y],text=True,capture_output=True,check=True)
                for line in result.stdout.splitlines():
                    #print(line)
                    if "icmp_seq" in line:
                        timing = float(line.split('time=')[-1].split(' ms')[0])
                        #print(timing)
                        average_ping += timing
            except subprocess.CalledProcessError:
                #print(result.returncode)
                #print(result.output)
                break 
        if average_ping > 0.0000:                   
            average_ping /= 64
            server_ping_averages.append({"server": y, "ping":average_ping})
        else:
            server_ping_averages.append({"server": y, "ping":None, "error":"Server could not be located"})    
        
    #return server_ping_averages
    #find and return nearest, connectable server.
    fastest_server = None
    for ku in server_ping_averages:
        if ku['ping'] == None:
            continue
        if fastest_server == None:
            fastest_server = ku
            continue
        if ku['ping'] < fastest_server['ping']:
            fastest_server = ku
            continue
        else:
            continue

    if fastest_server != None:
        return fastest_server["server"]
    else:
        return None                
        



def send_post_to_global(server_route, request_data): #sends the data to global 
    print("Processing data to global servers")
    print(request_data)
    req = requests.post("http://"+find_nearest_server()+server_route, json=request_data)
    print(req.json())



def connect_to_global():
    try:
        r = requests.get("http://"+information["nearest_server"])
        if r.status_code == 200:
            return True
        else:
            return False    
    except requests.exceptions.ConnectionError:
        raise ConnectionEror("COULD NOT CONNECT TO SERVER")


def check_if_registered():
    #checks if the server is registered and exists globally. 
    x = connect_to_global()
    print(information)
    if x:
        try:
            request = requests.post("http://"+information["nearest_server"]+'/check_registration', json={"username":information["username"], "password":information["password"], "device_id":information["device_id"]}) #send global request.
        except KeyError:
            #set device_id
            d_id = input("Set Device ID: ")
            information.update({"device_id":d_id})
            update_config(information)
            request = requests.post("http://"+information["nearest_server"]+'/check_registration', json={"username":information["username"], "password":information["password"], "device_id":information["device_id"]})
        j = request.json()
        #print(request.message)
        if request.status_code != 200:
            if j['error'] == -1:
                raise ConnectionError("NOT ENOUGH INFORMATION TO REGISTER/CONNECT: Error Code -1")
            elif j['error'] == -2:
                raise AccountNotFoundError("NO ACCOUNT FOUND: Error Code -2")   
            elif j['error'] == 0:
                print("Account not logged into server, Logging Account in")
                login_req = send_post_to_global('/login', {"username": information["username"], "password":information["password"]})
        if request.status_code == 200:
            print(j['Message'])

def find_variables_and_statuses():
    variables = []
    statuses = []
    if len(os.listdir('device-information')) == 0:
        print("PLEASE SET VARIABLES AND STATUSES: check <website> for instructions")
        sys.exit()
    else:
        for x in os.listdir('device-information'):
            print(x.split('.'))
            file_type = x.split('.')[1]
            infor = {}
            h = open(f"device-information/{x}", "r")
            lines = h.read().split('\n')
            for i in lines:
                y = re.split(":", i)
                if file_type == "var":
                    infor["name"] = y[0]
                    infor["value"] = y[1]
                    variables.append(infor)
                    continue

                elif file_type == "stat":
                    infor["name"] = y[1]
                    statuses.append(infor)
                    continue 

    return [variables, statuses]                     
#print(find_nearest_server())
