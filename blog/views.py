from django.shortcuts import render
from django.http import HttpResponse

def ola(request):
    return HttpResponse("Primeira View em Django.")
