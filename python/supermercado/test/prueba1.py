from operaciones import *
def unidad(unidades, valor):
    if unidades > 0:
        if valor > 0:
            pagar(unidades,valor)
        else:
            print("El valor no puede ser negativo")
    else:
        print("Las unidades no puede ser negativa")
def docena(docenas, valor):
    if docenas > 0:
        if docenas > 0:
            docena(docenas, valor)
        else:
            print("El valor no puede ser negativo")
    else:
        print("Las unidades no puede ser negativa")
