from django.db import models

class Cliente(models.Model):
     nombre = models.CharField(max_length=100)
     email = models.EmailField(max_length=100)
     telefono = models.CharField(max_length=15)


class Vendedor(models.Model):
     nombre = models.CharField(max_length=100)
     email = models.EmailField(max_length=100)
     telefono = models.CharField(max_length=15)


class Producto(models.Model):
     nombre = models.CharField(max_length=100)
     precio = models.DecimalField(max_digits=10, decimal_places=2)
