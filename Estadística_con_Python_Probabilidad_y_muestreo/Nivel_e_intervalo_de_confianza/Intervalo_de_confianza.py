import pandas as pd
import numpy as np
from scipy.special import comb
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

datos = pd.read_csv("Estadística_con_Python_Probabilidad_y_muestreo\\Distribucion_binominal\\data\\datos.csv", encoding='latin-1')
print(datos)

n = 2000
total_de_muestras = 1500

muestras = pd.DataFrame()
print(muestras)

for i in range(total_de_muestras):
    _ = datos.Edad.sample(n)
    _.index = range(0, len(_))
    muestras['Muestra_' + str(i)] = _

print(muestras)

muestras.mean()
print(muestras.mean())
print(muestras.mean().hist())

datos['Edad'].mean()
print(datos['Edad'].mean())
print(muestras.mean().mean())

print(muestras.mean().std()) #desviación estándar de la media muestral


print(datos.Edad.std() / np.sqrt(n)) #desviación estándar de la población

# Nivel de confianza y significación

media_muestra = 5050
print(media_muestra)

significancia = 0.05
print(significancia)

confianza = 1 - significancia
print(confianza)

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

# Cálculo del valor crítico Z para un nivel de confianza del 95%

z_critico = norm.ppf(1 - significancia / 2)
print("Valor crítico Z para un nivel de confianza del 95%:", z_critico)

desviacion_estandar = 150
n = 20
raiz_de_n = math.sqrt(n)
print("Raíz cuadrada de n:", raiz_de_n)

sigma = desviacion_estandar / raiz_de_n
print("Desviación estándar de la media muestral:", sigma)

e = z_critico * sigma
print("Error estándar:", e)

intervalo = (media_muestra - e, media_muestra + e)
print("Intervalo de confianza al 95%:", intervalo)

norm.interval(confidence = 0.95, loc=media_muestra, scale=sigma)
print("Intervalo de confianza al 95% usando scipy:", norm.interval(confidence=0.95, loc=media_muestra, scale=sigma))

# Margen de error
'''
Para estimar la cantidad media gastada por cada cliente de una gran cadena de comida rápida, se seleccionó una muestra de 50 clientes.

Suponiendo que el valor de la desviación estándar de la población es de $ 6,00 y que esta población se distribuye normalmente, obtenga el margen de error de esta estimación para un nivel de confianza del 95%.
'''


# Datos proporcionados
desviacion_estandar_poblacion = 6.00  # Desviación estándar de la población (sigma)
tamano_muestra = 50                  # Tamaño de la muestra (n)
nivel_confianza = 0.95               # Nivel de confianza

# 1. Calcular el error estándar de la media
# Comentario: El error estándar de la media mide la dispersión de las medias muestrales
# alrededor de la media poblacional. Se calcula dividiendo la desviación estándar
# de la población por la raíz cuadrada del tamaño de la muestra.
error_estandar_media = desviacion_estandar_poblacion / np.sqrt(tamano_muestra)

# 2. Obtener el valor crítico de Z para un nivel de confianza del 95%
# Comentario: Para un nivel de confianza del 95%, queremos encontrar el valor Z
# que deja el 2.5% de probabilidad en cada cola de la distribución normal estándar.
# La función ppf (percent point function) es la inversa de la función de distribución acumulada (CDF),
# y nos da el valor z correspondiente a una probabilidad acumulada.
# Para el 95% central, la probabilidad acumulada para la cola derecha es 0.95 + (1-0.95)/2 = 0.975
valor_critico_z = norm.ppf(1 - (1 - nivel_confianza) / 2)

# 3. Calcular el margen de error
# Comentario: El margen de error es el producto del valor crítico de Z y el error estándar de la media.
# Representa la cantidad máxima de diferencia que se esperaría entre la media muestral
# y la media poblacional real, con un cierto nivel de confianza.
margen_de_error = valor_critico_z * error_estandar_media

print(f"La desviación estándar de la población (sigma) es: ${desviacion_estandar_poblacion:.2f}")
print(f"El tamaño de la muestra (n) es: {tamano_muestra}")
print(f"El nivel de confianza es: {nivel_confianza*100:.0f}%")
print(f"El error estándar de la media es: ${error_estandar_media:.4f}")
print(f"El valor crítico de Z para un 95% de confianza es: {valor_critico_z:.4f}")
print(f"El margen de error de la estimación es: ${margen_de_error:.2f}")

'''
$ 1.66

¡Alternativa correcta! El siguiente código sirve como ejemplo para resolver este problema:

from scipy.stats import norm
import numpy as np

z = norm.ppf(0.975)
desviacion_estandar = 6
n = 50

e = z * (desviacion_estandar / np.sqrt(n))
print(f"$ {e:0.2f}")
'''

# Intervalo de confianza

'''
Una muestra aleatoria simple de 1976 elementos de una población distribuida normalmente, con una desviación estándar de 11, dio como resultado una media muestral de 28.

¿Cuál es el intervalo de confianza del 90% para la media de la población?
'''

# Datos proporcionados
media_muestral = 28                 # Media de la muestra (x_barra)
desviacion_estandar_poblacion = 11  # Desviación estándar de la población (sigma)
tamano_muestra = 1976               # Tamaño de la muestra (n)
nivel_confianza = 0.90              # Nivel de confianza deseado (90%)

# 1. Calcular el error estándar de la media
# Comentario: El error estándar mide la variabilidad esperada de las medias muestrales.
# Se calcula dividiendo la desviación estándar de la población por la raíz cuadrada del tamaño de la muestra.
error_estandar_media = desviacion_estandar_poblacion / np.sqrt(tamano_muestra)

# 2. Obtener el valor crítico de Z para el nivel de confianza del 90%
# Comentario: Para un intervalo de confianza del 90%, necesitamos el valor Z que
# acumula el (1 - (1 - 0.90)/2) = 0.95 de probabilidad en la distribución normal estándar.
# La función ppf (percent point function) es la inversa de la CDF y nos da el valor Z.
valor_critico_z = norm.ppf(1 - (1 - nivel_confianza) / 2)

# 3. Calcular el margen de error
# Comentario: El margen de error es la parte que se suma y se resta a la media muestral
# para obtener los límites del intervalo. Se calcula multiplicando el valor crítico de Z
# por el error estándar de la media.
margen_de_error = valor_critico_z * error_estandar_media

# 4. Calcular el intervalo de confianza
# Comentario: El límite inferior se obtiene restando el margen de error a la media muestral.
limite_inferior = media_muestral - margen_de_error
# Comentario: El límite superior se obtiene sumando el margen de error a la media muestral.
limite_superior = media_muestral + margen_de_error

print(f"Media muestral: {media_muestral}")
print(f"Desviación estándar de la población: {desviacion_estandar_poblacion}")
print(f"Tamaño de la muestra: {tamano_muestra}")
print(f"Nivel de confianza: {nivel_confianza*100:.0f}%")
print(f"Error estándar de la media: {error_estandar_media:.4f}")
print(f"Valor crítico de Z (para 90% de confianza): {valor_critico_z:.4f}")
print(f"Margen de error: {margen_de_error:.4f}")
print(f"El intervalo de confianza del 90% para la media de la población es: ({limite_inferior:.2f}, {limite_superior:.2f})")

'''
27.59 a 28.41

¡Alternativa correcta! Aquí está el código de sugerencia de solución:

from scipy.stats import norm
import numpy as np

media_muestral = 28
desviacion_estandar = 11
n = 1976

norm.interval(alpha = 0.90,
                    loc = media_muestral,
                    scale = desviacion_estandar / np.sqrt(n))
'''