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
    def __str__(self):
        return self.device_id

class session(models.Model):
    session_id = models.TextField()
    user = models.ForeignKey(u, on_delete=models.DO_NOTHING, related_name="logged")
    logged_out = models.BooleanField(null=True)