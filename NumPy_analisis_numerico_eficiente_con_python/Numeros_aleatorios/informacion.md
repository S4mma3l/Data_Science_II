# Los mismos valores

Micaela quería generar dos secuencias de números aleatorios diferentes entre 0 y 5 en su código. Supongamos que ella escribió lo siguiente:

import numpy as np

np.random.seed(42)
a = np.random.uniform(0, 1, 5)
np.random.seed(42)
b = np.random.uniform(0, 1, 5)

¿Qué problemas está experimentando con este código? respuesta: [](los_mismos_valores.py)

La secuencia de código generará 5 números entre 0 y 1. Además, seed(42) hará que ambas secuencias sean iguales.

La elección del primer valor dentro de random.uniform es el primer valor posible en la secuencia, el segundo valor es el último valor posible y el último valor es el número de valores en la secuencia. Además, colocar random.seed con el mismo número justo antes de la llamada a la función hará que se genere la misma secuencia. Un ejemplo de código que resolvería el problema correctamente es este, observe que se generarán secuencias de 5 números:

import numpy as np

np.random.seed(42)
a = np.random.uniform(0, 5, 5)
np.random.seed(8)
b = np.random.uniform(0, 5, 5)

# Aplicando a numpy

Has comenzado tus estudios con la biblioteca Numpy y decidiste usarla para reemplazar un cálculo que se realizaba con listas de Python. La lista que tienes en tus manos es la siguiente:

x = [0,1,2,3,4,5,6,7,8,9,10]

Esta lista se estaba utilizando para calcular varios valores de "y" en la ecuación y = x + 3 / 2. ¿Cómo se vería el código en Numpy para reemplazar el siguiente fragmento de código?

x = [0,1,2,3,4,5,6,7,8,9,10]
y = []

for i in x:
  y.append(i + 3 / 2)

Tip: Ejecuta el código anterior antes y verifique los valores en las variables x e y con la función print() para comparar los resultados del array.

respuesta : [](aplica_a_numpy.py)

# Lo que aprendimos en esta aula:

    Generar secuencias de números aleatorios.
    Garantizar la reproducibilidad de resultados.
    Agrupar arrays.
    Guardar archivos.

