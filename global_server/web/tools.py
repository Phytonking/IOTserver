from web import *
import requests

def syncDeviceInfoToInterface(device):
    #CHANGE REQUEST URL LATER FOR PRODUCTION AND DEPLOYMENT
    device_dict = {"device_id": device.device_id, "device_name":device.device_name,  "ip_address":device.ip_address}
    req = requests.post("http://127.0.0.1:8000/syncup", json={'username':device.owner.username, 'password':device.owner.password, 'information_type':0, 'data':device_dict})
    if req.status_code == 200:
        print("REQUEST SENT SUCCESSFULLY")
    else:
        print(f"{req.status_code} Error occured in sync")