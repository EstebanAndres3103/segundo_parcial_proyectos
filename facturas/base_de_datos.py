from facturas.models import *


def cliente_factura(nit, nombre, telefono):
    global cliente
    global factura
    cliente=Cliente(nit=nit, nombre=nombre, telefono=telefono)
    cliente.save()

    factura=Factura(cliente=cliente)
    factura.save()

def detalle_de_factura(tipo,sabor,tam,precio_tam,top,precio_top,cantidad):
    helado=Helado(tipo=tipo,sabor=sabor,tam=tam,precio=precio_tam)
    helado.save()

    topping=Topping(nombre=top,precio=precio_top)
    topping.save()

    detalle=DetalleFactura(cantidad=cantidad,factura=factura,helado=helado, topping=topping)
    detalle.save()

def valor_de_factura(total):
    valor=ValorFactura(factura=factura,total=total)
    valor.save()