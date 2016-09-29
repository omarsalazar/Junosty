from django import forms
from .models import datosusuario
from django.utils.translation import ugettext_lazy as _

class registroForm(forms.ModelForm):
    class Meta:
        model = datosusuario
        fields = '__all__'
        labels = {
            'contrasena': _(''),
            'nombre':_(''),
            'no_boleta':_(''),
            'apellidos':_(''),
            'curp':_(''),
            'carrera':_(''),
            'fecha_nacimiento':_(''),
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'type':'text',
                'placeholder':'Nombre',
                'class': 'validate',
            }),
            'no_boleta': forms.TextInput(attrs={
                'type':'text',
                'placeholder':'Boleta',
                'class': 'validate',
            }),
            'apellidos': forms.TextInput(attrs={
                'type':'text',
                'placeholder':'Apellidos',
                'class': 'validate',
            }),
            'carrera': forms.TextInput(attrs={
                'type':'text',
                'placeholder':'Carrera',
                'class': 'validate',
            }),
            'contrasena': forms.TextInput(attrs={
                'type': 'password',
                'placeholder':'Contraseña',
                'class': 'validate',
            }),
            'user': forms.TextInput(attrs={
                'type': 'hidden',
                'class': 'validate',
            }),
        }

class inicioForm(forms.ModelForm):
    class Meta:
        model = datosusuario
        #Esto se hace cuando no quieres todos los campos del modelo. Es una lista uwu
        fields = ('no_boleta', 'contrasena')
        labels = {
            'contrasena': _(''),
            'no_boleta':_(''),
            }
        widgets = {
            'no_boleta': forms.TextInput(attrs={
                'type':'text',
                'placeholder':'Boleta',
                'class': 'validate',
            }),
            'contrasena': forms.TextInput(attrs={
                'type': 'password',
                'placeholder':'Contraseña',
                'class': 'validate',
            }),
        }
class modificarForm(forms.ModelForm):
    class Meta:
        model = datosusuario
        fields = ('contrasena', 'apellidos','nombre')

        labels = {
            'contrasena': _(''),
            'nombre':_(''),
            'apellidos':_(''),
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'type':'text',
                'placeholder':'Nombre',
                'class': 'validate',
            }),
            'apellidos': forms.TextInput(attrs={
                'type':'text',
                'placeholder':'Apellidos',
                'class': 'validate',
            }),
            'contrasena': forms.TextInput(attrs={
                'type': 'password',
                'placeholder':'Contraseña',
                'class': 'validate',
            }),

        }
