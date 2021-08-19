def es_entero(n):
    if n > 0:
        return True
    else:
        return False



numero = int(input("Ingresa un número: "))
suma = 0

while es_entero(numero):
    suma = suma + numero
    numero = int(input("ingresa un número: "))

print("La suma de los números enteros ingresado es: ", suma)
