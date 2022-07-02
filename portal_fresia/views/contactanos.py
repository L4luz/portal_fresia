from django.shortcuts import redirect, render
from portal_fresia.lib.sendmail import build_and_send

def contactanos(request):

    if request.method == 'POST':
        enviar_correo(request)

    return render(request, 'contactanos.html')

def enviar_correo(request):
    nombre = request.POST.get('nombre')
    mail = request.POST.get('mail') #Destinatario
    password = request.POST.get('password')
    print('MAIL: ', mail)
    print('PASSWORD: ', password)    
    #Leer información del formulario
    build_and_send(mail, 'portalfresia@outlook.com', '@Portal123', 'm.outlook.com', '587', nombre)
    