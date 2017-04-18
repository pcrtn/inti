from django.db import models
from apps.proyecto.models import proyecto

# Create your models here.
class disenadores(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre

class acabadosGalvanico(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre

class materialesP(models.Model):
	nombre = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre

class producto(models.Model):
	idProyecto = models.ForeignKey(proyecto, on_delete=models.CASCADE, blank=True, null=True)
	nombre = models.CharField(max_length=30, blank=True, null=True)
	presupuesto = models.CharField(max_length=10, blank=True, null=True, default=0)
	unidades = models.CharField(max_length=10, blank=True, null=True, default=0)
	total = models.CharField(max_length=30, blank=True, null=True, default=0)
	muestraF = models.CharField(max_length=3, blank=True, null=True)
	numeroP = models.CharField(max_length=2, blank=True, null=True)
	materiales = models.ManyToManyField(materialesP, blank=True)
	acabados = models.ManyToManyField(acabadosGalvanico, blank=True) 
	descripcionP = models.CharField(max_length=200, blank=True, null=True)
	insumosD = models.CharField(max_length=200, blank=True, null=True)
	empaque = models.CharField(max_length=200, blank=True, null=True)
	disenador = models.ForeignKey(disenadores, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return	self.nombre

class diseno(models.Model):
	idProducto = models.ForeignKey(producto, on_delete=models.CASCADE, blank=True, null=True)
	nombre = models.CharField(max_length=40)

	def __str__(self):
		return self.nombre