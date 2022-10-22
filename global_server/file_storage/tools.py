import hashlib
from web.models import *
def generate_file(user, information, file_name):
    user_folder = hashlib.ssh256(bytes(user)).hexdigest()
    hashedfile = hashlib.ssh256(bytes(file_name)).hexdigest()
    info = information
    for x in range(0,64):
        hashedinfo = hashlib.ssh512(bytes(info)).hexdigest()
    f = open(f"files/{user_folder}/{hashedfile}", "x")
    f.write(hashedinfo)
    f.save()



def authenticate(username, serial_key):
    try:
        user = u.objects.get(username=username)
    except u.DoesNotExist:
        return None
    if user.logged_in and serial_key == user.account_user_serial_key:
        return True
    else:
        return False    