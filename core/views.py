from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from .models import Staff
from django.shortcuts import redirect #Login
from django.conf import settings #Login
from django.contrib.auth.models import User #Registro Usuarios
from django.contrib.auth.hashers import make_password #Registro Usuarios
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#Vistas del Login
def login(request):
    return render(request, 'login.html')
@login_required
def home(request):
    return render(request, 'home.html')


@csrf_exempt
def contactAjaxResponse(request):
    id = int("0" + request.POST["txtId"])
    try:
        item = Staff.objects.get(pk = id)
        item = model_to_dict(item)
        return JsonResponse(item)
    except:
        return JsonResponse({})


@csrf_exempt
def contactAjax(request):
    return render(request, 'core/contactAjax.html', {} )


def ajaxTestResponse(request):
    contexto = {'mensaje' : 'hola mundo Con ajax'}
    return JsonResponse(contexto)

def ajaxTest(request):
    return render(request, "core/ajaxTest.html", {})


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
    if not request.user.is_authenticated:
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    mensaje = ""
    lista   = {}
    item    = {}
    #Detecta si hay una solicitud
    if request.method == "POST":
        #CAPTURA LOS VALORES ENTREGADOS
        id              = int("0" + request.POST["txtId"])
        rut             = int("0" + request.POST["txtRut"])
        nombre          = request.POST["txtNombre"]
        apellido        = request.POST["txtApellido"]
        corre           = request.POST["txtCorre"]

        #detecta que boton presiono el usuario
        if 'btnGrabar' in request.POST:

            if id < 1: #nuevo registro
                Staff.objects.create(rut = rut, nombre=nombre, apellido=apellido, corre=corre)

            else:
                item = Staff.objects.get(pk = id)
                item.rut        = rut
                item.nombre     = nombre
                item.apellido   = apellido
                item.corre      = corre
                item.save()
                item = {}
            mensaje = "Datos Guardados"
        elif 'btnBuscar' in request.POST:
            try:
                item = Staff.objects.get(pk = id)
            except:
                mensaje = "Staff no encontrado"
                item = {}

        elif 'btnListar' in request.POST:
            lista = Staff.objects.all()

        elif 'btnEliminar' in request.POST:
            item = Staff.objects.get(pk = id)

            if isinstance (item, Staff):
                item.delete()
                mensaje = "Registro Eliminado"
                item    = {}
    #Contexto es la informacion que se envia a la plantilla para procesar
    contexto = {'mensaje' : mensaje, 'lista':lista, 'item':item}


    return render(request, "core/contact.html", contexto)

