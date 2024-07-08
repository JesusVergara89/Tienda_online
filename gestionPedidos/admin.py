from django.contrib import admin

from gestionPedidos.models import clientes,articulos,pedidos

class clientes_admin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono")
    search_fields=("nombre","direccion","telefono")

class articulos_admin(admin.ModelAdmin):
    list_filter=("nombre","seccion","precio")

class pedido_admin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(clientes,clientes_admin)
admin.site.register(articulos,articulos_admin)
admin.site.register(pedidos,pedido_admin)

