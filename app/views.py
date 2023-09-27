from django.shortcuts import render
from django.http import HttpResponse
import datetime
import os

def home(request):
        return HttpResponse("Домашняя страница")

def current_time(request):
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {formatted_time}")

def workdir(request):
    current_directory = os.getcwd()
    return HttpResponse(f"Содержимое рабочей директории: {current_directory}")
