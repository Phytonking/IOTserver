from atexit import register
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from web.models import *
from hashlib import *
import web.tools
# Create your views here.


def index(request):
    return JsonResponse({"Message": "Welcome to the global server"}, status=200)

@csrf_exempt
def check_registration(request):
    if request.method == "POST":
        x = json.loads(request.body)
        print(x)
        try:
            deviceId = x["device_id"]
            username = x["username"]
            password = x["password"]
        except KeyError:
            print({"Message":"ERROR", "error":-1})
            return JsonResponse({"Message":"ERROR", "error":-1}, status=403)  
        try:    
            dev = device.objects.get(device_id=deviceId)
            return JsonResponse({"Message": f"Device {dev.device_id} has been registered"},status=200)
        except device.DoesNotExist:
            print({"Message":"ERROR", "error":-3})
            #return JsonResponse({"Message":"ERROR", "error":-3}, status=403)
            try:
                user = u.objects.get(username=username, password=password)
                newDev = device(device_id=deviceId, device_name=f"{username}'s device", owner = user, ip_address = request.META.get('REMOTE_ADDR'))
                newDev.save()
                web.tools.syncDeviceInfoToInterface(newDev)
                return JsonResponse({"Message": "Device has been registered"},status=200)
            except u.DoesNotExist:    
                print({"Message":"ERROR", "error":-2})
                return JsonResponse({"Message":"ERROR", "error":-2}, status=404)
                
        


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Username=data["username"]
        Password=data["password"]
        try:
            user = u.objects.get(username=Username)
            if Password == user.password:
                user.logged_in = True
                user.save()
        except u.DoesNotExist:
            return JsonResponse({"Message":"Error", "error":-2}, status=403)        

        return JsonResponse({"Message": "Logged in as"+str(Username)}, status=200)    
    else:
        return JsonResponse({"Message":"Login"}, status=200)

#add new information to this server
@csrf_exempt
def recieve(request):
    if request.method == "GET":
        return JsonResponse({"Message":"POST REQUESTS ONLY"}, status=200)
    if request.method == "POST":
        import web.models 
        sender_information = json.loads(request.body)
        dev = web.models.device.objects.get(device_id=sender_information["device_id"])
        Username=sender_information["username"]
        Password=sender_information["password"]
        try:
            user = web.models.u.objects.get(username=Username)
        except web.models.u.DoesNotExist:
            return JsonResponse({"Message":"Error", "error":-2}, status=403)
        if user.password != Password:
            return JsonResponse({"Message":"Error", "error":1}, status=403)    
        if dev.owner.logged_in != True:
            return JsonResponse({"Message":"Error", "error":0}, status=403)    
        #variables = device_variables.objects.filter(from_device=dev)
        try:
            statuses = web.models.device_statuses.objects.filter(for_device=dev)
            current_status = web.models.current_device_status.objects.get(for_device=dev)
        except web.models.current_device_status.DoesNotExist:
            pass  
        #check for new variables
        if sender_information["new_variables"] != None:
            for n in sender_information["new_variables"]:
                print(n)
                is_it_there = web.models.device_variables.objects.filter(variable_name=n["name"],from_device=dev).count()
                if is_it_there == 1:
                    continue
                elif is_it_there > 1:
                    web.models.device_variables.objects.filter(variable_name=n["name"],from_device=dev).delete()
                    var = web.models.device_variables(from_device=dev, variable_name=n["name"], value=n["value"], value_type=str(type(n["value"])))
                    var.save()
                    continue
                else:
                    var = web.models.device_variables(from_device=dev, variable_name=n["name"], value=n["value"], value_type=str(type(n["value"])))
                    var.save()
                    continue
        #check for new statuses
        if sender_information["new_statuses"] != None:
            for x in sender_information["new_statuses"]:
                print(x)
                is_stat_there = web.models.device_statuses.objects.filter(status_name = x, for_device=dev).count()
                if is_stat_there == 1:
                    continue
                elif is_stat_there > 1:
                    web.models.device_statuses.objects.filter(status_name = x, for_device=dev).delete()
                    stat = web.models.device_statuses(status_name=x, for_device=dev)
                    stat.save() 
                else:
                    stat = web.models.device_statuses(status_name=x, for_device=dev)
                    stat.save()    
        #update variable values
        if sender_information["variables_to_update"] != None:
            for y in sender_information["variables_to_update"]:
                print(y)
                try:
                    vari = web.models.device_variables.objects.get(from_device=dev,variable_name=y["name"])
                    vari.value = y["value"]
                    vari.value_type = str(type(y["value"]))
                    vari.save()
                except web.models.device_variables.DoesNotExist:
                     return JsonResponse({"Message":"Error", "error":0}, status=400)   
        #update current_status
        if sender_information["status"] != None:
            for u in statuses:
                if u.status_name == sender_information["status"]:
                    current_status.current_status = u
                    current_status.save()
                    break
        #transfer new data across other global servers as nessesary
        return JsonResponse({"Message":"Data Recieved Successfully"}, status=200)

#send information out to the interface
@csrf_exempt
def send(request):
    #return "SEND"
    if request.method == "POST":
        data = json.loads(request.body)
        if data["action"] == "new_user":
            new_user = u(first_name = data["first_name"], last_name = data["last_name"], email = data["email"], username=data["username"], password = data["password"], account_user_serial_key = data['serial'], account_server_origin=data["origin"], logged_in=False)
            new_user.save()
        elif data["action"] == "new_device":
            new_device = device(device_id=data["device_id"], device_name=data["device_name"], owner=u.objects.get(username=data["owner"]), ip_address=data["ip"])
            new_device.save()
        return JsonResponse({"Message":"Data Recieved Successfully"}, status=200)
    if request.method == "GET":
    #refine data
        data = json.loads(request.body)
        Username=data["username"]
        Password=data["password"]
        try:
            user = u.objects.get(username=Username)
        except u.DoesNotExist:
            return JsonResponse({"Message":"Error", "error":-2}, status=403)    
        if user.password != Password:
            return JsonResponse({"Message":"Error", "error":1}, status=403)
    # get device
        try:
            dev = device.objects.get(device_id=data["device_id"])
        #find data
            variables = device_variables.objects.filter(from_device=dev)
            statuses = device_statuses.objects.filter(for_device=dev)
            current_status = current_device_status.objects.get(for_device=dev)
        #send_back
            return JsonResponse({"variables": variables, "current_status":current_status})
        except device.DoesNotExist:
            return JsonResponse({"Error": "Device not registered on the server!", "error_code":-1})