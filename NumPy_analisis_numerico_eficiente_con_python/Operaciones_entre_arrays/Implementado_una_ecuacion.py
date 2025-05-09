import numpy as np
import matplotlib.pyplot as plt

# Generar una secuencia de valores de x de -1 a 1 con un espaciado de 0.0001
# np.arange() es una función de NumPy que crea un array de números espaciados uniformemente dentro de un intervalo dado.
# -1 es el valor inicial del intervalo (inclusive).
# 1 es el valor final del intervalo (exclusive).
# 0.0001 es el espaciado entre cada valor en la secuencia. Cuanto menor sea el espaciado, más "suave" se verá la curva.
x = np.arange(-1, 1, 0.0001)

# Implementación de la fórmula para la parte superior de un círculo
# La ecuación de un círculo centrado en el origen (0, 0) con radio 1 es x^2 + y^2 = 1.
# Despejando 'y', obtenemos y^2 = 1 - x^2, y tomando la raíz cuadrada, obtenemos dos soluciones:
# y = +sqrt(1 - x^2) para la parte superior del círculo.
# Aquí, np.sqrt() es la función de NumPy para calcular la raíz cuadrada elemento por elemento del array (1 - x**2).
# x**2 calcula el cuadrado de cada elemento en el array 'x'.
y1 = np.sqrt(1 - x**2)

# Implementación de la fórmula para la parte inferior de un círculo
# Similar a la parte superior, pero con el signo negativo para obtener la parte inferior del círculo:
# y = -sqrt(1 - x^2).
y2 = -np.sqrt(1 - x**2)

# Graficar el gráfico con las dos partes del círculo
# plt.plot() es una función de Matplotlib para dibujar puntos o líneas en un gráfico.
# El primer argumento ('x') son los valores para el eje horizontal.
# El segundo argumento ('y1') son los valores para el eje vertical de la primera parte del círculo.
# El tercer argumento ('r') es una cadena de formato que especifica el color de la línea (en este caso, 'r' significa rojo).
plt.plot(x, y1, 'r')

# Se dibuja la segunda parte del círculo utilizando los mismos valores de 'x' pero diferentes valores de 'y' ('y2').
# También se utiliza el color rojo ('r') para esta parte.
plt.plot(x, y2, 'r' )

# Agregar el título del gráfico y las etiquetas de los ejes x e y
# plt.title() establece el título que aparecerá en la parte superior del gráfico.
plt.title("Círculo")

# plt.xlabel() establece la etiqueta que aparecerá en el eje horizontal (eje x).
plt.xlabel("Eje x")

# plt.ylabel() establece la etiqueta que aparecerá en el eje vertical (eje y).
plt.ylabel("Eje y")

# Mostrar el gráfico
# plt.show() es una función que muestra la figura o figuras creadas con Matplotlib.
# Sin esta línea, el gráfico no se mostrará al ejecutar el código.
plt.show()