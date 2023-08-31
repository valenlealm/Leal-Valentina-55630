from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
	
    path('', home, name='home'),
    path('about_me/', about_me, name='about_me' ),

    path('buscar/', buscar_resultados, name='buscar'),
    path('buscar_resultados/', buscar_resultados, name='buscar_resultados'),
    path('consultacliente/', consultacliente, name='consultacliente'),

    path('clientes/', ClienteList.as_view(), name='clientes'),
    path('create_cliente/', ClienteCreate.as_view(), name="create_cliente" ),
    path('update_cliente/<int:pk>/', ClienteUpdate.as_view(), name="update_cliente" ),
    path('delete_cliente/<int:pk>/', ClienteDelete.as_view(), name="delete_cliente" ),

    path('vendedores/', VendedoresList.as_view(), name='vendedores'),
    path('create_vendedor/', VendedorCreate.as_view(), name="create_vendedor" ),
    path('update_vendedor/<int:pk>/', VendedorUpdate.as_view(), name="update_vendedor" ),
    path('delete_vendedor/<int:pk>/', VendedorDelete.as_view(), name="delete_vendedor" ),

    path('producto/', ProductoList.as_view(), name='productos'),
    path('create_producto/', ProductoCreate.as_view(), name="create_producto" ),
    path('update_producto/<int:pk>/', ProductoUpdate.as_view(), name="update_producto" ),
    path('delete_producto/<int:pk>/', ProductoDelete.as_view(), name="delete_producto" ),
   
    path('ventas/', VentaList.as_view(), name='ventas'),   
    path('create_venta/', VentaCreate.as_view(), name="create_venta" ),
    path('update_venta/<int:pk>/', VentaUpdate.as_view(), name="update_venta" ),
    path('delete_venta/<int:pk>/', VentaDelete.as_view(), name="delete_venta" ), 

    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="app_ventas/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),


]