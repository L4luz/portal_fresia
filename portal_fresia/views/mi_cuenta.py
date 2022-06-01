from django.shortcuts import render

def mi_cuenta(request):
    return render(request, 'mi_cuenta.html')