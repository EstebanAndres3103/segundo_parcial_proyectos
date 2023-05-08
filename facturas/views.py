from django.shortcuts import render, HttpResponse
from facturas.funcionsubtotal import *
from facturas.models import *
from facturas.base_de_datos import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
acumulado=0


def inicio(request):
    return render(request,'inicio.html')

def compras(request):
    global nit
    global nombre
    global telefono

    nit=request.POST.get('nit')
    nombre=request.POST.get('nombre')
    telefono=request.POST.get('telefono')

    cliente_factura(nit,nombre,telefono)

    return render(request, 'basecompras.html')

def cremoso(request):
    global acumulado 


    sumar=request.POST.get('sumar')
    tamano=request.POST.get('tamano')
    sabor=request.POST.get('sabor')
    topping=request.POST.get('topping')
    estadoCompra=request.POST.get('pagar')
    tipo='helado_cremoso'
    precio_tam=precioTamano(tamano)
    precio_top=precioTopping(topping)

    if request.method == 'POST':
        if sumar=='sumar':
            preciounitario=calcularsubtotal(tamano,topping)
            acumulado+=preciounitario
            
            try:
                detalle_de_factura(tipo,sabor,tamano,precio_tam,topping,precio_top,preciounitario)
            except:
                messages.warning(request, 'Por favor llena todos los campos.')

        elif estadoCompra=='pagar':
            valor_de_factura(acumulado)
            acumulado=0

            
        
    print(acumulado)

    return render(request,'seleccioncremoso.html', {
        'acumulado': acumulado
    })

def hielo(request):

    global acumulado 

    sumar=request.POST.get('sumar')
    tamano=request.POST.get('tamano')
    sabor=request.POST.get('sabor')
    topping=request.POST.get('topping')
    estadoCompra=request.POST.get('pagar')
    cancelar=request.POST.get('cancelar')
    tipo='helado_de_hielo'
    precio_tam=precioTamano(tamano)
    precio_top=precioTopping(topping)

    if request.method == 'POST':
        if sumar=='sumar':
            preciounitario=calcularsubtotal(tamano,topping)
            acumulado+=preciounitario
            detalle_de_factura(tipo,sabor,tamano,precio_tam,topping,precio_top,preciounitario)

        elif estadoCompra=='pagar':
            acumulado=0
            valor_de_factura(acumulado)

        elif cancelar=='cancelar':
            acumulado=0
            
        
    print(acumulado)


    return render(request, 'seleccionhielo.html',{

        'acumulado': acumulado
    })

def registro(request):

    return render(request,'registro.html')


def comprarealizada(request):
    return render(request,'exito.html')


def ver_tablas(request):
    facturas=Factura.objects.all()
    clientes=Cliente.objects.all()
    valor=ValorFactura.objects.all()

    return render(request, 'ver_tablas.html',{
        'facturas':facturas,
        'clientes':clientes,
        'valor':valor
    })


@login_required

def tablas(request):
    return render(request,'tablas.html')