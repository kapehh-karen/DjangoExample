from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_view, name="admin_index"),
    url(r'^user/(\d+)/edit/$', edit_view, name="admin_edit"),
    url(r'^user/(\d+)/remove/$', remove_view, name="admin_remove")
]
