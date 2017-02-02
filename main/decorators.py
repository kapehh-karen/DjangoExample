from django.shortcuts import render
from functools import wraps


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


def bootstrap_form(cls):
    """
    Меняет стили у формы
    """

    old_init = cls.__init__

    def new_init(self, *args, **kwargs):

        # Сначала вызываем дефолтный инициализатор
        # чтобы он создал нам свойство fields
        old_init(self, *args, **kwargs)

        # А теперь выставляем им классы
        for title, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    cls.__init__ = new_init
    return cls
