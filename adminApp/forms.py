from django.contrib.auth.forms import UserChangeForm, UsernameField
from django import forms
from main.decorators import bootstrap_form
from siteApp.models import Film


@bootstrap_form
class MyUserChangeForm(UserChangeForm):
    # Убираю отображение хэша "пароля"
    password = None

    class Meta(UserChangeForm.Meta):
        fields = ('username', 'first_name', 'last_name')


@bootstrap_form
class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
