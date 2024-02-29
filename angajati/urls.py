"""
URL configuration for second_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home, angajati_view, angajati_total_count
from angajati.views import AngajatiCreateView, CreateAngajat, AngajatDetailView, AngajatUpdateView, AngajatDeleteView

urlpatterns = [

    path('', angajati_view, name="angajati"),
    path('nr_angajati/', angajati_total_count, name="angajati_total_count"),
    path('add/', AngajatiCreateView.as_view(), name='angajati-add'),
    path('create/', CreateAngajat.as_view(), name='angajati-create'),
    path('detail/<pk>', AngajatDetailView.as_view(), name='angajati-details'),
    path('update/<pk>', AngajatUpdateView.as_view(), name='angajati-update'),
    path('delete/<pk>', AngajatDeleteView.as_view(), name='angajati-delete'),
]
