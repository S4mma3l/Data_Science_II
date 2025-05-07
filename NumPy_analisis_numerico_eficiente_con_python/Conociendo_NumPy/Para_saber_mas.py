import numpy as np

# crea una lista
lista = [1, 2, 3, 4, 5]

# convierte la lista en un array Numpy
array = np.array(lista)

print("Lista: ", lista)
print("Array: ", array)
print("Tipo de dato de la lista: ", type(lista))
print("Tipo de dato del array: ", type(array))

print("\n segundo ejemplo \n")


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
print("Diferencia de tiempo: ", tiempo_lista - tiempo_array)
# El tiempo de la operación con el array es significativamente menor que el de la lista