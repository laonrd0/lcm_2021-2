#! -*- coding: utf-8 -*-

# Script que dertermina si un número entero dado por el usuario
# es par o impar

numero = int(input("Ingrese un número entero positivo: "))

if numero > 0 :
    if numero % 2 == 0:
        print(numero, ' Es par')
    else:
        print(numero, ' Es impar')
else:
    print("El numero es igual a cero o es un número negativo")