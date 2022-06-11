from django.shortcuts import render
from portal_fresia.models import Genero, Region
from portal_fresia.models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

def login(request):
    if request.method=='POST':

        user =request.POST.get('nombre')
        pas =request.POST.get('contrasena')

        user = User.objects.get(username=user)
        if check_password(pas,user.password):
            print('login valido')

        else:
            print('login invalido')

    return render(request, 'login.html')


