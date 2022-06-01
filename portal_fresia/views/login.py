from django.shortcuts import render
from portal_fresia.models import Region
from portal_fresia.models import Cliente

def login(request):
    return render(request, 'login.html')

def add_cliente(request):
    print('add_cliente INIT')
    if request.method == 'POST':
        email = request.POST.get('email')
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        fecha_de_nac = request.POST.get('fecha_de_nac')
        genero_id_genero = request.POST.get('genero_id_genero')
        estado_civil_id_estadocivil = request.POST.get('estado_civil_id_estadocivil')
        wallet_cliente_numero_tarjeta = request.POST.get('wallet_cliente_numero_tarjeta')
        print('email: ', email)
        print('rut: ', rut)
        print('nombre: ', nombre)
        print('fecha_de_nac: ', fecha_de_nac)
        print('genero_id_genero: ', genero_id_genero)
        print('estado_civil_id_estadocivil: ', estado_civil_id_estadocivil)
        print('wallet_cliente_numero_tarjeta: ', wallet_cliente_numero_tarjeta)
        login = Cliente()
        login.email = email
        login.rut = rut
        login.nombre = nombre
        login.fecha_de_nac = fecha_de_nac
        login.genero_id_genero = genero_id_genero
        login.estado_civil_id_estadocivil = estado_civil_id_estadocivil
        login.wallet_cliente_numero_tarjeta = wallet_cliente_numero_tarjeta
        login.save()
    return render(request, 'login.html')