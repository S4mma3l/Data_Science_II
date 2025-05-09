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
