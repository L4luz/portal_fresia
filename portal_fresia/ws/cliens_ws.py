from urllib import response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from portal_fresia.models import Cliente

from portal_fresia.views.region_controller import find_all
from django.http import JsonResponse
from portal_fresia.rules.client_rules import find_all,add

@api_view(['GET'])
def find_client_all(request):

    clients = find_all()
    print(clients)
    return JsonResponse(list(clients.values()), safe=False,json_dumps_params={'ensure_ascii': False})
 
@api_view(['POST'])
def add_client(request):

    print(request.data)
    client =Cliente(
            email = request.data.get('email'),
            rut = request.data.get('rut'),
            contrasena = request.data.get('contrasena'),
            nombre = request.data.get('nombre'),
            fecha_de_nac = request.data.get('fecha_de_nac'),
            id_genero_id = request.data.get('id_genero_id'),
            id_estado_civil_id = request.data.get('id_estado_civil_id'),
            id_tarjeta_cliente_id = request.data.get('id_tarjeta_cliente_id')
    )
    response = add(client)
    return JsonResponse({},safe=False,json_dumps_params={'ensure_ascii':False})