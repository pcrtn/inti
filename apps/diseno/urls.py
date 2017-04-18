from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.diseno.views import inicio_dis, diseno_proyecto, diseno_producto


urlpatterns = [
	url(r'^$', login_required(inicio_dis), name='inicio_dis'),
	url(r'^proyectos/', login_required(diseno_proyecto), name='diseno_proyecto'),
	url(r'^productos/$', diseno_producto, name='diseno_producto'),
	# url(r'^editar/(?P<id_proyecto>\d+)/$', proyecto_edit, name='proyecto_edit'),
	# url(r'^inicio/', login_required(inicio), name='inicio'),
]