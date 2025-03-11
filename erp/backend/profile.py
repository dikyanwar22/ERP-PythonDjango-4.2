from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.db import connection
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


# halaman profile
def profile(request):
    return render(request, 'modules/profile/index.html')

