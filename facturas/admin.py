from django.contrib import admin
from .models import *
# Register your models here.



# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nit', 'nombre', 'telefono')

class HeladoAdmin(admin.ModelAdmin):
    list_display = ('id_helado', 'tipo', 'sabor', 'tam', 'precio')

class ToppingAdmin(admin.ModelAdmin):
    list_display = ('id_topping', 'nombre', 'precio')

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id_factura', 'fecha', 'cliente')

class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('id_detalle', 'factura', 'helado', 'topping', 'cantidad')

class ValorFacturaAdmin(admin.ModelAdmin):
    list_display=('id_valorFactura','factura','total')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Helado, HeladoAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(DetalleFactura, DetalleFacturaAdmin)
admin.site.register(ValorFactura, ValorFacturaAdmin)
