from django.urls import path
from web.views import *
app_name = "pythoniot"
urlpatterns = [
    path('',index,name="index"),
    path('add',add_device_view, name="add")
]