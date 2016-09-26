#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
]