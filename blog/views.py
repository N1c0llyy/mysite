from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá! Minha primeira View em Django.")