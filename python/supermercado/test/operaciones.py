
import re
def docena(numero, valor):
    docenas = numero * 12
    pagar(docenas, valor)
def pagar (numero, valor):
    monto = numero * valor
    descuento(monto)
    if numero > 36:
        unidadesExtra(numero)
def descuento(numero):
    descuento = 0
    if numero > 36:
        descuento = numero * 0.15
    else:
        descuento = numero * 0.1
    print("Monto de descuento es $" , descuento)
    resta(descuento, numero)
def resta(descuento, numero):
    resta = numero - descuento
    print("El valor a pagar es $" , resta )
def unidadesExtra(numero):
    unidadesEx = numero - 36
    unidadesEx = unidadesEx / 4
    print("Unidades Extras "  , unidadesEx)