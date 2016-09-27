#!python
# log/urls.py
from django.conf.urls import url

from . import views


# We are adding a URL called /home
urlpatterns = [
    url(r'^form/', views.form, name='form'),
    url(r'^result/(\d+)/', views.result, name='result'),
    url(r'^chart/', views.chart, name='chart'),
]
