from django.contrib import admin
from apps.diseno.models import diseno, producto, materialesP, acabadosGalvanico, disenadores

# Register your models here.
admin.site.register(producto)
admin.site.register(materialesP)
admin.site.register(acabadosGalvanico)
admin.site.register(disenadores)
admin.site.register(diseno)