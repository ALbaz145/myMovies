from django import forms
from .models import Resena

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['usuario', 'texto', 'calificacion']
        widgets = {
            'usuario': forms.TextInput(attrs={
                'placeholder': 'Tu nombre o apodo',
                'class': 'bg-slate-800 border-slate-700 text-white rounded-lg p-2'
            }),
            'texto': forms.Textarea(attrs={
                'placeholder': '¿Qué te pareció la película?',
                'rows': 4,
                'class': 'bg-slate-800 border-slate-700 text-white rounded-lg p-2'
            }),
            'calificacion': forms.NumberInput(attrs={
                'min': 1, 
                'max': 10,
                'class': 'bg-slate-800 border-slate-700 text-white rounded-lg p-2'
            }),
        }
        