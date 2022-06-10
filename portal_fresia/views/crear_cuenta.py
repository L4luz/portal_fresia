


from django import apps
from django.shortcuts import render
from flask import appcontext_popped, render_template, request
from portal_fresia.models import Cliente, Genero, EstadoCivil, TarjetaCliente
from portal_fresia.ws.cliens_ws import find_all

def crear_cuenta(request):
    estado = False
    mensaje = None
    if request.method == 'POST':
        estado, mensaje = add_contact(request)
    generos = Genero.objects.all()
    estados_civiles = EstadoCivil.objects.all()
    tarjetas_clientes = TarjetaCliente.objects.all()

    return render(request, 'crear_cuenta.html',  {'generos': generos,'estados_civiles': estados_civiles,'tarjetas_clientes': tarjetas_clientes, 'estado': estado, 'mensaje' : mensaje})

#@appcontext_popped.route('/add_contact',methods=['POST'])
def add_contact(request):
    email=request.POST.get('email')
    rut=request.POST.get('rut')
    contrasena=request.POST.get('contrasena')
    nombre=request.POST.get('nombre')
    fecha_de_nac=request.POST.get('fecha-de-nac')
    id_genero=request.POST.get('id_genero')
    id_estado_civil=request.POST.get('id_estado_civil')
    id_tarjeta_cliente=request.POST.get('id_tarjeta_cliente')

    print('email', email)
    print('rut', rut)
    print('contrasena', contrasena)
    print('nombre', nombre)
    print('fecha_de_nac', fecha_de_nac)
    print('id_genero', id_genero)
    print('id_estado_civil', id_estado_civil)
    print('id_tarjeta_cliente', id_tarjeta_cliente)
    cliente = Cliente()
    cliente.email = email
    cliente.rut = rut
    cliente.contrasena = contrasena
    cliente.nombre = nombre
    cliente.fecha_de_nac = fecha_de_nac
    cliente.id_genero = Genero.objects.get(pk=id_genero)
    cliente.id_estado_civil = EstadoCivil.objects.get(pk=id_estado_civil)
    cliente.id_tarjeta_cliente = TarjetaCliente.objects.get(pk=id_estado_civil)

    try:
        cliente.save()
        return True, "Cliente creado con exito"
    except Exception as e:
       print(e)
