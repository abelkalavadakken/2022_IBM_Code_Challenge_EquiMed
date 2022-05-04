from django.urls import URLPattern, path
from django.urls import re_path as url

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('file.html',views.file, name='file'),
    path('analyse.html',views.analyse, name='analyse'),
    path('result.html',views.result, name='result'),
    path('noresult.html',views.noresult, name='noresult')
    ]