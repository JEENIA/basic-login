from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth.views import login

from cuser.forms import AuthenticationForm
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'account/login.html'}),
	url(r'^register/$', views.register, name='register') ,

    
]
