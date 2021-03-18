# -*- coding: utf-8 -*-

"""
Script para ejercicios con funciones en python
"""

def es_par(numero):
    if numero == 0:
        return True
    else:
        if numero % 2 == 0:
            return True
        else:
            return False
        

numero = int(input("Ingresa un valor entero: "))
if es_par(numero):
    print("El numero es par")
else:
    print("El número es impar")