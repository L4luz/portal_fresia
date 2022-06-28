from itertools import product
from django.shortcuts import render
from portal_fresia.models import CarritoCompra


def carrito_compra(request):
    products = []
    total = 0

    if request.user != None:
        if request.method == 'GET':
            codigo = request.GET.get('codigo')
            if codigo is not None:
                try:
                    elemento =  CarritoCompra.objects.get(id_carrito_compra = codigo)
                    elemento.delete()
                except Exception as e: 
                    print(e)
        queryset = CarritoCompra.objects.filter(id_cliente=request.user.id)
        carritoCompra =queryset.all()
        id_cliente=request.POST.get('id-user')
        
        for carrito in carritoCompra:
            print('id_cliente1', carrito.id_cliente.id_cliente)
            print('id_cliente2', id_cliente)
            print('id_cliente', carrito.id_cliente)
            print('id_modelo', carrito.id_modelo)
            print('VALOR', carrito.id_modelo.valor)
            print('id_talla', carrito.id_talla)
            products = [carrito.id_modelo]
            total = total + carrito.id_modelo.valor
        return render(request, 'cart.html',  {'carritoCompra': carritoCompra, 'total': total })
   
    return render(request, 'cart.html', {'products' : products, 'total': total})
    

    
