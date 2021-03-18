def es_par(numero):
    #considera como verdadero caundo se recibe un valor 0
    if numero == 0:
        return True
    else:
        if numero % 2 == 0:
            return True
        else:
            return False

#Esta funcion imprime un saludo
def print_header(cadena_texto):
    print("Hola ", cadena_texto)