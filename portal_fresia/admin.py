from django.contrib import admin
from portal_fresia.models import Cliente,Compra,Comuna ,Direccion , DocumentoTributario,Envio , EstadoCivil,EstadoEnvio , Genero, Insumo,Invitado 
from portal_fresia.models import Material,Producto , ProductoCompra,Region ,TarjetaCliente ,TipoDocumTribu ,TipoPago , TipoProducto,TipoTarjeta ,Trabajador 

class ClienteForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']

class GeneroForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
class EstadoCivilForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']

admin.site.register(Cliente, ClienteForm)
admin.site.register(Genero,GeneroForm)
admin.site.register(EstadoCivil,EstadoCivilForm)
admin.site.register(TarjetaCliente)
admin.site.register(Compra)
admin.site.register(EstadoEnvio)
admin.site.register(Insumo)
admin.site.register(Material)
admin.site.register(Producto)
admin.site.register(ProductoCompra)
admin.site.register(TipoDocumTribu)
admin.site.register(TipoPago)
admin.site.register(TipoProducto)
admin.site.register(TipoTarjeta)



#from.models import Cliente

#admin.site.register(Cliente)