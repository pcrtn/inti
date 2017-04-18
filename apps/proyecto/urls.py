from django.conf.urls import url
from apps.proyecto.views import create_disenos, producto_edit, pru, proyecto_view, proyecto_home, proyecto_list,proyecto_edit, inicio, producto_proyecto, solicitud
from django.contrib.auth.decorators import login_required


urlpatterns = [
	url(r'^$', login_required(proyecto_view), name='proyecto_view'),
	url(r'^home/', login_required(proyecto_home), name='proyecto_home'),
	url(r'^list$', login_required(proyecto_list), name='proyecto_list'),
	url(r'^editar/(?P<id_proyecto>\d+)/$', login_required(proyecto_edit), name='proyecto_edit'),
	url(r'^inicio/', login_required(inicio), name='inicio'),
	url(r'^prueba/$', login_required(producto_proyecto), name='producto_proyecto'),
	url(r'^pru/(?P<id_proyecto>\d+)/(?P<id_producto>\d+)/$', login_required(pru), name='pru'),
	url(r'^ediproducto/(?P<id_producto>\d+)/$', login_required(producto_edit), name='producto_edit'),
	url(r'^solicitarcliente/$', login_required(solicitud), name='solicitud'),
	url(r'^diseños/$', login_required(create_disenos), name='create_disenos'),
]