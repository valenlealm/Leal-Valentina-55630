
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import *
from .forms import * 

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "app_ventas/home.html")

def about_me(request):
    return render(request, "app_ventas/about_me.html")

@login_required
def productos(request):
    contexto = {'productos': Producto.objects.all(), 'titulo': 'Reporte de Productos' }
    return render(request, "app_ventas/producto_list.html", contexto)

@login_required
def clientes(request):
    contexto = {'clientes': Cliente.objects.all(), 'titulo': 'Reporte de Clientes' }
    return render(request, "app_ventas/cliente_list.html", contexto)

@login_required
def vendedores(request):
    contexto = {'vendedores': Vendedor.objects.all(), 'titulo': 'Reporte de Vendedores' }
    return render(request, "app_ventas/vendedor_list.html", contexto)

@login_required
def ventas(request):
    contexto = {'ventas': Venta.objects.all(), 'titulo': 'Reporte de Ventas' }
    return render(request, "app_ventas/venta_list.html", contexto)



def buscar_resultados(request):
    query = request.GET.get('buscar')
    resultados = Cliente.objects.filter(nombre__icontains=query)
    contexto = {"clientes": resultados}
    return render(request, 'app_ventas/clientes.html', contexto)

def consultacliente(request):
    return render(request, "app_ventas/consultacliente.html")


#____________________ CLASS BASED VIEW

#CLIENTES
class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    success_url = reverse_lazy('clientes')

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    success_url = reverse_lazy('clientes')

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')


##VENDEDORES
class VendedoresList(LoginRequiredMixin, ListView):
    model = Vendedor

class VendedorCreate(LoginRequiredMixin, CreateView):
    model = Vendedor
    fields = ['nombre', 'email', 'telefono']
    success_url = reverse_lazy('vendedores')

class VendedorUpdate(LoginRequiredMixin, UpdateView):
    model = Vendedor
    fields = ['nombre', 'email', 'telefono']
    success_url = reverse_lazy('vendedores')

class VendedorDelete(LoginRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('vendedores')


##PRODUCTOS
class ProductoList(LoginRequiredMixin, ListView):
    model = Producto

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['nombre', 'precio']
    success_url = reverse_lazy('productos')

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'precio']
    success_url = reverse_lazy('productos')

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')


## VENTAS
class VentaList(LoginRequiredMixin, ListView):
    model = Venta

class VentaCreate(LoginRequiredMixin, CreateView):
    model = Venta
    fields = ['producto', 'precio', 'cantidad']
    success_url = reverse_lazy('ventas')

class VentaUpdate(LoginRequiredMixin, UpdateView):
    model = Venta
    fields = ['producto', 'precio', 'cantidad']
    success_url = reverse_lazy('ventas')

class VentaDelete(LoginRequiredMixin, DeleteView):
    model = Venta
    success_url = reverse_lazy('ventas')


#____________________ LOGIN /LOGOUT / REGISTER

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatars/default.jpg"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "app_ventas/index.html", {'mensaje': f'Bienvenidx a A dministración Ventas {usuario}'})
            else:
                return render(request, "app_ventas/login.html", {'form': miForm, 'mensaje': f'Por favor valida tus datos para ingresar'})
        else:
            return render(request, "app_ventas/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "app_ventas/login.html", {"form":miForm})    

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "app_ventas/index.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "app_ventas/registro.html", {"form":miForm}) 


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"app_ventas/index.html")
        else:
            return render(request,"app_ventas/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "app_ventas/editarPerfil.html", {'form': form, 'usuario': usuario.username})


##_______________________________AVATARES

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Borrar avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar nuevo avatar
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"app_ventas/index.html")
    else:
        form = AvatarFormulario()
    return render(request, "app_ventas/agregarAvatar.html", {'form': form })


