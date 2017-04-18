from django import forms
from django.forms import ModelForm, Textarea
from apps.proyecto.models import proyecto, imgpyc

class ProyectoForm(forms.ModelForm):

	class Meta:
		model = proyecto

		fields = ('nombreCliente', 'nitCliente', 'asesor', 'valor','descripcion','descripcionP', 'tipoProyecto', 'fechaEntDis', 'fechaMueFis', 'fechaApr', 'fechaEntPro', 'descripcionF', 'selec')
		widgets = {
			'nombreCliente': forms.Select(attrs = {'class':'form-control','readonly':'readonly'}),
			'nitCliente': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Nit Cliente'}),
			'asesor': forms.Select(attrs = {'class':'form-control','readonly':'readonly'}),
			'valor': forms.TextInput(attrs = {'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Titulo del proyecto'}),
			'descripcionP':forms.Textarea(attrs = {'class': 'form-control wysihtml5'}), #wysihtml5
			'tipoProyecto': forms.Select(attrs = {'class':'form-control'}),
			'fechaEntDis': forms.TextInput(attrs={'class':'form-control datepicker','readonly':'readonly'}),
			'fechaMueFis': forms.TextInput(attrs={'class':'form-control datepicker','readonly':'readonly'}),
			'fechaApr': forms.TextInput(attrs={'class':'form-control datepicker','readonly':'readonly'}),
			'fechaEntPro': forms.TextInput(attrs={'class':'form-control datepicker','readonly':'readonly'}),
			'descripcionF':forms.Textarea(attrs = {'class': 'form-control wysihtml5'}),
			'selec': forms.CheckboxSelectMultiple({'class':'form-control col-md-9'}),
		}

class ImagenesPYCForm(forms.ModelForm):
	class Meta:
		model = imgpyc

		fields = ('proyecto', 'document')
