from email import message
from portal_fresia.models import Cliente

def find_all():
    return Cliente.objects.all().order_by('nombre')

def add(cliente):
    cliente.save()
    message = 'CLIENTE {0} {1}'
    code = 0
    return{
        'message':message,
        'code':code}