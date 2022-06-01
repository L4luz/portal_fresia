from django.shortcuts import render
from portal_fresia.models import Region

def index_region(request):
    return render(request, 'region.html')

def add_region(request):
    print('add_regiont INIT')
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        print('id: ', id)
        print('nombre: ', nombre)
        region = Region()
        region.id_region = id
        region.nombre = nombre
        region.save()
    return render(request, 'region.html')