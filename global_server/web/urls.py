from django.urls import path, include
from web.views import *

app_name='web'
urlpatterns = [
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path("check_registration", check_registration, name="check_reg"),
    path("recieve", recieve, name="recieve"),
    path("send", send, name="send")
]
