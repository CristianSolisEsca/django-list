from django.db import models

# Create your models here.

class Usuario(models.Model):
    
    genero_eleccion = (
                ('F','Femenino'),
                ('M','Masculino'),
    )
    
    codigo = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    genero = models.CharField(choices=genero_eleccion, max_length=100)
    ciudad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
