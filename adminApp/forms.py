from django.contrib.auth.forms import UserChangeForm, UsernameField
from django import forms


class MyUserChangeForm(UserChangeForm):
    # Убираю отображение хэша "пароля"
    password = None

    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'

    class Meta(UserChangeForm.Meta):
        fields = ('username', 'first_name', 'last_name')
