from django.contrib import admin
from portal_fresia.models import Region, Comuna, Compra, EstadoCivil, EstadoEnvio, Genero, Insumo, Material, Producto, ProductoCompra, TipoDocumTribu, TipoPago, TipoProducto


class RegionForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']

admin.site.register(Region, RegionForm)

class ComunaForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']

admin.site.register(Compra)
admin.site.register(EstadoCivil)
admin.site.register(EstadoEnvio)
admin.site.register(Genero)
admin.site.register(Insumo)
admin.site.register(Material)
admin.site.register(Producto)
admin.site.register(ProductoCompra)
admin.site.register(TipoDocumTribu)
admin.site.register(TipoPago)
admin.site.register(TipoProducto)


#from.models import Cliente

#admin.site.register(Cliente)