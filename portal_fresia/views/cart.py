from django.shortcuts import render
import requests

def cart(request):
    print('cart')

    control = { 'image' : 'img/MODELOS/MODELO 9 CAPRI/CAPRI (4).jpeg',
                'product': 'XBOX GAMEPAD',
                'description': 'BLACK COLOR',
                'price' : 59000,
                'quantity': 1
                }
                
    gabinete = {'image' : 'img/MODELOS/MODELO 9 CAPRI/CAPRI (1).jpeg',
                'product': 'CABINET',
                'description': 'BLACK MATE COLOR',    
                'price' : 69000,
                'quantity': 1
                }

    notebook = {'image' : 'img/MODELOS/MODELO 9 CAPRI/CAPRI (2).jpeg',
                'product': 'GAMER LAPTOP',
                'description': 'WHITE COLOR',    
                'price' : 2150000,
                'quantity': 1
                }                   

    products = [control, gabinete, notebook]
    total = control.get('price') + gabinete.get('price') + notebook.get('price')

    return render(request, 'cart.html', {'products' : products, 'total': total})
    