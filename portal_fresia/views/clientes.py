from django.shortcuts import render
#from portal_fresia.models import Cliente

def clientes(request):
    #clientesListados = Cliente.objects.all()

    return render(request, 'clientes.html',{"clientes":''})