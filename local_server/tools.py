import requests
import json
import subprocess

from errors import AccountNotFoundError, ConnectionEror

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

def find_nearest_server():
    servers_raw = open("servers.txt","rt")
    servers = servers_raw.read().split("\n")   
    print(servers) 
    average_ping = 0.0
    server_ping_averages = []
    result = None
    for y in servers:
        average_ping = 0.0
        for x in range(0,65):
            try:
                result = subprocess.run(['ping', '-c', '1', y.split()[0]],text=True,capture_output=True,check=True)
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
        



def send_post_to_global(server_route, request): #sends the data to global 
    print("Processing data to global servers")
    request = requests.post(find_nearest_server()+server_route, data=json.dumps(request))




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
            request = requests.get("http://"+information["nearest_server"]+'/check_registration', json={"username":information["username"], "password":information["password"], "device_id":information["device_id"]}) #send global request.
        except KeyError:
            #set device_id
            d_id = input("Set Device ID: ")
            information.update({"device_id":d_id})
            update_config(information)
            request = requests.get("http://"+information["nearest_server"]+'/check_registration', json={"username":information["username"], "password":information["password"], "device_id":information["device_id"]})
        j = request.json()
        #print(request.message)
        if request.status_code != 200 and j['Message'] == 'ERROR':
            if j['error'] == -1:
                raise ConnectionError("NOT ENOUGH INFORMATION TO REGISTER/CONNECT: Error Code -1")
            elif j['error'] == -2:
                raise AccountNotFoundError("NO ACCOUNT FOUND: Error Code -2")    
        if request.status_code == 200:
            print(j['Message'])


#print(find_nearest_server())
