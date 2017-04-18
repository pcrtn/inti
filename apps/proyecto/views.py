from django.shortcuts import render
from django.http import HttpResponse
from apps.proyecto.models import item
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from apps.proyecto.models import proyecto, cliente
from apps.proyecto.forms import ProyectoForm, ImagenesPYCForm
import time
from django.shortcuts import redirect
from apps.diseno.forms import productoForm, disenoForm
from apps.diseno.models import producto, diseno
from datetime import datetime,timedelta, date

#variables publicas
i = item.objects.all()
f = time.strftime("%d/%m/%y")


# Vistas PROYECTO

#Creación de proyectos
def proyecto_view(request):
	client = cliente.objects.all()
	if request.method == 'POST':
		print('ingreso')
		# create a form instance and populate it with data from the request:
		form = ProyectoForm(request.POST)
		# check whether it's valid:
		print   ("siii")
		if form.is_valid():
			id_proyecto = form.save()
		return redirect('pyc:proyecto_edit', id_proyecto.id)
	else:
		form = ProyectoForm()

	return render(request, 'proyecto/index.html', {'i':i, 'form':form, 'f':f, 'client':client})

#creación de producto
def producto_proyecto(request):
	if request.method == 'POST':
		print('ingreso')
		# create a form instance and populate it with data from the request:
		form = productoForm(request.POST)
		# check whether it's valid:
		print   ("siii")
		if form.is_valid():
			if form.cleaned_data['nombre'] == '':
				print ('nombre vacio')
			else:

				form.idProyecto = form.cleaned_data['idProyecto']
				form.nombre = form.cleaned_data['nombre']
				id_producto = form.save()
				return redirect('pyc:producto_edit', id_producto.id)
			return HttpResponse("Error!!!")
	else:
		return HttpResponse("Error!!!")

	return render(request, 'proyecto/index.html', {'i':i, 'f':f})


#edicción de productos
def producto_edit(request, id_producto):
	dise = diseno.objects.filter(idProducto=id_producto)
	product =  producto.objects.get(id=id_producto)
	disForm = disenoForm()
	if request.method == 'GET':
		form = productoForm(instance=product)	
	else:
		form = productoForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
	return render(request, 'proyecto/editprod.html', {'form':form, 'i':i, 'product':product, 'dise':dise, 'disForm':disForm})


#Primera vista despues del login
def proyecto_home(request):
	return render(request, 'base/base.html', {'i':i})

#lista de proyectos
def proyecto_list(request):
	p = proyecto.objects.all()
	ar = []
	h = date.today() 
	for x in p:
		a = x.fecha
		dias = a+timedelta(days=2)
		ar.append(dias<=h)
		print(ar)
	return render(request, 'proyecto/list.html', {'i':i, 'p':p})

#edicción de proyectos
def proyecto_edit(request, id_proyecto):
	# if request.user.is_authenticated:
	# 	print("authenticado")
	# else:
	# 	print("Negativo")
	prod = producto.objects.filter(idProyecto=id_proyecto)
	print(prod)
	proyect =  proyecto.objects.get(id=id_proyecto)
	a = id_proyecto
	b = proyecto.objects.filter(id=id_proyecto)
	fe = ''
	for s in b:
		fe = s.fecha
	print(request.user.is_authenticated)
	if request.method == 'GET':
		form = ProyectoForm(instance=proyect)
		imgPyc = ImagenesPYCForm()
	else:
		form = ProyectoForm(request.POST, instance=proyect)
		if form.is_valid():
			form.save()
	if request.method == 'POST':
		imgPyc = ImagenesPYCForm(request.POST, request.FILES)
		if imgPyc.is_valid():
			print("formulario imgpyc")
		return redirect('pyc:proyecto_list')
	return render(request, 'proyecto/editpyc.html', {'form':form,'i':i,'a':a, 'fe': fe, 'imgPyc':imgPyc, 'prod':prod})

#Vista inicial de Matrícula de proyectos
def inicio(request):
	pyc=proyecto.objects.all()
	c = pyc.count()
	return render(request, 'proyecto/inicio.html', {'i':i, 'c':c})

#prueba
def pru(request, id_proyecto, id_producto):
	print(id_proyecto)
	print(id_producto)
	return HttpResponse("prueba")

#Creación solicitud de clientes
def solicitud(request):
	return render(request, 'proyecto/SolicitudCliente.html', {'i':i})

#Creación diseños
def create_disenos(request):
	print('entro al diseno')
	if request.method == 'POST':
		form = disenoForm(request.POST)
		if form.is_valid():
			f = form.save()
			return redirect('proyecto_list')
	return HttpResponse('prueba2')