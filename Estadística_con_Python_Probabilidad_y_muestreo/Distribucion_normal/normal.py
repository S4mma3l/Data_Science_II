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

print(tabla_normal_estandarizada)

# caso 1:

media = 1.70
desviacion_estandar = 0.1
Z = (1.80 - media) / desviacion_estandar
print("Z:", Z)

probabilidad = 0.8413
print("Probabilidad de que la altura sea menor a 1.80:", probabilidad)

# caso 1 con scipy
probabilidad = norm.cdf(1.80, loc=media, scale=desviacion_estandar)
print("Probabilidad de que la altura sea menor a 1.80 con scipy:", probabilidad)

# Prueba de estadistica
media = 70
desviacion_estandar = 5

probabilidad = norm.cdf(85, loc=media, scale=desviacion_estandar)
print("probabilidad que un estudiante,seleccionado al azar, saque menos de 85 puntos:", probabilidad)

'''
99,86%

¡Alternativa correcta! Aquí está una sugerencia de la solución:

from scipy.stats import norm

media = 70
desviacion_estandar = 5
Z = (85 - media) / desviacion_estandar

norm.cdf(Z)
'''

# caso 2:

media = 1.70
desviacion_estandar = 0.1
Z = (1.60 - media) / desviacion_estandar
print("Z:", Z)
Z = (1.80 - media) / desviacion_estandar
print("Z:", Z)

probabilidad = norm.cdf(1.80, loc=media, scale=desviacion_estandar) - norm.cdf(1.60, loc=media, scale=desviacion_estandar)
print("Probabilidad de que la altura sea mayor a 1.60 y menor a 1.80:", probabilidad)

# Facturacion diaria
'''
La facturación diaria de un controlador de aplicación sigue una distribución aproximadamente normal, 
con un media de $ 300,00 y una desviación estándar igual a $ 50,00. Obtenga las probabilidades de que, 
en un día aleatorio, el conductor gane:

1) Entre $ 250,00 y $ 350,00

2) Entre $ 400,00 y $ 500,00
'''
media_1 = 300
desviacion_estandar_1 = 50
probabilidad_1 = norm.cdf(350, loc=media_1, scale=desviacion_estandar_1) - norm.cdf(250, loc=media_1, scale=desviacion_estandar_1)
print("Probabilidad de que la facturación diaria esté entre $250,00 y $350,00:", probabilidad_1)
probabilidad_2 = norm.cdf(500, loc=media_1, scale=desviacion_estandar_1) - norm.cdf(400, loc=media_1, scale=desviacion_estandar_1)
print("Probabilidad de que la facturación diaria esté entre $400,00 y $500,00:", probabilidad_2)

# pasar a porcentaje
probabilidad_1 *= 100
probabilidad_2 *= 100
print("Probabilidad de que la facturación diaria esté entre $250,00 y $350,00:", probabilidad_1, "%")
print("Probabilidad de que la facturación diaria esté entre $400,00 y $500,00:", probabilidad_2, "%")

'''
1) 68,27%; 2) 2,27%

¡Alternativa correcta! Los siguientes códigos ejemplifican la solución al problema:

1)

from scipy.stats import norm

media = 300
desviacion_estandar = 50
Z_inferior = (250 - media) / desviacion_estandar
Z_superior = (350 - media) / desviacion_estandar

probabilidad = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print(f'{probabilidad:.2%}')

2)

from scipy.stats import norm

media = 300
desviacion_estandar = 50
Z_inferior = (400 - media) / desviacion_estandar
Z_superior = (500 - media) / desviacion_estandar

probabilidad = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print(f'{probabilidad:.2%}')
'''

# caso 3:
media = 1.70
desviacion_estandar = 0.1

Z = (1.90 - media) / desviacion_estandar
print("Z:", Z)
probabilidad = 1 - norm.cdf(1.90, loc=media, scale=desviacion_estandar)
print("Probabilidad de que la altura sea mayor a 1.90:", probabilidad)

# Vida util
'''
Una empresa verificó que las lámparas incandescentes XPTO tienen una vida útil normalmente distribuida, 
con un media igual a 720 días y una desviación estándar igual a 30 días. 
Calcula la probabilidad de que una lámpara, elegida al azar, dure:

1) Entre 650 y 750 días

2) Más de 800 días

3) Menos de 700 días
'''
media_2 = 720
desviacion_estandar_2 = 30
probabilidad_3 = norm.cdf(750, loc=media_2, scale=desviacion_estandar_2) - norm.cdf(650, loc=media_2, scale=desviacion_estandar_2)
print("Probabilidad de que la lámpara dure entre 650 y 750 días:", probabilidad_3)
probabilidad_4 = 1 - norm.cdf(800, loc=media_2, scale=desviacion_estandar_2)
print("Probabilidad de que la lámpara dure más de 800 días:", probabilidad_4)
probabilidad_5 = norm.cdf(700, loc=media_2, scale=desviacion_estandar_2)
print("Probabilidad de que la lámpara dure menos de 700 días:", probabilidad_5)
# pasar a porcentaje
probabilidad_3 *= 100       
probabilidad_4 *= 100
probabilidad_5 *= 100
print("Probabilidad de que la lámpara dure entre 650 y 750 días:", probabilidad_3, "%")
print("Probabilidad de que la lámpara dure más de 800 días:", probabilidad_4, "%")
print("Probabilidad de que la lámpara dure menos de 700 días:", probabilidad_5, "%")
'''
1) 83,15%; 2) 0,38%; 3) 25,25%

¡Alternativa correcta! Sigue una opción para resolver este problema:

from scipy.stats import norm

media = 720
desviacion_estandar = 30

# Item A
Z_inferior = (650 - media) / desviacion_estandar
Z_superior = (750 - media) / desviacion_estandar

probabilidad = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print(f'{probabilidad:.2%}')

# Item B
Z = (800 - media) / desviacion_estandar

probabilidad = 1 - norm.cdf(Z)
print(f'{probabilidad:.2%}')

# Item C
Z = (700 - media) / desviacion_estandar

probabilidad = norm.cdf(Z)
print(f'{probabilidad:.2%}')
'''

#  calculando probabilidades
'''
Usando la tabla estandarizada, o las herramientas proporcionadas por Python, 
encuentre el área debajo de la curva normal para los valores Z a continuación:

1) Z < 1,96

2) Z > 2,15

3) Z < -0,78

4) Z > 0,59
'''
'''
respuesta:
1) 0,9750; 2) 0,0158; 3) 0,2177; 4) 0,2776

¡Alternativa correcta! Si no desea utilizar la tabla estandarizada, siga el código:

from scipy.stats import norm

# Item A
probabilidad = norm.cdf(1.96)
print(f'{probabilidad:0.4f}')

# Item B
probabilidad = 1 - norm.cdf(2.15)
# o -> probabilidad = norm.sf(2.15)
print(f'{probabilidad:0.4f}')

# Item C
probabilidad = norm.cdf(-0.78)
print(f'{probabilidad:0.4f}')

# Item D
probabilidad = 1 - norm.cdf(0.59)
# o -> probabilidad = norm.sf(0.59)
print(f'{probabilidad:0.4f}')
'''