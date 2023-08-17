
from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
from .models import *

def home(request):
    return render(request, "app_ventas/home.html")

def productos(request):
    contexto = {'productos': Producto.objects.all(), 'titulo': 'Reporte de Productos' }
    return render(request, "app_ventas/productos.html", contexto)

def clientes(request):
    contexto = {'clientes': Cliente.objects.all(), 'titulo': 'Reporte de Clientes' }
    return render(request, "app_ventas/clientes.html", contexto)

def vendedores(request):
    contexto = {'vendedores': Vendedor.objects.all(), 'titulo': 'Reporte de Vendedores' }
    return render(request, "app_ventas/vendedores.html", contexto)


def insertar_datos(request):
    cliente_form = ClienteForm()

    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)

        if cliente_form.is_valid():
            cliente_nombre = cliente_form.cleaned_data.get('nombre')
            cliente_email = cliente_form.cleaned_data.get('email')
            cliente_telefono = cliente_form.cleaned_data.get('telefono')

            cliente = Cliente(nombre=cliente_nombre,email=cliente_email,telefono=cliente_telefono)
            cliente.save()
    else:

        cliente_form = ClienteForm()
    
    return render(request, "app_ventas/clienteform.html", {"form": cliente_form })



def buscar_resultados(request):
    query = request.GET.get('buscar')
    resultados = Cliente.objects.filter(nombre__icontains=query)
    contexto = {"clientes": resultados}
    return render(request, 'app_ventas/clientes.html', contexto)

def consultacliente(request):
    return render(request, "app_ventas/consultacliente.html")