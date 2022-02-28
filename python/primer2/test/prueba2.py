import random
from prueba1 import *
def numero():
    horasA = 0
    minutosA = 0
    for i in range(6):
        horasA  = random.randint(0, 24)
        minutosA = random.randint(0, 60)
        hora =  str(horasA)  + ":" + str(minutosA)
        print(len(hora))
        print(hora)
        validacion(hora)
numero()