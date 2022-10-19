from django.http import HttpResponse
from django.shortcuts import render

from Appblog.models import Subcriptores, Curso
from Appblog.form import form_formulario

# Create your views here.


def inicio(request):
    subcriptor = Subcriptores(
        nombre="Rodrigo", apellido="Pacheco", email="eze@hotmail.com"
    )
    subcriptor.save()
    contexto = {"subcriptor_1": subcriptor}
    return render(request, "Appblog/inicio.html", contexto)


def subscripcion(request):
    return render(request, "Appblog/subscripcion.html")


def articulos(request):
    return render(request, "Appblog/articulos.html")


def autores(request):
    return render(request, "Appblog/autores.html")


def cursos(request):
    return render(request, "Appblog/cursos.html")


def asignatura(request):
    return render(request, "Appblog/asignatura.html")


def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "Appblog/formulario.html")

    curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
    curso.save()
    return render(request, "Appblog/inicio.html")


def formulario_form(request):
    if request.method != "POST":
        mi_formulario = form_formulario()
    else:
        mi_formulario = form_formulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return render(request, "Appblog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "Appblog/formulario2.html", contexto)
