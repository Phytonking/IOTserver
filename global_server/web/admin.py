from django.contrib import admin
from web.models import *
# Register your models here.
admin.site.register(u)
admin.site.register(device)
admin.site.register(device_variables)
admin.site.register(device_statuses)
admin.site.register(current_device_status)