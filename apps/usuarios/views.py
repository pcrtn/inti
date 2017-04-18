from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect

from apps.usuarios.forms import RegistroForm

# Create your views here.
class RegistroUsuario(CreateView):
	model = User
	template_name = "usuarios/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('usu:index')

def index(request):
	return render(request, 'usuarios/usuariocreado.html')

def recuperar(request):
	return render(request, 'usuarios/recuperar.html')