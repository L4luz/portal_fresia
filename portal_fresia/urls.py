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
from re import I
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from django.conf.urls.static import static
from django.conf import settings
from portal_fresia.views.errorpage import error_401_page,error_403_page,error_404_page
from portal_fresia.views.contactanos import contactanos
from portal_fresia.views.galeria import galeria
from portal_fresia.views.quienes_somos import quienes_somos
from portal_fresia.views.productos import productos
from portal_fresia.views.login import authentication
from portal_fresia.views.region_controller import index_region, add_region
from portal_fresia.views.home import index
from portal_fresia.views.pago import pago
from portal_fresia.views import user
from portal_fresia.views.cart import cart
from portal_fresia.views import  model_register
from portal_fresia.views import verification_recovery
from portal_fresia.views import recovery
from portal_fresia.views.carrito_compra import carrito_compra
from portal_fresia.views.logout import logout_user
from portal_fresia.views.crear_cuenta import crear_cuenta
from portal_fresia.views.productos import crear_productos,add_producto
from portal_fresia.views.crear_cuenta import add_contact
from portal_fresia.views.clientes import clientes
from portal_fresia.views.transbankpay import commitpay,webpay_plus_create
from portal_fresia.views import user_controller 
from portal_fresia.ws.cliens_ws import find_client_all,add_client
from portal_fresia.views.transbankpay import webpay_plus_create



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index),
    path('api/v1/clients', find_client_all),
     path('api/v1/add-clients', add_client),
    path('api/v1/user/<int:id>', user_controller.user_by_id),
    path('', index),
    path('region/', index_region),
    path('add-region', add_region),
    path('contactanos/', contactanos),
    path('galeria/', galeria),
    path('quienes_somos/', quienes_somos),
    path('productos/', crear_productos),
    path('productos/', add_producto),
    path('cart/', carrito_compra),
    path('crear_cuenta/', crear_cuenta),
    path('add_contact/', add_contact),
    path('clientes/',clientes),
    path('login', authentication),
    path('pago/', pago),
    path('cart/', cart),
    path('verification-recovery/', verification_recovery.load),
    path('recovery/', recovery.load),
    path('edit-user/', user.load),
    path('logout', logout_user),
    path('commit-pay/', commitpay),
    path('webpay-plus-create', webpay_plus_create),  
    path('accounts/',include('django.contrib.auth.urls')) ,
    path('error-401/',error_401_page),
    path('error-403/',error_403_page),
    path('error-404/',error_404_page),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "portal_fresia.views.errorpage.error_404"
