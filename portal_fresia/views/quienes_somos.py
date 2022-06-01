from django.shortcuts import render

def quienes_somos(request):
    return render(request, 'quienes_somos.html')