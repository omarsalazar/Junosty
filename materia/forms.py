from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _

class MateriaForm(forms.ModelForm):
    class Meta:
        model = datosmateria
        fields = ('materia', 'profesor', 'grupo')
        labels = {
            'materia': _(''),
            'profesor': _(''),
            'grupo': _('')
        }
        widgets = {
            'materia': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la materia'
                    'required'
                }
            ),
            'profesor': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Profesor que imparte'
                    'required'
                }
            ),
            'grupo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Grupo de la materia'
                    'required'
                }
            ),
        }
