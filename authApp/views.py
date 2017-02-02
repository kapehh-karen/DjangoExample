from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, MyUserCreationForm


# Create your views here.

def register_view(request):
    errors = None

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: Не нашел более простого способа для того чтобы
            #       передать параметры через GET запрос
            return redirect("%s?registered=1" % reverse("auth_login"))
        else:
            errors = "Имеются ошибки в заполнении формы"
    else:
        form = MyUserCreationForm()

    return render(request, "auth/register.html", {"form": form, "errors": errors})


def login_view(request, next=None):
    errors = None

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect(next) if next else redirect("site_index")
            else:
                errors = "Введены некорректные имя пользователя или пароль. " \
                         "Либо такого пользователя не существует."
        else:
            errors = "Форма не прошла валидацию"
    else:
        form = UserLoginForm()

    return render(request, "auth/login.html", {
        "form": form,
        "next": next,
        "errors": errors,
        "registered": request.GET.get("registered")
    })


def logout_view(request):
    logout(request)
    return redirect("site_index")
