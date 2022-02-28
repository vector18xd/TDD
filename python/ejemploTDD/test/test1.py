#Programa para probar todo el programa: operaciones
#Se importa esta libreria para trabajar con rutas de carpetas
import sys
sys.path.append("..")
from math import sqrt

#Se importa el programa a realizar el test
from operaciones import *
#Importar librerias para usar numeros aleatorios
import random

def prueba():
    #uniform: genera numeros reales entre un rango dado
    numero=random.uniform(-1000,2000)
    numero2=random.uniform(-1000,2000)
#Prueba para sumas
    print("Prueba para sumas")
    llega=suma(numero,numero2)
    resultadoCorrecto=numero+numero2
#Se evalua si lo que llego es lo mismo a lo que se calculo y deben ser iguales
    if llega==resultadoCorrecto:
        print("Nros generados:",numero,"|",numero2,"y el resultado es:",resultadoCorrecto)
    else:
        print("ERROR Nros generados:",numero,"|",numero2,"y el resultado es:",llega,"se esperaba:",resultadoCorrecto)

#Prueba para RESTAS
    print("\nPrueba para Restas")
    llega=resta(numero,numero2)
    resultadoCorrecto=numero-numero2
#Se evalua si lo que llego es lo mismo a lo que se calculo y deben ser iguales
    if llega==resultadoCorrecto:
        print("Nros generados:",numero,"|",numero2,"y el resultado es:",resultadoCorrecto)
    else:
        print("ERROR Nros generados:",numero,"|",numero2,"y el resultado es:",llega,"se esperaba:",resultadoCorrecto)

#Prueba para MULTIPLICACION
    print("\nPrueba para Multiplicar")
    llega=multiplica(numero,numero2)
    resultadoCorrecto=numero*numero2
#Se evalua si lo que llego es lo mismo a lo que se calculo y deben ser iguales
    if llega==resultadoCorrecto:
        print("Nros generados:",numero,"|",numero2,"y el resultado es:",resultadoCorrecto)
    else:
        print("ERROR Nros generados:",numero,"|",numero2,"y el resultado es:",llega,"se esperaba:",resultadoCorrecto)

#Prueba para dividir
    print("\nPrueba para Divisiones")
    llega=divide(numero,numero2)
    if numero2==0:
        resultadoCorrecto="División entre cero"
    else:
        resultadoCorrecto=numero/numero2
#Se evalua si lo que llego es lo mismo a lo que se calculo y deben ser iguales
    if llega==resultadoCorrecto:
        print("Nros generados:",numero,"|",numero2,"y el resultado es:",resultadoCorrecto)
    else:
        print("ERROR Nros generados:",numero,"|",numero2,"y el resultado es:",llega,"se esperaba:",resultadoCorrecto)

#Prueba para POTENCIAS
    print("\nPrueba para Potencias x^y")
    llega=potencia(numero,numero2)
    try:
        resultadoCorrecto=pow(numero,numero2)
    except:
        resultadoCorrecto="Fuera de rango"

#Se evalua si lo que llego es lo mismo a lo que se calculo y deben ser iguales
    if llega==resultadoCorrecto:
        print("Nros generados:",numero,"|",numero2,"y el resultado es:",resultadoCorrecto)
    else:
        print("ERROR Nros generados:",numero,"|",numero2,"y el resultado es:",llega,"se esperaba:",resultadoCorrecto)


#Prueba para RAICES
    print("\nPrueba de raices")    
#se guarda el valor que llega del programa que se esta probando    
    llega=raiz (numero)

#Se realizan los calculos que debe regresar el programa
    try:
        resultadoCorrecto=sqrt(numero)
    except:
        resultadoCorrecto="No hay raiz cuadrada para numeros negativos"

#Se evalua si lo que llego es lo mismo a lo que se calculo y deben ser iguales
    if llega==resultadoCorrecto:
        print("Nro generado:",numero,"y el resultado es:",resultadoCorrecto)
    else:
        print("ERROR Nro generado:",numero,"y el resultado es:",llega,"se esperaba:",resultadoCorrecto)
