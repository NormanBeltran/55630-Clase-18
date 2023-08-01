from django.template import Template, Context, loader
from django.http import HttpResponse
import datetime
from aplicacion.models import *
from random import randint

def bienvenida(request):
    return HttpResponse("Bienvenidos al curso de Django!!")

def bienvenida_html(request):
    hoy = datetime.datetime.now()
    response = f"""
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2>Esta es la comision 55630</h2>
    <h3>Hoy es {hoy} </h3>
    </html>
    """
    return HttpResponse(response)

def saludar(request, nombre):
    response = f"Hola, bienvenido {nombre} al curso de Django!"
    return HttpResponse(response)

def calcular_bruto(request, neto):
    neto = int(neto)
    response = f"<html><h1>El bruto de la factura es {neto*1.21} $</h1></html>"
    return HttpResponse(response)

def saludar2(request, nombre, apellido):
    response = f"Hola, bienvenido {nombre} {apellido} al curso de Django!"
    return HttpResponse(response)

def bienvenida_template(request):
    nombre = "Norman"
    apellido = "Beltran"
    curso = "Python & Django"
    notas = [8,9,5,10,7]

    diccionario = {"nombre": nombre, "apellido": apellido, "curso": curso, "notas": notas}    
    plantilla = loader.get_template('bienvenido.html')    
    
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def clase18(request):
    nombre = "Norman"
    apellido = "Beltran"
    curso = "Python & Django"
    notas = [8,9,5,10,7]

    diccionario = {"nombre": nombre, "apellido": apellido, "curso": curso, "notas": notas}    
    plantilla = loader.get_template('clase18.html')    
    
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def agregar_curso(request):
    nro_comision = randint(1,99999)
    str_nombre = "Python"
    curso = Curso(nombre=str_nombre, comision=nro_comision)
    curso.save()
    documento = f"<html><h1>Se acaba de crear un curso de {str_nombre} para la comision {nro_comision}</h1></html>"
    return HttpResponse(documento)

