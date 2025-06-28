import pandas as pd
import numpy as np
from scipy.stats import norm, binom
import math

datos = pd.read_csv("Estadística_con_Python_Probabilidad_y_muestreo\\Resumen_y_proyecto_final\\datos\\datos.csv", encoding='latin-1')
print(datos.head())

k = 7 # Número de éxitos
n = 10 # Número de intentos

p = 0.7 # Probabilidad de éxito

probabilidad = binom.pmf(k, n, p) # Función de masa de probabilidad para la distribución binomial
print(f"La probabilidad de obtener {k} éxitos en {n} intentos con una probabilidad de éxito de {p} es: {probabilidad:.4f}")

media = n * p # Media de la distribución binomial
n = media / p # Número de intentos necesarios para alcanzar la media

n = 100 / probabilidad # Número de intentos necesarios para alcanzar una probabilidad específica
print(f"Para alcanzar una probabilidad de {probabilidad:.4f}, se necesitan {int(n)} intentos.")

# Desafio #1
dataset = datos.Ingreso.sample(n=200, random_state=101) # Muestra aleatoria de 200 ingresos
media_muestra = dataset.mean() # Media de la muestra
desviacion_muestra = dataset.std() # Desviación estándar de la muestra
print(f"Media de la muestra: {media_muestra:.2f}, Desviación estándar de la muestra: {desviacion_muestra:.2f}")

media_muestra = dataset.mean()
desviacion_estandar_muestra = dataset.std()
recursos = 150000
costo_entrevistas = 100
print(f"Con un presupuesto de {recursos}, se pueden realizar {int(recursos / costo_entrevistas)} entrevistas.")

# Desafio #2
e = 0.10 * media_muestra # Error máximo permitido
print(f"Error máximo permitido: {e:.2f}")
# 90%
0.5 + 0.90 / 2
z = norm.ppf(0.5 + 0.90 / 2) # Valor crítico z para un intervalo de confianza del 95%
n_confianza_90 = (z * desviacion_estandar_muestra / e) ** 2 # Tamaño de muestra necesario para un intervalo de confianza del 90%
n_confianza_90 = int(n_confianza_90.round())
print(f"Tamaño de muestra necesario para un intervalo de confianza del 90%: {n_confianza_90}")

#  95%
0.5 + 0.95 / 2
z = norm.ppf(0.5 + 0.95 / 2) # Valor crítico z para un intervalo de confianza del 95%
n_confianza_95 = (z * desviacion_estandar_muestra / e) ** 2 # Tamaño de muestra necesario para un intervalo de confianza del 90%
n_confianza_95 = int(n_confianza_95.round())
print(f"Tamaño de muestra necesario para un intervalo de confianza del 95%: {n_confianza_95}")

#  99%
0.5 + 0.99 / 2
z = norm.ppf(0.5 + 0.99 / 2) # Valor crítico z para un intervalo de confianza del 95%
n_confianza_99 = (z * desviacion_estandar_muestra / e) ** 2 # Tamaño de muestra necesario para un intervalo de confianza del 90%
n_confianza_99 = int(n_confianza_99.round())
print(f"Tamaño de muestra necesario para un intervalo de confianza del 99%: {n_confianza_99}")

# Desafio #3

n_confianza_90 = n_confianza_90 * costo_entrevistas
n_confianza_95 = n_confianza_95 * costo_entrevistas
n_confianza_99 = n_confianza_99 * costo_entrevistas
print(f"Costo total para un intervalo de confianza del 90%: {n_confianza_90}, 95%: {n_confianza_95}, 99%: {n_confianza_99}")

# Desafio #4

intervalo = norm.interval(confidence=0.95, loc=media_muestra, scale=desviacion_estandar_muestra / np.sqrt(n_confianza_95))
print(intervalo)

# Desafio #5

n_confianza_95 = recursos / costo_entrevistas
print(n_confianza_95)

z = norm.ppf(.975)
e = z * (desviacion_estandar_muestra / np.sqrt(n_confianza_95)
         )
print(e)

e_porcentual = 100 * e / media_muestra
print(f'El nuevo margen de error es {e_porcentual:.2f}')

# Dasafio #6

e = 0.05 * media_muestra
print(e)

z = norm.ppf(.975)
n_confianza_95 = (z * (desviacion_estandar_muestra / e)) ** 2
n_confianza_95 = int(n_confianza_95.round())
print(n_confianza_95)

costo_confianza_95 = n_confianza_95 * costo_entrevistas
print(costo_confianza_95)