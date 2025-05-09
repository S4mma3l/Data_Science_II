import numpy as np
import matplotlib.pyplot as plt

# --- 1. Carga de Datos ---
# Define la ruta del archivo CSV que contiene los datos de las manzanas.
ruta_archivo = 'NumPy_analisis_numerico_eficiente_con_python\Conociendo_NumPy\manzanas.csv'

# Carga los datos numéricos del archivo CSV.
# - 'delimiter=',' indica que los valores en el archivo están separados por comas.
# - 'usecols=(np.arange(1, 88))' selecciona las columnas desde la segunda (índice 1) hasta la columna 88 (índice 87),
#   excluyendo potencialmente una columna de índice inicial (como nombres de columna).
datos = np.loadtxt(ruta_archivo, delimiter=',', usecols=(np.arange(1, 88, 1)))

# --- 2. Exploración Inicial de los Datos ---
# Muestra el número de dimensiones del array 'datos'. Para datos tabulares, generalmente será 2 (filas y columnas).
num_dimensiones = datos.ndim
print(f"Número de dimensiones del array 'datos': {num_dimensiones}")

# Muestra la forma (shape) del array 'datos', que indica el número de filas y columnas (filas, columnas).
forma_datos = datos.shape
print(f"Forma del array 'datos' (filas, columnas): {forma_datos}")

# --- 3. Transposición de los Datos ---
# Transpone el array 'datos', intercambiando sus filas por columnas. Esto es útil para acceder a los datos de manera diferente.
datos_transpuestos = datos.T
print("\nArray 'datos' transpuesto (primeras 5 filas y columnas):")
print(datos_transpuestos[:5, :5]) # Imprime las primeras 5 filas y columnas para una vista previa

# --- 4. Extracción de Fechas y Precios ---
# Asumiendo que la primera columna del array transpuesto ('datos_transpuestos') contiene las fechas
# y las columnas restantes contienen los precios.
fechas = datos_transpuestos[:, 0]
print(f"\nPrimeras 5 fechas: {fechas[:5]}")

precios = datos_transpuestos[:, 1:]
print(precios)

fechas = np.arange(1, 88, 1) # Asigna un rango de fechas desde 1 hasta 87 (suponiendo que son días o meses)
print(f"\nRango de fechas (1 a 87): {fechas}")

# plt.plot(fechas, precios[:,0])  # Grafica los precios en función de las fechas
# plt.show()  # Muestra la gráfica

moscu = precios[:,0]  # Asigna los precios de Moscú a la variable 'moscu'
kaliningrado = precios[:,1]  # Asigna los precios de Kaliningrado a la variable 'kaliningrado'
petersburgo = precios[:,2]  # Asigna los precios de Petersburgo a la variable 'petersburgo'
krasnodar = precios[:,3]  # Asigna los precios de Krasnodar a la variable 'krasnodar'
ekaterinburgo = precios[:,4]  # Asigna los precios de Ekaterinburgo a la variable 'ekaterinburgo'
'''
plt.plot(fechas, moscu, label='Moscú')  # Grafica los precios de Moscú
plt.plot(fechas, kaliningrado, label='Kaliningrado')  # Grafica los precios de Kaliningrado     
plt.plot(fechas, petersburgo, label='Petersburgo')  # Grafica los precios de Petersburgo
plt.plot(fechas, krasnodar, label='Krasnodar')  # Grafica los precios de Krasnodar
plt.plot(fechas, ekaterinburgo, label='Ekaterinburgo')  # Grafica los precios de Ekaterinburgo
plt.title('Precios de manzanas en diferentes ciudades')  # Título de la gráfica
plt.legend(['Moscú', 'Kaliningrado', 'Petersburgo', 'Krasnodar', 'Ekaterinburgo'])  # Muestra la leyenda con las etiquetas de cada línea
plt.show()  # Muestra la gráfica con todas las líneas
'''

