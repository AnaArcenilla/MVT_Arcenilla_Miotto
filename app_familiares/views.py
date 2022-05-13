from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from app_familiares.models import Familiar

def mostrar_familiares(self):

    familiar1=Familiar(nombre="Pepe",apellido="Lopez",fecha_nacimiento="1999-07-10")
    familiar1.save()
    familiar2=Familiar(nombre="Juan",apellido="Perez",fecha_nacimiento="2021-02-22")
    familiar2.save()
    familiares=list()
    familiares=[familiar1,familiar2]
    diccionario={"hoy":datetime.now(),"familiares":familiares}
    
    plantilla=loader.get_template('template.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)