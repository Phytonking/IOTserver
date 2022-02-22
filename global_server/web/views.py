from atexit import register
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from web.models import *
from hashlib import *
# Create your views here.


def index(request):
    return JsonResponse({"Message": "Welcome to the global server"}, status=200)

@csrf_exempt
def check_registration(request):
    if request.method == "GET":
        x = json.loads(request.body)
        try:
            deviceId = x["device_id"]
            username = x["username"]
            password = x["password"]
        except KeyError:
            return JsonResponse({"Message":"ERROR", "error":-1}, status=403)  
        try:    
            dev = device.objects.get(device_id=deviceId)
        except device.DoesNotExist:
            return JsonResponse({"Message":"ERROR", "error":-3}, status=403)
            
        try:
            owned_by=dev.owner
            return JsonResponse({"Message":"device is active on server"}, status=200)
        except dev.owner == None: #register device 
            try:
                user = u.objects.get(username=username, password=password)
            except u.DoesNotExist:    
                return JsonResponse({"Message":"ERROR", "error":-2}, status=403)
            dev.owner = user
            dev.ip_address = request.META.get('REMOTE_ADDR')
            dev.save()
            return JsonResponse({"Message": "Device has been registered"},status=200)
        


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
def recieve(request):
    if request.method == "GET":
        return JsonResponse({"Message":"POST REQUESTS ONLY"}, status=200)
    if request.method == "POST":
        sender_information = json.loads(request.body)
        dev = device.objects.get(device_id=sender_information["device_id"])
        Username=sender_information["username"]
        Password=sender_information["password"]
        try:
            user = u.objects.get(username=Username)
        except u.DoesNotExist:
            return JsonResponse({"Message":"Error", "error":-2}, status=403)
        if user.password != Password:
            return JsonResponse({"Message":"Error", "error":1}, status=403)    
        if dev.owner.logged_in != True:
            return JsonResponse({"Message":"Error", "error":0}, status=403)    
        variables = device_variables.objects.filter(from_device=dev)
        statuses = device_statuses.objects.filter(for_device=dev)
        current_status = current_device_status.objects.get(for_device=dev)
        #check for new variables
        if sender_information["new_variables"] != None:
            for n in sender_information["new_variables"]:
                var = device_variables(from_device=dev, variable_name=n["name"], value=n["value"], value_type=str(type(n["value"])))
                var.save()
        #check for new statuses
        if sender_information["new_statuses"] != None:
            for x in sender_information["new_statuses"]:
                stat = device_statuses(status_name=x, for_device=dev)
                stat.save()
        #update variable values
        if sender_information["variables_to_update"] != None:
            for y in sender_information["variables_to_update"]:
                vari = device_variables.objects.get(from_device=dev,variable_name=y["name"])
                vari.value = y["value"]
                vari.value_type = str(type(y["value"]))
                vari.save()
        #update current_status
        if sender_information["status"] != None:
            for u in statuses:
                if u.status_name == sender_information["status"]:
                    current_status.current_status = u
                    current_status.save()
                    break
        #transfer new data across other global servers as nessesary
        return "DONE"

#send information out to the cient
def send(request):
    #return "SEND"
    if request.method == "POST":
        return JsonResponse({"Message":"GET REQUESTS ONLY"}, status=200)
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
        dev = device.objects.get()
    #find data
        variables = device_variables.objects.filter(from_device=dev)
        statuses = device_statuses.objects.filter(for_device=dev)
        current_status = current_device_status.objects.get(for_device=dev)
    #send_back
        return JsonResponse({"variables": variables, "current_status":current_status})
