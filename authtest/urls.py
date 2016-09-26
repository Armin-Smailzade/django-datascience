#!python
# authtest/urls.py
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as authView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from log.forms import LoginForm
from log import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', authView.login, {'template_name': 'log/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', authView.logout, {'next_page': '/login'}), 

    url(r'', include('log.urls')),
    
    
    

]
