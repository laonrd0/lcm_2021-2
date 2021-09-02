# Apuntes de Python

[TOC]

## Introducción

Python es un lenguaje de programación interpretado de uso generalizado, se considera fácil de leer y aprender por su código limpio y por escribirse de forma muy parecida al lenguaje natural.

## Estructuras de control

Una estructura de control, es un bloque de código que permite agrupar instrucciones de manera controlada. 

Para conocer las estructuras de control es necesario entender la __indentación_. La _indentación_ es un anglicismo que hace referencia a la sangría utilizada en algunos lenguajes de programación . Así como para el lenguaje  formal, cuando uno redacta una carta, debe respetar ciertas sangrías,  python requieren una _indentación_ para conformar bloques de código, por lo que forma parte de la sintaxis de este lenguaje.



### If, elif, else

### Ciclos while

### Ciclos for

Los ciclos `for` permiten ejecutar una o varias instrucciones de forma **iterativa**, recorriendo elementos de una colección. Las colecciones pueden ser de varios tipos _(listas, sets, diccionarios)_, el `for` puede recibir una colección predefinida o directamente de la salida de una función.

#### sintaxis básica

```python
for <variable_iterante> in <coleccion>: 
    instrucción_1
    instrucción_2
    ...
    instrucción_n

```

#### Diferencias for y while



![](https://raw.githUbusercontent.com/laonrd0/picgo/main/img2ixTr7min.jpeg)



# Introducción a Numpy para realizar operaciones con vectores y matrices

Numpy es un paquete fundamental para realizar cómputo científico con python de manera ágil. Con Numpy se puede trabajar con :
* Objetos array de N-dimensiones.
* Funciones de expansión (_broadcasting_) con matríces y vectores.
* Algebra lineal, Transformada de Fourier y números aleatorios.
* Este paquete posee herramientas de integración con C y fortran 

Para mas información sobre Numpy puedes consultar el [Guía rápida ](https://numpy.org/doc/stable/user/quickstart.html)] o la [Documentación Completa](https://numpy.org/doc/stable/index.html).


#### Utilizar numpy
Es altamente aconsejable importar numpy utilizando un alias:
```python
import numpy as np
```



## Introducción a matplotlib

Matplotlib es una biblioteca para graficas en 2D capaz de producir imagenes en una gran variedad de formatos y con la calidad y resolución requerida para cualquier tipo de publicación. 
Para conocer más sobre matplotlib, sus func iones y tipos de gráficos puedes consultar la [documentación oficial](https://matplotlib.org/).

### Importar matplotlib
Para hacer uso de la librería es necesario realizar la importación correspondiente en el entorno.


```python
#Importamos la biblioteca con alias para facilitar su manejo en el código
import matplotlib.pyplot as plt
```

### Opciones para trabajar con matplotlib

La biblioteca matplotlib permite generar varios tipos de gráficos, uno de ellos son las graficas de puntos y líneas ó plots, este tipo de gráfica se genera utilizando la función plot().

la función plot recibe un conjunto de valores para ser graficados.
plt.plot([1,2,3,4,5])

La función show() es la encargada de mostrar el grafico que se generó con la función anterior.
plt.show()

La función show() despliega la figura producida previamente. La función draw() permite redibujar una figura en modo interactivo, cuando cambias los datos o formato de una gráfica permite modificar directamente la figura.

### Modo interactivo

El modo interactivo me permite actualizar un gráfico en tiempo real y de forma dinámica sin necesidad de utilizar la función show().

plt.ion()                                           #activar modo interactivo
plt.ioff()                                          #desactivar modo interactivo

plt.isinteractive()                                 #Me permite saber esta activo el modo interactivo