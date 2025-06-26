import pandas as pd
import numpy as np
from scipy.special import comb
from scipy.stats import poisson
import matplotlib.pyplot as plt
import math

datos = pd.read_csv("Estadística_con_Python_Probabilidad_y_muestreo\\Distribucion_binominal\\data\\datos.csv", encoding='latin-1')
print(datos)

print(np.e)

media = 20 # cantidada de pedidos por hora
k = 15 # Número de eventos

probabilidad = ((np.e ** (-media)) * (media ** k)) / (math.factorial(k)) # Fórmula de Poisson
print(f"La probabilidad de que ocurran {k} eventos en una hora es: {probabilidad:.4f}")

probabilidad_scipy = poisson.pmf(k, media) # Usando scipy para calcular la probabilidad
print(f"La probabilidad de que ocurran {k} eventos en una hora (usando scipy) es: {probabilidad_scipy:.4f}")

# Estimando los clientes en determinada hora
'''
El número media de clientes que ingresan a una panadería por hora es 20. Obtenga la probabilidad de que, 
en la próxima hora, ingresen exactamente 25 clientes.
'''

# --- Definir los parámetros ---
# 'mu' (mew) es el símbolo que usa SciPy para la media (lambda) de la distribución de Poisson.
# Representa el número promedio de eventos en un intervalo dado.
media_clientes_por_hora = 20

# 'k' es el número exacto de ocurrencias que nos interesa.
# Queremos la probabilidad de que ingresen exactamente 25 clientes.
k_clientes = 25

# --- Calcular la probabilidad usando scipy.stats.poisson.pmf ---
# poisson.pmf(k, mu) calcula la probabilidad de P(X=k) para una media 'mu'.
# Es decir, nos da la probabilidad de obtener exactamente 'k_clientes' eventos
# cuando la tasa promedio de eventos es 'media_clientes_por_hora'.
probabilidad_decimal = poisson.pmf(k=k_clientes, mu=media_clientes_por_hora)

probabilidad_porcentaje = probabilidad_decimal * 100  # Convertimos a porcentaje

# --- Mostrar el resultado ---
# Formateamos el resultado para que se muestre con 4 decimales para mayor claridad.
print(f"La probabilidad de que ingresen exactamente {k_clientes} clientes")
print(f"en la próxima hora (con una media de {media_clientes_por_hora}) es:")
print(f"{probabilidad_porcentaje:.2f}%") # Mostramos el valor como porcentaje

'''
4,46%

¡Alternativa correcta! Aquí está el código de la solución:

from scipy.stats import poisson

media = 20
k = 25

probabilidad = poisson.pmf(k, media)
print(f'{probabilidad:.2%}')
'''