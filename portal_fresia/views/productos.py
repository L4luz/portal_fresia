from django.shortcuts import render
from django.shortcuts import render

from portal_fresia.models import AuthUser, CarritoCompra, Cliente, Compra, Modelo, Producto, Talla, Color, TipoProducto,Material

def productos(request):
    return render(request, 'productos.html')


def crear_productos(request):
    estado = False
    mensaje = None
    if request.method == 'POST':
        estado, mensaje = add_producto(request)
    productos = Producto.objects.all()
    modelos = Modelo.objects.all()
    tallas = Talla.objects.all()
    colores = Color.objects.all()
    tipo_productos = TipoProducto.objects.all()
    materiales = Material.objects.all()
  
  

    return render(request, 'productos.html',  {'productos':productos,'modelos': modelos,'tallas': tallas,'colores': colores,'tipo_productos': tipo_productos, 'materiales':materiales,'estado': estado, 'mensaje' : mensaje})



def add_producto(request):
    id_modelo=request.POST.get('id-modelo')
    id_talla=request.POST.get('id-talla')
    id_color=request.POST.get('id-color')
    id_tipo_producto=request.POST.get('id-tipo-producto')
    id_material=request.POST.get('id-material')
    id_cliente=request.POST.get('id-user')
 
    

    print('id_modelo', id_modelo)
    print('id_talla', id_talla)
    print('id_color', id_color)
    print('id_tipo_producto', id_tipo_producto)
    print('id_material', id_material)
    print('userID', id_cliente)
  
    carrito = CarritoCompra()
    carrito.id_modelo = Modelo.objects.get(pk=id_modelo)
    carrito.id_talla = Talla.objects.get(pk=id_talla)
    carrito.id_color = Color.objects.get(pk=id_color)
    carrito.id_tipo_producto = TipoProducto.objects.get(pk=id_tipo_producto)
    carrito.id_material = Material.objects.get(pk=id_material)
    carrito.id_cliente = Cliente.objects.get(pk=id_cliente)
    
   

    
    try:
        
        carrito.save()
        #compra.save()
        
        return True, "Producto agregado Correctamente"

    except Exception as e:
       print(e)