from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
     nombre = models.CharField(max_length=100, blank=False)
     email = models.EmailField(max_length=100, blank=False)
     telefono = models.CharField(max_length=15, blank=False)

     def __str__(self):
        return f"{self.nombre}"

class Vendedor(models.Model):
     nombre = models.CharField(max_length=100, blank=False)
     email = models.EmailField(max_length=100, blank=False)
     telefono = models.CharField(max_length=15, blank=False)

     def __str__(self):
        return f"{self.nombre}"

class Producto(models.Model):
     nombre = models.CharField(max_length=100, blank=False)
     precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

     def __str__(self):
        return f"{self.nombre}"

class Venta(models.Model):
     producto = models.CharField(max_length=100, blank=False)
     precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
     cantidad = models.DecimalField(max_digits=10, decimal_places=0, blank=False)
     
     def __str__(self):
        return f"{self.producto}"
     
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatars")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
   