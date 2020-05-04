from django.db import models


class Ingrediente(models.Model):
    nombre=models.CharField(max_length=200,)
    descripcion=models.TextField(max_length=1000)

    # def __str__(self):
    #     return self.name


class Hamburguesa(models.Model):
    nombre=models.CharField(max_length=200)
    precio = models.IntegerField(default=0)
    descripcion=models.TextField(max_length=1000)
    imagen=models.URLField(max_length = 200) 
    ingredientes=models.ManyToManyField(Ingrediente,blank=True,default='')

    def __str__(self):
        return self.nombre


