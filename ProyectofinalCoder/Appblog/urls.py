from django.urls import path

from Appblog.views import (
    inicio,
    cursos,
    articulos,
    asignatura,
    subscripcion,
    procesar_formulario,
    formulario_form,
)


urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("curso/", cursos, name="cursos"),
    path("subscripcion/", subscripcion, name="subscripcion"),
    path("articulos/", articulos, name="articulos"),
    path("asignaturas/", asignatura, name="asignaturas"),
    path("formulario/", procesar_formulario, name="formulario"),
    path("formulario-2/", formulario_form, name="formulario-2"),
]
