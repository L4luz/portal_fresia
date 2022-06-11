from socket import timeout
from django.shortcuts import render

#from portal_fresia.models import Cliente

def clientes(request):
    #clientesListados = Cliente.objects.all()

    return render(request, 'clientes.html')

def find_all():
    url='http://127.0.0.1:8000/api/v1/clients'
    print('CALL REST SERVICE {0}'.format(url))

    try:
        response = request.get(url,timeout=(5,15))

        if(response.status_code == 200):
            clientes_json =response.json()
            print('response: {0}'.format(clientes_json))

            for client_json in clientes_json:
                
                clientes_json(
                    {
                        "id_cliente": client_json['id_cliente'],
                        "email":client_json['email'],
                        "rut": client_json['rut'],
                        "contrasena": client_json['contrasena'],
                        "nombre": client_json['nombre'],
                        "fecha_de_nac": client_json['fecha_de_nac'],
                        "id_genero_id":client_json['id_genero_id'],
                        "id_estado_civil_id":client_json['id_estado_civil_id'],
                        "id_tarjeta_cliente_id": client_json['id_tarjeta_cliente_id'],
                    }
                )
    except Exception in e:
        print(e)
    return clientes

        
def add(client_json):
    url='http://127.0.0.1:8000/api/v1/add-clients'
    print('CALL REST SERVICE {0}'.format(url))
   
    try:
        response = request.post(url,timeout=(5,15),data=client_json)

        if(response.status_code == 200):
            clientes_json =response.json()
            print('response: {0}'.format(clientes_json))
    except Exception in e:
        print(e)
    return "clientes"
