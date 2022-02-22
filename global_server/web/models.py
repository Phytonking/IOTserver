from ipaddress import ip_address
from pyexpat import model
from django.db import models

# Create your models here.
class u(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    username = models.TextField(null=True)
    password = models.TextField(null=True)
    account_user_serial_key = models.TextField(null=True)
    account_server_origin = models.TextField()
    logged_in = models.BooleanField(null=True)
    

class device(models.Model):
    device_id = models.TextField()
    device_name = models.TextField()
    owner = models.ForeignKey(u, on_delete=models.CASCADE, related_name='linked_account')
    ip_address = models.GenericIPAddressField(null=True)
    #current_device_status = models.ForeignKey(device_statuses, on_delete=models.CASCADE, related_name='stat', null=True)

class device_statuses(models.Model):
    status_name = models.TextField()
    for_device = models.ForeignKey(device, on_delete=models.CASCADE, related_name='dev')

class device_variables(models.Model):
    from_device = models.ForeignKey(device, on_delete=models.CASCADE, related_name='data')
    variable_name = models.TextField()
    value = models.TextField(null=True)
    value_type = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now=True)

class current_device_status(models.Model):
    for_device = models.ForeignKey(device, on_delete=models.CASCADE, related_name="device")
    current_status = models.ForeignKey(device_statuses, on_delete=models.CASCADE, related_name='stat', null=True)