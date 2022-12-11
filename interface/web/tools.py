from django.db import IntegrityError
from web.models import *
from uuid import uuid4
import requests
import json
def create_session(use):
    try:
        ses = session.objects.create(session_id = uuid4(), user = u.objects.get(username=use), logged_out=False)
        ses.save()
    except IntegrityError:
        return False
    return ses.session_id

def logout_session(sess):
    try:
        k = session.objects.get(session_id=sess)
        try:
            us = k.user
            us.logged_in = False
            us.save()
            return True
        except u.DoesNotExist:
            return False
    except session.DoesNotExist:
        return False

global_server="0.0.0.0"
def send_user_to_global(user):
    server = f"http://{global_server}/send"
    l = requests.post(server,json={"action":"new_user","first_name":user.first_name,"last_name":user.last_name, "email":user.email, "username":user.username, "password":user.password, "serial":user.account_user_serial_key, "origin":user.account_server_origin, "logged_in":False})
    return l.json()

def send_device_to_global(device):
    server = f"http://{global_server}/send"
    l = requests.post(server,json={"action":"new_device","device_id":device.device_id, "device_name":device.device_name, "owner": device.owner.username, "ip":device.ip_address})
    return l.json()

def pull_from_global(User, device):
    server = f"http://{global_server}/send"
    l = requests.get(server, json={"username": User.username, "password":User.password, "device_id": device})
    return l.json()