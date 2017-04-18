from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]

		labels = {
			'username': '',
			'first_name': '',
			'last_name': '',
			'email': '',
		}

		widgets = {
			'username': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Usuario'}),
			'first_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Nombre'}),
			'last_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Apellido'}),
			'email': forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Correo'}),
		}
