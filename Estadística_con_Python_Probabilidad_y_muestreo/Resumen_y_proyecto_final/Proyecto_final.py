import pandas as pd
import numpy as np
from scipy.special import comb
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

datos = pd.read_csv("Estadística_con_Python_Probabilidad_y_muestreo\\Resumen_y_proyecto_final\\datos\\datos.csv", encoding='latin-1')
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

ingresos_5000 = datos.query('Ingreso <= 5000')['Ingreso']
print(ingresos_5000)

sigma = ingresos_5000.std()
print(sigma)

media = ingresos_5000.mean()
print(media)

z = norm.ppf(0.5 + 0.95 / 2)
print(z)

e = 10

n = (z * sigma / e) ** 2
print(int(n.round()))

intervalo = norm.interval(0.95, loc=media, scale=sigma / np.sqrt(n))
print(intervalo)

tamano_simulacion = 1000

medias = [ingresos_5000.sample(n).mean() for n in range(1, tamano_simulacion)]
medias = pd.DataFrame(medias)

ax = medias.plot(style='.')
ax.figure.set_size_inches(12, 6)
ax.hlines(y=media, xmin=0, xmax=tamano_simulacion, color='black', linestyles= '-', label='Media muestral')
ax.hlines(y=intervalo[0], xmin=0, xmax=tamano_simulacion, color='red', linestyles= '-', label='Límite inferior del intervalo de confianza')
ax.hlines(y=intervalo[1], xmin=0, xmax=tamano_simulacion, color='red', linestyles= '-', label='Límite superior del intervalo de confianza')
plt.show()