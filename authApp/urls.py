from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register/$', register_view, name="auth_register"),
    url(r'^login/$', login_view, name="auth_login"),
    url(r'^logout/$', logout_view, name="auth_logout"),
]
