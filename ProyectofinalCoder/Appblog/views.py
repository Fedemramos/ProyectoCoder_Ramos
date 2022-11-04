from django.http import HttpResponse
from django.shortcuts import render

from Appblog.models import Curso, Autor, Avatar
from Appblog.form import form_formulario, UserEditionForm, AvatarForm

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request, "Appblog/inicio.html", contexto)


def inicio_seccion(request):
    return render(request, "Appblog/iniciar_seccion.html")


def subscripcion(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "Appblog/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "Appblog/subscripcion.html", {"form": form})


@login_required
def articulos(request):
    return render(request, "Appblog/articulos.html")


def autores(request):
    return render(request, "Appblog/autores.html")


def sobre_mi(request):
    return render(request, "Appblog/sobre_mi.html")


@login_required
def cursos(request):
    return render(request, "Appblog/cursos.html")


def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "Appblog/formulario.html")

    curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
    curso.save()
    return render(request, "Appblog/inicio.html")


@login_required
def formulario_form(request):
    if request.method != "POST":
        mi_formulario = form_formulario()
    else:
        mi_formulario = form_formulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["comision"])
            curso.save()
            return render(request, "Appblog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "Appblog/formulario2.html", contexto)


@login_required
def busqueda_2(request):
    return render(request, "Appblog/buscar_comision.html")


@login_required
def buscar_2(request):

    if not request.GET["camada"]:
        return HttpResponse("No se encontro comision")
    else:
        camada_a_buscar = request.GET["camada"]  # camada=comision
        cursos = Curso.objects.filter(camada=camada_a_buscar)

        contexto = {"camada": camada_a_buscar, "cursos_encontrados": cursos}

        return render(request, "Appblog/resultado_de_busqueda.html", contexto)


@login_required
def busqueda_autor(request):
    return render(request, "Appblog/buscar_autor.html")


@login_required
def buscar_autor(request):
    if not request.GET["autor"]:
        return HttpResponse("No se encontro el autor")
    else:
        apellido_a_buscar = request.GET["autor"]
        autor = Autor.objects.filter(apellido=apellido_a_buscar)

        contexto = {"nombre": apellido_a_buscar, "autor_encontrados": autor}

        return render(request, "Appblog/resultado_de_autores.html", contexto)


@login_required
def listas_cursos(request):
    todos_los_cursos = Curso.objects.all()
    contexto = {"cursos_encontrados": todos_los_cursos}
    return render(request, "Appblog/listas_de_cursos.html", contexto)


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "Appblog/cursos_list.html"


class CursoDetalle(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "Appblog/curso_detalle.html"


from django.urls import reverse


class CursoCreacion(LoginRequiredMixin, CreateView):
    model = Curso
    fields = ["nombre", "camada"]

    def get_success_url(self):
        return reverse("CursoList")


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    success_url = "/Appblog/curso/list"
    fields = ["nombre", "camada"]


class CursoDelete(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = "/Appblog/curso/list"


class MyLogin(LoginView):
    template_name = "Appblog/login.html"


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "Appblog/logout.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "Appblog/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "Appblog/registro.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "Appblog/inicio.html", {"avatar": avatar.imagen.url})

    contexto = {"user": user, "form": form, "avatar": avatar.imagen.url}
    return render(request, "Appblog/editarPerfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "Appblog/inicio.html")

    contexto = {"form": form}
    return render(request, "Appblog/avatar.html", contexto)
