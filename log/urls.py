#!python
# log/urls.py
from django.conf.urls import url
from django.contrib.auth import views as authView

from log.forms import LoginForm
from log import views
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^log/index/$', views.index, name='index'),
    
    url(r'^log/register/$', views.register, name='register'),

    url(r'^log/login/$', authView.login, {'template_name': 'log/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^log/logout/$', authView.logout, {'next_page': '/log/login'}), 
]
