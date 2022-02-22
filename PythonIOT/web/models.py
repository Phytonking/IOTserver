from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IPAddressField, UUIDField
# Create your models here.

LIGHT = "LIS"
device_types = [(LIGHT,"light")]


class device(models.Model):
    device_id = models.UUIDField(null=True)
    device_name = models.TextField(null=True)
    device_type = models.CharField(max_length=5,choices=device_types,null=True)
    IP_address = models.GenericIPAddressField(null=True)


class action(models.Model):
    time = models.DateTimeField(auto_now=True)
    device_used = models.ForeignKey(device, on_delete=models.CASCADE, related_name='signal_reciver')
    prev_device_status = models.TextField()
    now_device_status = models.TextField()
    client_ip_address = models.GenericIPAddressField()