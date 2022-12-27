from django.shortcuts import render
from django.http import HttpResponse
from familia.models import Familia
# Create your views here.

def agregar_familiares(request):
    Familia.objects.create(nombre = 'Mauricio', edad = 57, mayor_de_edad = True, parentesco = 'Papá')
    Familia.objects.create(nombre = 'Laura', edad = 51, mayor_de_edad = True, parentesco = 'Mamá')
    Familia.objects.create(nombre = 'Julian', edad = 28, mayor_de_edad = True, parentesco = 'Hermano')
    Familia.objects.create(nombre = 'Agustina', edad = 20, mayor_de_edad = True, parentesco = 'Hermana más grande')
    Familia.objects.create(nombre = 'Sofia', edad = 15, mayor_de_edad = False , parentesco = 'Hermana más chica')

    return HttpResponse('Se agregó la familia a la base de datos')


def lista_familiares (request):
    familiares = Familia.objects.all()
    context = {
        'familiares' : familiares
    }
    return render (request, 'familia.html', context=context)