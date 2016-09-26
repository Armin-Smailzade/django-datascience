#!python
# authtest/urls.py
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as authView

from log.forms import LoginForm
from log import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'', include('log.urls')),
    
    # url(r'^calculator/$', include('calculator.urls')),
]
