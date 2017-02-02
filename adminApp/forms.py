from django.contrib.auth.forms import UserChangeForm, UsernameField
from main.decorators import bootstrap_form


@bootstrap_form
class MyUserChangeForm(UserChangeForm):
    # Убираю отображение хэша "пароля"
    password = None

    class Meta(UserChangeForm.Meta):
        fields = ('username', 'first_name', 'last_name')
