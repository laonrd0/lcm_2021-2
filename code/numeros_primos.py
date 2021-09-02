# -*- coding: utf-8 -*

def es_primo(n):
    if n >= 1:
        primo = True
        for i in range(2, n):
            if n % i == 0:
                primo = False
                break
    else:
        primo = False
    return primo


num1  = int(input("Escribe un numero entero: " ))
if es_primo(num1):
    print("Es primo")
else:
    print("No es primo")