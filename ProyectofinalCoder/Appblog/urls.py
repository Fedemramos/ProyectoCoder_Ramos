from django.contrib import admin
from django.urls import path, include

from Appblog.views import mostrar_inicio

urlpatterns = [path("inicio/", mostrar_inicio)]
