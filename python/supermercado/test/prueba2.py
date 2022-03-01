import random
from prueba1 import *

def datos():
    for i in range(10):
        precio  = random.uniform(-100,100)
        unidades = random.randint(-10,10)
        unidad(unidades, precio)
datos()