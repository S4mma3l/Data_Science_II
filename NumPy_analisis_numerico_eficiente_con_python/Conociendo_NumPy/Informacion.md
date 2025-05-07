## Temas que abordaremos
NumPy


## Presentacion del problema

-Precio de manzanas en 5 cuidades rusas durante un periodo de 7 anos y 3 meses.
-Basados en un dataset de: https://www.kaggle.com/datasets/kapatsa/apple-prices-in-russian-regions

## Herramienta utilizada:

-NumPy

-trabaja con una estructura llamada *array*.
Es un objeto que almacena un conjunto de datos hoogeneos(todos del mismo tipo y relacionados).
son espacios fijos, las operaciones matematicas son mucho mas rapida, menor uso de memorias, diversos metodos para su utilizacion.

## Secuencia de valores

En Ciencia de Datos, existen varias situaciones en las que necesitamos evaluar datos relacionados con eventos periódicos que ocurren en una fecha fija o predeterminada, ya que estos pueden tener alguna influencia en el fenómeno que queremos analizar. Un ejemplo de un evento que afecta a muchas personas de diversos países es la Copa del Mundo, organizada por la Federación Internacional de Fútbol (FIFA).

Dado el ejemplo de un evento periódico anterior, crea un array utilizando la función np.arange() que liste todos los años en los que ocurrió o se prevé que ocurra la Copa del Mundo, considerando el intervalo cerrado desde el año 2000 hasta el 2102.

Tip: La primera Copa del Mundo ocurrió en el año 2002.

*python*
*import numpy as np*

*ano_inicial = 2002*
*ano_final = 2102*
*np.arange(ano_inicial, ano_final + 1, 4)*

Este algoritmo muestra todos los años en el intervalo cerrado de 2000 a 2102 en los que ocurre la Copa del Mundo.

link dataset: [gist.github.com/ahcamachod/41b8a65c5e5b58125401deafb68af460](https://gist.github.com/ahcamachod/41b8a65c5e5b58125401deafb68af460)

## Para saber mas

Las listas en Python son estructuras de datos básicas que pueden contener elementos de diferentes tipos (enteros, cadenas, otras listas, etc.). Por otro lado, Numpy (Numerical Python) es una biblioteca de Python que proporciona soporte para matrices multidimensionales, estructuras de datos más avanzadas y eficientes para cálculos numéricos.

Aquí tienes un ejemplo de cómo convertir una lista en un array Numpy:

import numpy as np

# crea una lista
lista = [1, 2, 3, 4, 5]

# convierte la lista en un array Numpy
array = np.array(lista)

print("Lista: ", lista)
print("Array: ", array)

Salida:

Lista: [1, 2, 3, 4, 5]

Array: [1 2 3 4 5]

Existen varias ventajas en el uso de arrays Numpy en lugar de listas regulares de Python y aquí tienes algunas de ellas:

1. Eficiencia de procesamiento: Las operaciones matemáticas en los arrays Numpy son mucho más rápidas que en las listas regulares, ya que Numpy está optimizado para trabajar con conjuntos de datos homogéneos y libera memoria de la computadora de manera rápida.

2. Facilidad de uso: Las operaciones matemáticas en los arrays Numpy se expresan de manera mucho más clara y concisa que en las listas regulares, lo que hace que el código sea más fácil de leer y mantener.

3. Integración con otras bibliotecas: Numpy es una de las bibliotecas más utilizadas en ciencia de datos y aprendizaje automático. Muchas otras bibliotecas, como Pandas y Matplotlib, están diseñadas para trabajar directamente con arrays Numpy.

Comparación de rendimiento: listas vs arrays

Centrándonos en la eficiencia, podemos comparar el tiempo necesario para realizar un cálculo utilizando listas y arrays.

import numpy as np
import time

# crea una lista con 1000000 elementos
lista = list(range(1000000))

# convierte la lista en un array Numpy
array = np.array(lista)

# comienza a medir el tiempo para la operación con la lista
start_time = time.time()

# realiza la operación de elevar al cuadrado cada elemento de la lista
lista_cuadrado = [i**2 for i in lista]

# detiene el cronómetro
tiempo_lista = time.time() - start_time

# comienza a medir el tiempo para la operación con el array
start_time = time.time()

# realiza la operación de elevar al cuadrado cada elemento del array
array_cuadrado = array**2

# detiene el cronómetro
tiempo_array = time.time() - start_time

print("Tiempo de la operación con la lista: ", tiempo_lista)
print("Tiempo de la operación con el array: ", tiempo_array)

Salida:

Tiempo de la operación con la lista: 0.2745847702026367

Tiempo de la operación con el array: 0.004081010818481445

Como se puede ver, la operación realizada con el array Numpy fue mucho más rápida que con la lista regular, lo que demuestra la eficiencia en el procesamiento con el array.


## Obteniedo las dimensiones

Un colega te pidió que cargues una base de datos y verifiques el número de filas y columnas del archivo cargado. Tenía dudas sobre si se habían cargado todas las filas.

¿Cómo determinar las dimensiones correctas de una matriz?

Para responder a esta pregunta, necesitarás acceder al siguiente dataset. Puedes usar la opción skiprows=1 para omitir la primera línea del archivo.

repuesta en archivo: [NumPy_analisis_numerico_eficiente_con_python\Conociendo_NumPy\obteniendo_las_dimensiones.py](obteniendo_las_dimensiones.py)


## Lo que aprendimos en esta aula:

    Crear arrays con secuencias numéricas.
    Cargar archivos.
    Verificar las dimensiones de un array.
    Realizar la transposición de un array.

