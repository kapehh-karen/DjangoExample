from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from functools import wraps
from .forms import MyUserChangeForm


# Create your views here.

# Декоратор для проверки прав пользователя
def user_is_admin(method):
    # wraps юзаю для того, чтобы при ошибках в методе 'method'
    # у меня в логах было имя функции view, а не "inner"
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
