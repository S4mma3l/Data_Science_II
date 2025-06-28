import pandas as pd
import numpy as np
from scipy.special import comb
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

datos = pd.read_csv("Estadística_con_Python_Probabilidad_y_muestreo\\Distribucion_binominal\\data\\datos.csv", encoding='latin-1')
print(datos)
# Tablas estandarizadas

tabla_normal_estandarizada = pd.DataFrame(
    [],
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])
for index in tabla_normal_estandarizada.index:
    for column in tabla_normal_estandarizada.columns:
        z = np.round(float(index) + float(column), 2)
        tabla_normal_estandarizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(z))

tabla_normal_estandarizada.rename_axis('Z', axis='columns', inplace=True)

# Mostrar una parte de la tabla normal estandarizada

tabla_normal_estandarizada[16:26]

print(tabla_normal_estandarizada)

0.95/2
0.5 + 0.95 / 2

z = norm.ppf(0.5 + 0.95 / 2)
print(z)

sigma = 3323.39

e = 100

n = (z * sigma / e) ** 2
print(int(n.round()))

# Calcular el tamaño de la muestra

import numpy as np
from scipy.stats import norm

# Datos proporcionados
media_poblacion_conocida = 45.50  # Valor promedio gastado por los clientes (mu)
desviacion_estandar_poblacion = 15.00  # Desviación estándar de los gastos (sigma)
nivel_significancia = 0.10             # Nivel de significancia (alfa)
error_maximo_porcentaje = 0.10         # Error máximo aceptable como porcentaje

# 1. Calcular el margen de error (ME)
# Comentario: El margen de error se define como un porcentaje del valor promedio.
margen_de_error = error_maximo_porcentaje * media_poblacion_conocida

# 2. Calcular el nivel de confianza a partir del nivel de significancia
# Comentario: El nivel de confianza es 1 menos el nivel de significancia.
nivel_confianza = 1 - nivel_significancia

# 3. Obtener el valor crítico de Z para el nivel de confianza
# Comentario: Para un intervalo de confianza del 90% (1 - 0.10),
# necesitamos el valor Z que acumula 1 - (alfa/2) = 1 - (0.10/2) = 0.95 de probabilidad.
valor_critico_z = norm.ppf(1 - (nivel_significancia / 2))

# 4. Calcular el tamaño de la muestra (n)
# Comentario: La fórmula para el tamaño de la muestra se deriva de la fórmula del margen de error,
# despejando n. Redondeamos hacia arriba porque el tamaño de la muestra debe ser un número entero
# y no podemos tener una fracción de una persona o elemento.
tamano_muestra = ( (valor_critico_z * desviacion_estandar_poblacion) / margen_de_error )**2

# Como el tamaño de la muestra debe ser un número entero, redondeamos hacia arriba
tamano_muestra_redondeado = np.ceil(tamano_muestra)

print(f"Valor promedio gastado por los clientes: ${media_poblacion_conocida:.2f}")
print(f"Desviación estándar de los gastos: ${desviacion_estandar_poblacion:.2f}")
print(f"Nivel de significancia: {nivel_significancia*100:.0f}%")
print(f"Error máximo aceptable (como porcentaje): {error_maximo_porcentaje*100:.0f}%")
print(f"Margen de error absoluto (ME): ${margen_de_error:.2f}")
print(f"Nivel de confianza: {nivel_confianza*100:.0f}%")
print(f"Valor crítico de Z (para {nivel_confianza*100:.0f}% de confianza): {valor_critico_z:.4f}")
print(f"Tamaño de la muestra calculado (sin redondear): {tamano_muestra:.4f}")
print(f"El tamaño de la muestra necesario es: {int(tamano_muestra_redondeado)}")

# variables cuantitativas y poblaciones finitas

N = 10000 # cantidad de latas

z = norm.ppf(0.5 + 0.95 / 2) # valor crítico de Z para un nivel de confianza del 95%

s = 12 # desviación estándar de la población

e = 5 # error máximo permitido

n = ((z**2) * (s**2) * (N)) / ((N - 1) * (e**2) + (z**2) * (s**2))
print(f"El tamaño de la muestra necesario para una población finita es: {int(n.round())}")

#  Muestra de sacos de harina

# Datos proporcionados
desviacion_estandar_muestral_g = 480  # Desviación estándar muestral en gramos
error_maximo_kg = 0.3                # Margen de error máximo aceptable en kilogramos
nivel_confianza = 0.95               # Nivel de confianza deseado (95%)
tamano_poblacion_N = 2000            # Tamaño total de la población

# 1. Convertir la desviación estándar a kilogramos
# Comentario: Es crucial que todas las unidades sean consistentes.
desviacion_estandar_kg = desviacion_estandar_muestral_g / 1000

# 2. Obtener el valor crítico de Z para el nivel de confianza del 95%
# Comentario: Para un intervalo de confianza del 95%, necesitamos el valor Z que
# acumula 1 - (alfa/2) = 1 - (0.05/2) = 0.975 de probabilidad en la distribución normal estándar.
valor_critico_z = norm.ppf(1 - (1 - nivel_confianza) / 2)

# 3. Calcular el tamaño de la muestra inicial (n_0) para población infinita
# Comentario: Esta fórmula calcula el tamaño de muestra sin considerar el tamaño finito de la población.
# Se basa en el margen de error, la desviación estándar y el valor Z.
n_0 = ( (valor_critico_z * desviacion_estandar_kg) / error_maximo_kg )**2

# 4. Calcular el tamaño de la muestra ajustado (n) para población finita
# Comentario: Si el tamaño de la muestra inicial (n_0) es una porción significativa
# de la población (más del 5%), se aplica este factor de corrección para obtener un tamaño de muestra más preciso.
n_ajustado = (n_0 * tamano_poblacion_N) / (n_0 + (tamano_poblacion_N - 1))

# Como el tamaño de la muestra debe ser un número entero, redondeamos hacia arriba
tamano_muestra_final = np.ceil(n_ajustado)

print(f"Desviación estándar (en kg): {desviacion_estandar_kg:.3f} kg")
print(f"Margen de error (ME): {error_maximo_kg:.1f} kg")
print(f"Nivel de confianza: {nivel_confianza*100:.0f}%")
print(f"Valor crítico de Z: {valor_critico_z:.4f}")
print(f"Tamaño de la población (N): {tamano_poblacion_N}")
print(f"Tamaño de la muestra inicial (n_0) calculado: {n_0:.4f}")
print(f"Tamaño de la muestra ajustado para población finita (n_ajustado) calculado: {n_ajustado:.4f}")
print(f"El tamaño de muestra que debe seleccionarse es: {int(tamano_muestra_final)}")