"""option_pricing2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from option_pricing2 import views

urlpatterns=[
    path("",views.index,name="myapp"),
    path("services",views.services,name="services"),
    path("two_step",views.two_step,name="two_step"),
    path("n_step",views.n_step,name="n_step"),
    path("black_scholes",views.black_scholes,name="black_scholes"),
]
