"""portal_fresia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from portal_fresia.views.contactanos import contactanos
from portal_fresia.views.galeria import galeria
from portal_fresia.views.quienes_somos import quienes_somos
from portal_fresia.views.productos import productos
from portal_fresia.views.mi_cuenta import mi_cuenta
from portal_fresia.views.crear_cuenta import crear_cuenta
from portal_fresia.views.login import login,add_cliente
from portal_fresia.views.region_controller import index_region, add_region
from portal_fresia.views.home import index
from portal_fresia.views.clientes import clientes
from portal_fresia.views.user_controller import user, user_by_id


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index),
    path('api/v1/user', user),
    path('api/v1/user/<int:id>', user_by_id),
    path('', index),
    path('region/', index_region),
    path('add-region', add_region),
    path('crear_cuenta/', crear_cuenta),
    path('add_cliente', add_cliente),
    path('contactanos/', contactanos),
    path('galeria/', galeria),
    path('quienes_somos/', quienes_somos),
    path('productos/', productos),
    path('mi_cuenta/', mi_cuenta),
    path('clientes/',clientes),
    path('login/', login),
    path('accounts/',include('django.contrib.auth.urls')) 
    

]
