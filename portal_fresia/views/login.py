from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from portal_fresia.lib.autogenerate import generate


def authentication(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)            
        except Exception as e:
            print('Error: ', e)
    return redirect('home/')

def authorization(request, perm):
    if request.user != None:
        if request.user.has_perm(perm):
            return True
        else:
            return False
    else:
        return False

def send_mail_recovery_pass(username):
    return None

def recovery_pass(request):
    print('new key', generate(32))
    return None    