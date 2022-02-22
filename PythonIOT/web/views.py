import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.http import request, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
import web.tools as tools
from django.urls import reverse
from web.models import *
from web.tools import password_hash

def index(request):
    return render(request, 'web/index.html')


