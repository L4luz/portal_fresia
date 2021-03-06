from django.contrib import admin
from portal_fresia.models import AreaTrabajo, Cliente,Compra,Comuna ,Direccion , DocumentoTributario,Envio , EstadoCivil,EstadoEnvio , Genero, Insumo,Invitado 
from portal_fresia.models import CarritoCompra,Compra,Material,Producto , ProductoCompra,Region ,TarjetaCliente ,TipoDocumTribu ,TipoPago , TipoProducto,TipoTarjeta ,Trabajador ,Modelo,Talla,Color

class AreaTrabajoForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['descripcion']
admin.site.register(AreaTrabajo, AreaTrabajoForm)


class ClienteForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Cliente, ClienteForm)

class ComunaForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Comuna, ComunaForm)

class DireccionForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Direccion, DireccionForm)

class EstadoCivilForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(EstadoCivil,EstadoCivilForm)

class EstadoEnvioForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(EstadoEnvio,EstadoEnvioForm)

class GeneroForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Genero,GeneroForm)

class InsumoForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Insumo,InsumoForm)

class InvitadoForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['email']
admin.site.register(Invitado,InvitadoForm)

class MaterialForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Material,MaterialForm)

class ProductoForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['id_producto']
admin.site.register(Producto,ProductoForm)

class RegionForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Region,RegionForm)

class TarjetaClientelForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(TarjetaCliente,TarjetaClientelForm )

class TipoDocumTribuForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(TipoDocumTribu,TipoDocumTribuForm)

class TipoPagoForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(TipoPago,TipoPagoForm)

class TipoProductoForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(TipoProducto,TipoProductoForm)

class TipoTarjetaForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(TipoTarjeta,TipoTarjetaForm)

class TrabajadorForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Trabajador,TrabajadorForm)


class ModeloForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Modelo,ModeloForm)

class TallaForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Talla,TallaForm)

class ColorForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['nombre']
admin.site.register(Color,ColorForm)


class CompraForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['id_compra']
admin.site.register(Compra,CompraForm)

class CarritoCompraForm(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['id_carrito_compra']
admin.site.register(CarritoCompra,CarritoCompraForm)



#from.models import Cliente

#admin.site.register(Cliente)