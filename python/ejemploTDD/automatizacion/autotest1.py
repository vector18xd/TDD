#Programa para ejecutar N test al programa: operaciones
#Se importa esta libreria para trabajar con rutas de carpetas
import sys
sys.path.append("../test")

#Se importa el programa test

from test1 import *

for i in range(10):
    print("Prueba:",str(i+1))
    prueba()
    print("-"*50)
    