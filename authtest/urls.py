#!python
# authtest/urls.py
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'', include('log.urls')),
    url(r'^calculator/', include('calculator.urls')),
    url(r'^map/', include('map.urls')),
]
