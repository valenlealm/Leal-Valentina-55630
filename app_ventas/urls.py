from django.urls import path, include
from .views import *

urlpatterns = [
	path('insertar/', insertar_datos, name='insertar_datos'),
	path('buscar/', buscar_resultados, name='buscar'),
    path('productos/', productos, name='productos'),
    path('clienteform/', insertar_datos, name='clienteform'),
    path('clientes/', clientes, name='clientes'),
    path('', home, name='home'),
    path('buscar_resultados/', buscar_resultados, name='buscar_resultados'),
    path('consultacliente/', consultacliente, name='consultacliente'),
    path('vendedores/', vendedores, name='vendedores'),

]