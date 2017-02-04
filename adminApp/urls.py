from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_view, name="admin_index"),
    url(r'^user/(\d+)/edit/$', edit_view, name="admin_user_edit"),
    url(r'^user/(\d+)/remove/$', remove_view, name="admin_user_remove"),
    url(r'^film/add/$', film_add, name="admin_film_add"),
    url(r'^film/(\d+)/edit/$', film_edit, name="admin_film_edit"),
    url(r'^film/(\d+)/remove/$', film_delete, name="admin_film_delete")
]
