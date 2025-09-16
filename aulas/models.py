from django.db import models
from django.contrib.auth.models import User

class Aula(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - Capacidad: {self.capacidad}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    profesor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class Reserva(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"Reserva de {self.aula.nombre} por {self.usuario.username} el {self.fecha}"

