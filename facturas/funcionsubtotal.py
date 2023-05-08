def precioTamano(heladoTamano):
        
    if heladoTamano=='pequeno':
        valorTamano=15
    elif heladoTamano=='mediano':
        valorTamano=20
    elif heladoTamano=='grande':
        valorTamano=24
    else:
        valorTamano=0
    return valorTamano

def precioTopping(toppingHelado):

    if toppingHelado=='chispas':
        valorTopping=5
    elif toppingHelado=='anicillos':
        valorTopping=3
    elif toppingHelado=='crema':
        valorTopping=7
    elif toppingHelado=='chocolate':
        valorTopping=5
    else:
        valorTopping=0
    
    return valorTopping  

def valorDetalle(tamano,topping):
    costoXtamano=precioTamano(tamano)
    costoXtopping=precioTopping(topping)

    return costoXtamano+costoXtopping

def calcularsubtotal(tamano,topping):

    subtotal=valorDetalle(tamano,topping)
    print(subtotal)
    return subtotal