moscu.shape  # Muestra la forma del array 'moscu', que debería ser unidimensional (número de días)
print(moscu.shape)  # Imprime la forma del array 'moscu'
moscu_1= moscu[0:12]  # Selecciona los primeros 12 elementos del array 'moscu'
moscu_2= moscu[12:24]
moscu_3= moscu[24:36]
moscu_4= moscu[36:48]
'''
plt.plot(np.arange(1, 13, 1), moscu_1, label='Moscú 1')  # Grafica los primeros 12 precios
plt.plot(np.arange(1, 13, 1), moscu_2, label='Moscú 2')  # Grafica los siguientes 12 precios
plt.plot(np.arange(1, 13, 1), moscu_3, label='Moscú 3')  # Grafica los siguientes 12 precios
plt.plot(np.arange(1, 13, 1), moscu_4, label='Moscú 4')  # Grafica los siguientes 12 precios
plt.title('Precios de manzanas en Moscú')  # Título de la gráfica
plt.legend(['2013', '2014', '2015', '2016'])  # Muestra la leyenda con las etiquetas de cada línea
plt.show()  # Muestra la gráfica con todas las líneas
'''

np.array_equal(moscu_1, moscu_2)  # Compara si los arrays 'moscu_1' y 'moscu_2' son iguales
print(np.array_equal(moscu_1, moscu_2))  # Imprime el resultado de la comparación (True o False)

np.allclose(moscu_1, moscu_2, 5)  # Compara si los arrays 'moscu_1' y 'moscu_2' son cercanos dentro de una tolerancia
print(np.allclose(moscu_1, moscu_2, 5))  # Imprime el resultado de la comparación (True o False)

np.mean(moscu_1)  # Calcula la media de los precios en 'moscu_1'
print(np.mean(moscu_1))  # Imprime la media de los precios en 'moscu_1' (Promedio)

np.mean(kaliningrado)  # Calcula la media de los precios en 'kaliningrado'
print(np.mean(kaliningrado))  # Imprime la media de los precios en 'kaliningrado' (Promedio)

print(kaliningrado)

np.isnan(kaliningrado)  # Verifica si hay valores NaN en el array 'kaliningrado'
print(np.isnan(kaliningrado))  # Imprime un array booleano indicando la presencia de NaN en 'kaliningrado'

np.sum(np.isnan(kaliningrado))  # Suma el número de valores NaN en 'kaliningrado'
print(np.sum(np.isnan(kaliningrado)))  # Imprime el número total de valores NaN en 'kaliningrado'

kaliningrado[4] = (kaliningrado[3] + kaliningrado[5])/2  # Suma los valores en las posiciones 3 y 4 de 'kaliningrado'
print(np.sum(np.isnan(kaliningrado))) 

print(np.mean(kaliningrado))  # Imprime la media de los precios en 'kaliningrado' después de la imputación

# plt.plot(fechas, moscu, label='Moscú') # Grafica los precios de Moscú
# plt.show() # Muestra la gráfica de precios de Moscú

# definicion de recta
# y = ax + b

x = fechas
y = 0.5 * x + 78  # Definición de la recta con pendiente 1.5 y ordenada al origen 2

print(y)

# plt.plot(fechas, moscu, label='Moscú')  # Grafica los precios de Moscú
# plt.plot(x, y, label='Recta')  # Grafica la recta
# plt.show()  # Muestra la gráfica

valores_recta = np.sqrt(np.sum(np.power(moscu - y, 2))) # Calcula la diferencia entre los precios de Moscú y los valores de la recta
print(valores_recta)  # Imprime la diferencia entre los precios de Moscú y los valores de la recta

np.linalg.norm(moscu - y)  # Calcula la norma de la diferencia entre los precios de Moscú y los valores de la recta
print(np.linalg.norm(moscu - y))  # Imprime la norma de la diferencia entre los precios de Moscú y los valores de la recta

