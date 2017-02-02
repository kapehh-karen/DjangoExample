from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.decorators import bootstrap_form


@bootstrap_form
class UserLoginForm(forms.Form):
    username = forms.CharField(label="Имя")
    password = forms.CharField(label="Пароль")


@bootstrap_form
class MyUserCreationForm(UserCreationForm):
    pass
