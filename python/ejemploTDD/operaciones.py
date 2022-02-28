'''
Construir un programa que realice las operaciones básicas de suma,
resta, multiplicación, división, potencia con 2 números reales y raíz cuadrada

'''
def suma(n1,n2):
    return n1+n2

def resta(n1,n2):
    return n1-n2

def multiplica(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2==0:
        return("División entre cero")
    else:
        return n1/n2

def potencia(n1,n2):
    try:
        return n1 ** n2
    except:
        resultadoCorrecto="Fuera de rango"

def raiz(numero):
    return (numero **(0.5)) if numero >0 else "No hay raiz cuadrada para numeros negativos"