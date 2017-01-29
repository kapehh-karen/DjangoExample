from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from functools import wraps


# Create your views here.

# Декоратор для проверки прав пользователя
def user_is_admin(method):
    @wraps(method)
    def inner(request, *args, **kwargs):
        if request.user.is_superuser:
            return method(request, *args, **kwargs)

        return render(request, "admin/forbidden.html")

    return inner


@user_is_admin
def index_view(request):
    return render(request, "admin/index.html", {
        "data": {
            "Пользователи": User.objects.all()
        }
    })


@user_is_admin
def edit_view(request, user_id):
    print(user_id)
    return redirect("/")


@user_is_admin
def remove_view(request, user_id):
    print(user_id)
    return redirect("/")