n = np.size(moscu)  # Obtiene el tamaño del array 'moscu'
y = moscu
x = fechas
a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(np.power(x, 2)) - np.power(np.sum(x), 2))  # Calcula la pendiente de la recta
b = (np.sum(y) - a * np.sum(x)) / n  # Calcula la ordenada al origen de la recta
print(f"Pendiente (a): {a}")  # Imprime la pendiente de la recta
print(f"Ordenada al origen (b): {b}")  # Imprime la ordenada al origen de la recta

y = a * x + b  # Calcula los valores de la recta utilizando la pendiente y la ordenada al origen
print(y)  # Imprime los valores de la recta

np.linalg.norm(moscu - y)  # Calcula la norma de la diferencia entre los precios de Moscú y los valores de la recta
print(np.linalg.norm(moscu - y))  # Imprime la norma de la diferencia entre los precios de Moscú y los valores de la recta

# plt.plot(fechas, moscu, label='Moscú')  # Grafica los precios de Moscú
# plt.plot(x, y, label='Recta')  # Grafica la recta
# plt.plot(25, a * 25 + b, 'ro')  # Grafica un punto rojo en la posición (25, a * 25 + b)
# plt.show()  # Muestra la gráfica

fecha_exacta = a * 25 + b  # Calcula la fecha exacta utilizando la pendiente y la ordenada al origen
print(f"Fecha exacta: {fecha_exacta}")  # Imprime la fecha exacta calculada

# ENTEROS
np.random.randint(40, 100, 100) # Genera 100 números enteros aleatorios entre 40 y 100
print(('Numeros enteros: '), np.random.randint(40,100, 100))  # Imprime los números enteros aleatorios generados

# DECIMALES
np.random.uniform(0.1, 0.9, 100) # Genera 100 números decimales aleatorios entre 40 y 100
print(('Numeros decimales: '), np.random.uniform(40,100, 100))  # Imprime los números decimales aleatorios generados

pendientes = np.random.uniform(0.1, 0.9, 100)  # Genera 100 pendientes aleatorias entre 0.1 y 0.9
print(('Pendientes: '), pendientes)  # Imprime las pendientes aleatorias generadas

for i in range(100):
    print(np.linalg.norm(moscu - (pendientes[i] * x + b)))  # Calcula la norma de la diferencia entre los precios de Moscú y los valores de la recta para cada pendiente
    # Imprime la norma de la diferencia para cada pendiente

norma = np.array([])  # Inicializa un array vacío para almacenar las normas

for i in range(100):
    norma = np.append(norma, np.linalg.norm(moscu - (pendientes[i] * x + b)))  # Calcula la norma y la agrega al array 'norma'
    print(norma)  # Imprime el array 'norma' después de cada iteración

# generar siempre los mismos números aleatorios
semilla = np.random.seed(99)  # Establece la semilla para la generación de números aleatorios
aleatorios_iguales = np.random.uniform(0.1, 0.9, 5)  # Genera 5 números decimales aleatorios entre 0.1 y 0.9
print(aleatorios_iguales)  # Imprime la semilla utilizada para la generación de números aleatorios

np.random.seed(99)
norma = np.array([])  # Inicializa un array vacío para almacenar las normas

for i in range(100):
    norma = np.append(norma, np.linalg.norm(moscu - (pendientes[i] * x + b)))  # Calcula la norma y la agrega al array 'norma'
    print(norma)  # Imprime el array 'norma' después de cada iteración


# EXPORTAR ARRAYS

datos = np.column_stack([norma, pendientes])  # Combina los arrays 'norma' y 'pendientes' en un solo array de dos columnas
print(datos)  # Imprime el array combinado 'datos'
print(datos.shape)  # Imprime la forma del array 'datos' (número de filas y columnas)

np.savetxt('datos_y_pendientes.csv', datos, delimiter=',')  # Guarda el array 'datos' en un archivo CSV