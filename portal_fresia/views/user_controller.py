from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
import json
#import random

#ARREGLO QUE ALMACENA USUARIOS
array_users = []

@api_view(['GET', 'POST', 'PUT'])
def user(request):
    print('INIT user')
    if request.method == 'GET':
        print('method: GET')
        return HttpResponse(json.dumps(find_all()), content_type="application/json")
    if request.method == 'POST':
        print('method: POST')
        id = random.randint(1, 9999999999)
        body_unicode = request.body.decode('utf-8') 	
        payload = json.loads(body_unicode)
        new_user = create_or_update(payload, id)
        array_users.append(new_user)
        return HttpResponse(json.dumps(new_user), content_type="application/json")
    if request.method == 'PUT':
        body_unicode = request.body.decode('utf-8') 	
        payload = json.loads(body_unicode)
        user = None
        for idx, u in enumerate(array_users):
            if u['id'] == payload['id']:
                array_users[idx] = create_or_update(payload, u['id'])
                return HttpResponse(json.dumps(array_users[idx]), content_type="application/json") 
        if user is None:
            status_code = status.HTTP_404_NOT_FOUND
            return HttpResponse('Not Found User {0}'.format(id), content_type='application/json')

@api_view(['GET', 'DELETE'])
def user_by_id(request, id):
    user = None
    print('INIT find_by_id')
    for u in array_users:
        if u['email'] == id:
            user = u
    if user is None:
        status_code = status.HTTP_404_NOT_FOUND
        return HttpResponse('Not Found User {0}'.format(id), content_type='application/json')
    else: 
        if request.method == 'GET':
            status_code = status.HTTP_200_OK 
            return HttpResponse(json.dumps(user), content_type='application/json')
        if request.method == 'DELETE':
            status_code = status.HTTP_200_OK
            array_users.remove(user)
            return HttpResponse('user {0} deleted'.format(id), content_type='text/plain')        

def find_all():
    return array_users

def create_or_update(payload, id):
    email = payload['id']
    email = payload['email']
    rut = payload['rut']
    nombre = payload['nombre']
    fecha_de_nac = payload['fecha_de_nac']
    genero_id_genero = payload['genero_id_genero']
    estado_civil_id_estadocivil = payload['estado_civil_id_estadocivil']
    wallet_cliente_numero_tarjeta = payload['wallet_cliente_numero_tarjeta']
    contrasena = payload['contrasena']
    user =  {
        'id' : id,
        'email' : email,
        'rut' : rut,
        'nombre' : nombre,
        'fecha_de_nac' : fecha_de_nac,
        'genero_id_genero' : genero_id_genero,
        'estado_civil_id_estadocivil' : estado_civil_id_estadocivil,
        'wallet_cliente_numero_tarjeta' : wallet_cliente_numero_tarjeta,
        'contrasena' : contrasena
       
    }
    return user