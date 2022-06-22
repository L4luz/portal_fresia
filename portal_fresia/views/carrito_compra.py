from django.shortcuts import render
from portal_fresia.models import CarritoCompra


def carrito_compra(request):
    carritoCompra = CarritoCompra.objects.all()
    id_cliente=request.POST.get('id-user')
    for carrito in carritoCompra:
        print('id_cliente1', carrito.id_cliente.id_cliente)
        print('id_cliente2', id_cliente)
        if(carrito.id_cliente.id_cliente == 14):
            print('id_cliente', carrito.id_cliente)
            print('id_modelo', carrito.id_modelo)
            print('VALOR', carrito.id_modelo.valor)
            print('id_talla', carrito.id_talla)
            products = [carrito.id_modelo]
            total = carrito.id_modelo.valor
            return render(request, 'cart.html',  {'carritoCompra': carritoCompra })
        else:
            print('Debe iniciar sesion')  
            return render(request, 'cart.html')
    return render(request, 'cart.html', {'products' : products, 'total': total})
    

    
