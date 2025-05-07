import numpy as np

url = "https://gist.githubusercontent.com/ahcamachod/41b8a65c5e5b58125401deafb68af460/raw/8f328f1777a4d628015f827240457a1f8078ab02/manzanas.csv" # Datos desde la URL

np.loadtxt(url, delimiter=",", usecols=(np.arange(1, 88, 1)))
# 12 * 7 + 3 = 87
np.arange(1, 88, 1)

print(np.loadtxt(url, delimiter=',', usecols=(np.arange(1, 88, 1)))) # Carga los datos del archivo CSV y los imprime

path= 'NumPy_analisis_numerico_eficiente_con_python\Conociendo_NumPy\manzanas.csv' # dato de la ruta del archivo CSV

print(np.loadtxt(path, delimiter=',', usecols=(np.arange(1, 88, 1)))) # Carga los datos del archivo CSV y los imprime

datos= np.loadtxt(path, delimiter=',', usecols=(np.arange(1, 88, 1))) # Carga los datos del archivo CSV y los almacena en la variable 'datos'
print(datos) # Imprime los datos cargados

datos.ndim # Muestra la cantidad de dimensiones del array 'datos'
print(datos.ndim) # Imprime la cantidad de dimensiones del array 'datos'
datos.shape # Muestra la forma del array 'datos' (número de filas y columnas)
print(datos.shape) # Imprime la forma del array 'datos' (número de filas y columnas)

datos.T # Transpone el array 'datos' (intercambia filas por columnas)
print(datos.T) # Imprime el array 'datos' transpuesto (intercambia filas por columnas)

datos_transpuestos= datos.T # Almacena el array 'datos' transpuesto en la variable 'datos_transpuestos'
print(datos_transpuestos) # Imprime el array 'datos_transpuestos' (intercambia filas por columnas)