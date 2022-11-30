from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# ********************************************************************************************
#   Creación del usuario extendido
#
# ********************************************************************************************


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.user

# ********************************************************************************************
#   Creación del registro de casos
# ********************************************************************************************

class Case(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='cases', verbose_name='Usuarios')
    name = models.CharField(max_length=100, blank=False,
                            verbose_name='Empresa')
    nitempresa = models.IntegerField(max_length=100, verbose_name='Nit Empresa')
    rams = models.CharField(max_length=100, blank=True,
                            verbose_name='N. RANSOMWARE')
    detail = models.CharField(max_length=500, verbose_name='Detalle del caso')
    imagen = models.ImageField(verbose_name="Image", null=True)
    email = models.CharField(max_length=500, verbose_name='Mensaje de rescate')
    wallet = models.CharField(max_length=100, verbose_name='Moneda')
    timestamp = models.DateTimeField(
        default=timezone.now, verbose_name='Fecha')

    class Meta:
        ordering = ['-timestamp']
#self.user, self.name, self.nitempresa, self.rams, self.detail, self.imagen, self.exte, self.email, self.wallet, self.timestamp

    def __str__(self):
        return self.name

class Encuesta(models.Model):
    id = models.AutoField(primary_key=True)
    
    question1 = models.CharField(max_length=100, verbose_name='Pregunta 1', blank=True)
    question2 = models.CharField(max_length=500, verbose_name='Pregunta 2', blank=True)
    question3 = models.CharField(max_length=500, verbose_name='Pregunta 3', blank=True)
    question4 = models.CharField(max_length=500, verbose_name='Pregunta 4', blank=True)
    question5 = models.CharField(max_length=500, verbose_name='Pregunta 5', blank=True)
    question6 = models.CharField(max_length=500, verbose_name='Pregunta 6', blank=True)
    question7 = models.CharField(max_length=500, verbose_name='Pregunta 7', blank=True)
    question8 = models.CharField(max_length=500, verbose_name='Pregunta 8', blank=True)

    def __str__(self):
        return self.question1


class Metodologia(models.Model):
    id = models.AutoField(primary_key=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE,
                             related_name='metodologia', verbose_name='Casos', blank=False)
    name = models.CharField(max_length=100, blank=False, verbose_name='Nombre')

    def __str__(self):
        return self.name
