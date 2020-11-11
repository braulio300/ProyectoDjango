from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect #Login
from django.conf import settings #Login
from django.contrib.auth.models import User #Registro Usuarios
from django.contrib.auth.hashers import make_password #Registro Usuarios
# Create your views here.

def registro(request):
    if request.method == "POST":
        nombre = request.POST["txtNombre"]
        correo = request.POST["txtCorreo"]
        clave = request.POST["txtClave"]
        #if nombre == '' or correo == '' or clave == '':
            #return redirect(request, '/core/registro.html')     Cuando no escriben nada, despues de la alerta se cae y si le pongo
        #else:                                                   esto, me tira otro error 'NoReverseMatch at /registro'
        User.objects.create(username=nombre, email=correo, password=make_password(clave))

        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "core/registro.html")

def home(request):

    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def event(request):
    if not request.user.is_authenticated:
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "core/event.html")

def contact(request):
    return render(request, "core/contact.html")
