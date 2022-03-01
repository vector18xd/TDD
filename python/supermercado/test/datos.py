from prueba1 import *
def menu():
    print("Bienvenido a supermercado mondongo desea comprar este producto en")
    print("0|Unidades")
    print("1|Docenas")
    id = int(input("Digite el id(0,1): "))
    valor = float(input("Digite el valor del producto: "))
    if id == 0:
        unidades = int(input("Digite las unidades que desea: "))
        unidad(unidades, valor)
    elif id == 1:
        docenas = int(input("Digite las decenas que desea: "))
        docena(docenas, valor)
    else:
        print("No existe este id")
menu()