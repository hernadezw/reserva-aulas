from django import forms
from .models import Reserva, Curso

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['aula', 'curso', 'fecha', 'hora_inicio', 'hora_fin']

class FormCurso(forms.ModelForm):
    class Meta:
        model=Curso
        fields=['nombre', 'codigo', 'profesor']