from django.contrib import admin
from django.urls import path, include
from learn import views

urlpatterns = [
    path('python/', views.python, name='python'),
    path('tpmpython1_print', views.python1_print, name='python1_print'),
]