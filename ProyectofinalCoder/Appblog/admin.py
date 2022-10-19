from django.contrib import admin

from Appblog.models import Articulo, Subcriptores, Curso, Autor

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Subcriptores)
admin.site.register(Curso)
admin.site.register(Autor)
