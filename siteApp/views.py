from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Film


# Create your views here.

def index(request):
    films = Film.objects.all()
    paginator = Paginator(films, 2)

    page = request.GET.get('page')
    try:
        film_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        film_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        film_list = paginator.page(paginator.num_pages)

    return render(request, 'site/index.html', {'film_list': film_list})
