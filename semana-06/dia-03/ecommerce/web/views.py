from django.shortcuts import render, redirect
from .models import( Categoria, Marca, Producto)

# Create your views here.

def index(request):
    lista_productos = Producto.objects.all()
    lista_categorias = Categoria.objects.all()
    lista_marcas = Marca.objects.all()

    context = {
        'productos': lista_productos,
        'categorias': lista_categorias,
        'marcas': lista_marcas
    }
    return render(request, 'index.html', context)

def productos_por_categoria(request, categoria_id):
    obj_categoria = Categoria.objects.get(id=categoria_id)
    lista_productos = obj_categoria.producto_set.all()
    lista_categorias = Categoria.objects.all()
    lista_marcas = Marca.objects.all()

    context = {
        'productos': lista_productos,
        'categorias': lista_categorias,
        'marcas': lista_marcas
    }
    
    return render(request, 'index.html', context)

def productos_por_marca(request, marca_id):
    obj_marca = Marca.objects.get(id=marca_id)
    lista_productos = obj_marca.producto_set.all()
    lista_categorias = Categoria.objects.all()
    lista_marcas = Marca.objects.all()

    context = {
        'productos': lista_productos,
        'categorias': lista_categorias,
        'marcas': lista_marcas
    }
    
    return render(request, 'index.html', context)

def productos_por_nombre(request):
    nombre = request.POST['nombre']
    lista_productos = Producto.objects.filter(nombre__icontains=nombre)
    lista_categorias = Categoria.objects.all()
    lista_marcas = Marca.objects.all()

    context = {
        'productos': lista_productos,
        'categorias': lista_categorias,
        'marcas': lista_marcas
    }
    
    return render(request, 'index.html', context)

def producto_detalle(request, producto_id):
    obj_producto = Producto.objects.get(id=producto_id)

    context = {
        'producto': obj_producto
    }
    return render(request, 'producto.html', context)

"""
-------- CARRITO DE COMPRAS -----------------------
"""
from .cart import Cart

def carrito(request):
    return render(request,'carrito.html')

def agregar_carrito(request, producto_id):
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
    else:
        cantidad = 1

    obj_producto = Producto.objects.get(pk=producto_id)

    carrito_producto = Cart(request)
    carrito_producto.add(obj_producto, cantidad)
    #print(request.session.get('cart'))
    return render(request, 'carrito.html')

def eliminar_producto_carrito(request, producto_id):
    carrito_producto = Cart(request)
    carrito_producto.delete(producto_id)

    return render(request, 'carrito.html')

def limpiar_carrito(request):
    carrito_producto = Cart(request)
    carrito_producto.clear()

    return render(request, 'carrito.html')


"""
-------- USUARIOS Y CLIENTES -----------------------
"""
from django.contrib.auth.models import User
from django.contrib.auth import login

def crear_usuario(request):
    if request.method == 'POST':
        data_usuario = request.POST['usuario']
        data_password = request.POST['password']
        nuevo_usuario = User.objects.create_user(username=data_usuario, password=data_password)
        if nuevo_usuario is not None:
            login(request,nuevo_usuario)
            return redirect('/cuenta')

        
    return render(request,'login.html')
        
def cuenta_usuario(request):
    return render(request,'cuenta.html')