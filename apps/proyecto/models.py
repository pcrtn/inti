from django.db import models
from django.contrib.auth.models import User

prueba = (('FR', 'Freshman'),('b', 'b'))

# Create your models here.
class cliente(models.Model):
	nit = models.IntegerField()
	nombre = models.CharField(max_length=125)
	telefono = models.IntegerField(blank=True, null=True)
	contacto = models.CharField(max_length=125, blank=True, null=True)
	correo = models.EmailField(max_length=125, blank=True, null=True)
	cargo = models.CharField(max_length=125, blank=True, null=True)

	def __str__(self):
		return	self.nombre

class tipoProyecto(models.Model):
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=125)

	def __str__(self):
		return self.nombre

class opcionesD(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre

class proyecto(models.Model):
	nombreCliente = models.ForeignKey(cliente, null=True, blank=True, on_delete=models.CASCADE)
	nitCliente = models.IntegerField()
	asesor = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
	fecha = models.DateField(auto_now_add=True)
	valor = models.IntegerField(default=0)
	descripcion = models.CharField(max_length=125)
	descripcionP = models.TextField(max_length=125, null=True, blank=True)
	tipoProyecto = models.ForeignKey(tipoProyecto, on_delete=models.CASCADE, null=True, blank=True)
	fechaEntDis = models.DateField(auto_now_add=False, blank=True, null=True)
	fechaMueFis = models.DateField(auto_now_add=False, blank=True, null=True)
	fechaApr = models.DateField(auto_now_add=False, blank=True, null=True)
	fechaEntPro = models.DateField(auto_now_add=False, blank=True, null=True)
	descripcionF = models.TextField(max_length=125, null=True, blank=True)
	selec = models.ManyToManyField(opcionesD, blank=True)

	def __str__(self):
		return self.descripcion

class item(models.Model):
	padre = models.CharField(max_length=60)
	hijo = models.CharField(max_length=60)
	ruta = models.CharField(max_length=60)
	font = models.CharField(max_length=60, blank=True, null=True)

	def __str__(self):
		return self.padre

class imgpyc(models.Model):
	proyecto = models.CharField(max_length=4, blank=True, null=True)
	document = models.FileField(upload_to='imagenesProyecto/')
	uploaded_at = models.DateTimeField(auto_now_add=True)