from django.contrib import admin
from apps.proyecto.models import cliente, tipoProyecto, proyecto, item, opcionesD, imgpyc

# Register your models here.
admin.site.register(cliente)
admin.site.register(tipoProyecto)
admin.site.register(proyecto)
admin.site.register(item)
admin.site.register(opcionesD)
admin.site.register(imgpyc)