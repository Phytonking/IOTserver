from django.urls import path, include
from web.views import *
app_name="web"
urlpatterns = [
    path('', index, name="index"),
    path("about", about_page, name="about"),
    path('<uuid:sess>/about',about_page_logged, name="about_logged"),
    path('<uuid:sess>/index', logged_in_index, name="logged_index"),
    path('<uuid:sess>/devices', device_view, name="device"),
    path('login',login_view,name="login"),
    path('register',register_view,name="register"),
    path('<str:session>/logout', logout_view, name="logout"),
    path('<uuid:sess>/device_view/<str:deviceId>', specific_device_view, name="one_device"),
    # API
    path("syncup", sync, name="syncup")
]