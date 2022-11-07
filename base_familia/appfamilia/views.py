from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from datetime import datetime
from appfamilia.models import *

# Create your views here.
def datos(request):

    respuesta = ""
    for e in Madre.objects.all():
             
        respuesta += f"Nombre: {e.nombre}, Apellido: {e.apellido}, Edad: {e.edad}, Fecha Nac: {e.fecha_nac}"

    respuesta = respuesta.split(",")


    resultado = ""
    for e in Padre.objects.all():
             
        resultado += f"Nombre: {e.nombre}, Apellido: {e.apellido}, Edad: {e.edad}, Fecha Nac: {e.fecha_nac}"

    resultado = resultado.split(",")
 

    llamada = ""
    for e in Hermana.objects.all():
             
        llamada += f"Nombre: {e.nombre}, Apellido: {e.apellido}, Edad: {e.edad}, Fecha Nac: {e.fecha_nac}"

    llamada = llamada.split(",")


    dic = {"madre": respuesta, "padre": resultado, "hermana": llamada}

    plantilla = loader.get_template("plantilla_familia.html")

    documento = plantilla.render(dic)
    
    return HttpResponse(documento)


