from django.urls import URLPattern, path
from django.urls import re_path as url

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home.html',views.home, name='home'),
    path('analyse.html',views.analyse, name='analyse'),
    ]