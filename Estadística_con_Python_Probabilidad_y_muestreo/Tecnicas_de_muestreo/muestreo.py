import pandas as pd
import numpy as np
from scipy.special import comb
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

datos = pd.read_csv("Estadística_con_Python_Probabilidad_y_muestreo\\Distribucion_binominal\\data\\datos.csv", encoding='latin-1')
print(datos)

print(datos.shape[0])  # Número de filas
print(datos.Ingreso.mean())  # Media de la columna Ingresos

muestra = datos.sample(n=1000, random_state=101)  # Muestra aleatoria de 100 filas
print(muestra)
print(muestra.shape[0])  # Número de filas en la muestra
print(muestra.Ingreso.mean())  # Media de la columna Ingresos en la muestra

print(datos.Sexo.value_counts(normalize=True)*100)  # Conteo de valores únicos en la columna Sexo
print(muestra.Sexo.value_counts(normalize=True)*100)  # Conteo de valores únicos en la columna Sexo
