from django.shortcuts import render
from apps.proyecto.models import item, proyecto
from apps.diseno.models import producto

i = item.objects.all()

# Create your views here.
def inicio_dis(request):
	return render(request, 'diseno/inicio.html', {'i':i})

def diseno_proyecto(request):
	p = proyecto.objects.all()
	return render(request, 'diseno/verProyecto.html', {'i':i, 'p':p})

def diseno_producto(request):
	pro = producto.objects.all()
	return render(request, 'diseno/verProducto.html', {'i':i, 'pro':pro})