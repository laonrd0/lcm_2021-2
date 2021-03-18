#! -*- coding: utf-8 -*-

'''
Script que determina si un número entero dado por el usuario es negativo o positivo
Leonardo
11/03/2021
'''
numero = int(input("Ingresa un número entero: "))

if numero > 0 :
    print(numero, " Es un número positivo")
elif numero == 0:
    print("El número es cero")
elif numero < 0:
    print(numero, " Es un número negativo")



