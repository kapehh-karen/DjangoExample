from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def index_view(request):
    return render(request, "admin/index.html", {
        "data": {
            "Пользователи": User.objects.all(),
            "Пользователи2": User.objects.all()
        }
    })
