def negativoPositivo (numero):
    if numero > 0:
        print("Es postivo")
    else:
        print("ES negativo")
    pares(numero)
def pares(numero):
    if numero % 2 == 0:
        print("Pares")
    else:
        print("No par")