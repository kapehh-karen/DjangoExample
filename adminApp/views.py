from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from main.decorators import user_is_admin
from siteApp.models import Film
from .forms import MyUserChangeForm, FilmForm


# Create your views here.

@user_is_admin
def index_view(request):
    class ListContainer:
        def __init__(self, **kwargs):
            self.fields = kwargs

    return render(request, "admin/index.html", {
        "data": [
            ListContainer(
                title="Пользователи",
                list=User.objects.all(),
                support_add=False,
                url_edit="admin_user_edit",
                url_delete="admin_user_remove"
            ),
            ListContainer(
                title="Фильмы",
                list=Film.objects.all(),
                support_add=True,
                url_add="admin_film_add",
                url_edit="admin_film_edit",
                url_delete="admin_film_delete"
            )
        ]
    })


@user_is_admin
def edit_view(request, user_id):
    errors = None
    user = get_object_or_404(User, pk=user_id)

    if request.method == "POST":
        form = MyUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("admin_index")
        else:
            errors = "Форма заполнена некорректно"
    else:
        form = MyUserChangeForm(instance=user)

    return render(request, "admin/user/user_edit.html", {
        "form": form,
        "selected_user": user,
        "errors": errors
    })


@user_is_admin
def remove_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect("admin_index")


@user_is_admin
def film_add(request):
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("admin_index")
    else:
        form = FilmForm()
    return render(request, "admin/film/film_add.html", {"form": form})


@user_is_admin
def film_edit(request, film_id):
    errors = None
    film = get_object_or_404(Film, pk=film_id)

    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect("admin_index")
        else:
            errors = "Форма заполнена некорректно"
    else:
        form = FilmForm(instance=film)

    return render(request, "admin/film/film_edit.html", {"errors": errors, "film": film, "form": form})


@user_is_admin
def film_delete(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    film.delete()
    return redirect("admin_index")
