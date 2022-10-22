from web.tools import *
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from web.models import *
import hashlib
import json
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, "web/index.html", {"User":None})
    
def logged_in_index(request, sess):
    return render(request, "web/index.html", {"User":session.objects.get(session_id=sess).user, "in_session":True, "session_id":sess})

#def logged_index(request, serial_key)
def login_view(request):
    if request.method == "GET":
        return render(request, "web/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = u.objects.get(username=username)
            if password == user.password:
                user.logged_in = True
                user.save()
                session_id = create_session(user.username)
                if session_id == False:
                    return render(request, "web/login.html",{"error": "session error"})
                else:
                    return HttpResponseRedirect(reverse("web:logged_index", kwargs={"sess": session_id}))
            else:
                return render(request, "web/login.html",{"error": "password is incorrect"})
        except u.DoesNotExist:
            return render(request, "web/login.html",{"error": "user does not exist"})

def register_view(request):
    if request.method == "GET":
        return render(request, "web/register.html")
    else:
        fName = request.POST["firstName"]
        lName = request.POST["lastName"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        cPassword = request.POST["cPassword"]
        try:
            user = u(first_name = fName, last_name = lName, email = email, username=username, password = password, account_user_serial_key = None)
            if password == cPassword:
                user.logged_in = True
                user.save()
                return HttpResponseRedirect(reverse("web:index"))
            else:
                return render(request, "web/register.html",{"error": "passwords dont match"})
        except u.DoesNotExist:
            return render(request, "web/register.html",{"error": "user does not exist"})

def logout_view(request, session):
    l = logout_session(session)
    if l:
        return HttpResponseRedirect(reverse("index"))
    else:
        return "Failed to logout"

def device_view(request, sess):
    User = session.objects.get(session_id=sess).user
    if request.method == "GET":
        return render(request, "web/device.html", {"User":User, "devices": device.objects.filter(owner=User), "session_id":sess, "deviceCount":device.objects.filter(owner=User).count()})
    if request.method == "POST":
        iden = request.POST["device_id"]
        name = request.POST["name"]
        ip_address = request.POST["IP_address"]
        dev = device(device_id = iden, device_name=name, owner=User, ip_address=ip_address)
        dev.save()
        return render(request, "web/device.html", {"User":User, "devices": device.objects.filter(owner=User), "session_id":sess, "deviceCount":device.objects.filter(owner=User).count()})
@csrf_exempt
def sync(request):
    if request.method == "GET":
        return JsonResponse({"Message":"POST REQUESTS ONLY"}, status=200)
    else:
        # add security key checker
        data = json.loads(request.json)
        user = u.objects.get(username=data["username"], password=data["password"])
        if data["information_type"] == 0: #info type 0 indicates a new device being registered into the system
            j = data["data"]
            d = device(device_id = j["device_id"], device_name=j["device_name"], owner=user, ip_address=j["ip_address"])
            d.save()
            return JsonResponse({"Message":"Sync Successful"}, status=200)
        
        



    