from django import forms
from apps.diseno.models import producto, diseno
from apps.proyecto.models import *

class productoForm(forms.ModelForm):

	class Meta:

		model = producto
		fields = ('idProyecto', 'nombre', 'presupuesto', 'unidades', 'total', 'muestraF', 'numeroP', 'materiales', 'acabados', 'descripcionP', 'insumosD', 'empaque', 'disenador')
		widgets = {
			'idProyecto': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'idProyecto', 'style': 'display:none;' }),
			'nombre': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'nombre', 'style': 'display:none;' }),
			'presupuesto': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Presupuesto del producto'}),
			'unidades': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Unidades del producto'}),
			'total': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Valor total del producto'}),
			'muestraF': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'muestraF'}),
			'numeroP': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'numeroP'}),
			'materiales': forms.CheckboxSelectMultiple({'class':'form-control col-md-9'}),
			'acabados': forms.CheckboxSelectMultiple({'class':'form-control'}),
			'descripcionP': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Describa el producto'}),
			'insumosD':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Mencione los insumos decorativos'}),
			'empaque':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Describa los empaques del proyecto'}),
		}

class disenoForm(forms.ModelForm):

	class Meta:

		model = diseno
		fields = ('__all__')