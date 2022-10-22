from django.http import JsonResponse
from django.shortcuts import render
from file_storage.models import *
from web.models import *
from file_storage.tools import *
import json
# Create your views here.

def list_files(request):
    if request.method == "GET":
        file_obj = files.objects.all()
        if file_obj.count == 0:
            return "No files found"
        else:
            return file_obj

def add_files(request):
    if request.method == "POST":
        file_info = json.loads(request.body)
        auth = authenticate(file_info["user"], file_info["serial_key"])
        if auth == True:
            generate_file()
            new_file = files(file_name=file_info["file_name"], file_owner=u.objects.get("username"), file_size_bytes="", in_folder=None, in_parent_folder=None)
            return True
        elif auth == None:
            return JsonResponse({"message":"Error","error":-3}, status=404)
        elif auth == False:
            return JsonResponse({"message":"Error","error":-3}, status=400)        
        #Note: generate search system to find the folders and parent folders to identify them. 