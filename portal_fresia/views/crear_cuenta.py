from django.shortcuts import render
from portal_fresia.models import Cliente
def crear_cuenta(request):
    return render(request, 'crear_cuenta.html')

def add_cliente(request):
    print('add_cliente INIT')
    if request.method == 'POST':
        email = request.POST.get('email')
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        fecha_de_nac = request.POST.get('fecha_de_nac')
        genero_id_genero = request.POST.get('genero_id_genero')
        estado_civil_id_estadocivil = request.POST.get('estado_civil_id_estadocivil')
        id_cliente = request.POST.get('id_cliente')
        wallet_cliente_numero_tarjeta = request.POST.get('wallet_cliente_numero_tarjeta')
        contrasena = request.POST.get('contrasena')
        print('email: ', email)
        print('rut: ', rut)
        print('nombre: ', nombre)
        print('fecha_de_nac: ', fecha_de_nac)
        print('genero_id_genero: ', genero_id_genero)
        print('estado_civil_id_estadocivil: ', estado_civil_id_estadocivil)
        print('id_cliente: ', id_cliente)
        print('wallet_cliente_numero_tarjeta: ', wallet_cliente_numero_tarjeta)
        print('contrasena: ', contrasena)
        crear_cuenta = Cliente()
        crear_cuenta.email = email
        crear_cuenta.rut = rut
        crear_cuenta.nombre = nombre
        crear_cuenta.fecha_de_nac = fecha_de_nac
        crear_cuenta.genero_id_genero = genero_id_genero
        crear_cuenta.estado_civil_id_estadocivil = estado_civil_id_estadocivil
        crear_cuenta.id_cliente = id_cliente
        crear_cuenta.wallet_cliente_numero_tarjeta = wallet_cliente_numero_tarjeta
        crear_cuenta.contrasena = contrasena
        crear_cuenta.save()
    return render(request, 'index.html')
