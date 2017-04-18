from django.conf.urls import url
from apps.usuarios.views import RegistroUsuario, index, recuperar

urlpatterns = [
	url(r'^registrar/', RegistroUsuario.as_view(), name="registro"),
	url(r'^completado/', index, name='index'),
	url(r'^recuperar/', recuperar, name='recuperar'),
]