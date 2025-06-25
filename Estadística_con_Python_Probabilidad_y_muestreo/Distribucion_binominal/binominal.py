import pandas as pd
import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt

datos = pd.read_csv("Estadística_con_Python_Probabilidad_y_muestreo\\Distribucion_binominal\\data\\datos.csv", encoding='latin-1')
print(datos)

combinaciones = comb(60, 6)
print(f"Combinaciones posibles al elegir 6 números de 60: {combinaciones}")

probabilidad = 1 / combinaciones
print(f"Probabilidad de acertar los 6 números: {probabilidad:.10f}")

# Exposicion de premios de Alura

combinaciones = comb(25, 20)
print(f"Combinaciones posibles al elegir 20 números de 25: {combinaciones}")

probabilidad = 1 / combinaciones
print(f"Probabilidad de acertar los 20 números: {probabilidad:.10f}")

# Concurso para cientifico de datos

n = 10 # Cantidad de preguntas
print(f"cantidad de preguntas: {n} preguntas")

numero_de_alternativas_por_pregunta = 3
p = 1 / numero_de_alternativas_por_pregunta # Probabilidad de acertar una pregunta
print(f"Probabilidad de acertar una pregunta: {p:.2f}")

q = 1 - p # Probabilidad de fallar una pregunta
print(f"Probabilidad de fallar una pregunta: {q:.2f}")

k = 5 # Cantidad de preguntas acertadas
print(f"Cantidad de preguntas acertadas: {k} preguntas")

probabilidad = comb(n, k) * (p ** k) * (q ** (n - k)) # Usando la fórmula de la distribución binomial
print(f"Probabilidad de acertar {k} preguntas: {probabilidad:.10f}")

from scipy.stats import binom

probabilidad = binom.pmf(k, n, p) # Usando la función de masa de probabilidad
print(f"Probabilidad de acertar {k} preguntas usando scipy: {probabilidad:.10f}")

P_acertar_5_o_mas = binom.pmf(5, n, p) + binom.pmf(6, n, p) + binom.pmf(7, n, p) + binom.pmf(8, n, p) + binom.pmf(9, n, p) + binom.pmf(10, n, p)

print(f"Probabilidad de acertar 5 o más preguntas: {P_acertar_5_o_mas:.10f}")

P_acertar_5_o_mas = binom.pmf([5, 6, 7, 8, 9, 10], n, p).sum()
print(f"Probabilidad de acertar 5 o más preguntas usando scipy: {P_acertar_5_o_mas:.10f}")

P_acertar_5_o_mas = 1 - binom.cdf(4, n, p)
print(f"Probabilidad de acertar 5 o más preguntas usando la función de distribución acumulada: {P_acertar_5_o_mas:.10f}")

P_acertar_5_o_mas = binom.sf(4, n, p)
print(f"Probabilidad de acertar 5 o más preguntas usando la función de supervivencia: {P_acertar_5_o_mas:.10f}")

# Lanzamiento de una moneda
combinaciones = comb(60, 6)
n = 4 # Total de lanzamientos
k = 2 # Cantidad de caras
p = 0.5 # Probabilidad de cara
probabilidad = binom.pmf(k, n, p)
print(f"Probabilidad de obtener {k} caras en {n} lanzamientos: {probabilidad:.10f}")

# Lanzamineto de un dado
n = 10 # Total de lanzamientos
k = 2 # Cantidad de veces que sale el número 5
p = 1 / 6 # Probabilidad de que salga el número 5
probabilidad = binom.sf(k, n, p)
print(f"Probabilidad de obtener {k} veces el número 5 en {n} lanzamientos: {probabilidad:.10f}")

# Ejemplo: Yincana
p = 0.6 # porcentaje de participantes
n = 12 # cantidad de miembros del equipo
k = 8 # cantidad de mujeres por equipo
probabilidad = binom.pmf(k, n, p)
print(f"Probabilidad de que en un equipo de {n} miembros haya {k} mujeres: {probabilidad:.10f}")

equipos = 30 * probabilidad
print(f"Cantidad de equipos que cumplen la condición: {equipos:.2f}")

# Posibilidad de tener ojos azules
p = 0.22 # porcentaje de personas con ojos azules
n = 3 # cantidad de hijos
k = 2 # personas por pareja
N = 50 # Número de parejas
probabilidad = binom.pmf(k, n, p)   
media = probabilidad * N
print(f"Probabilidad de que al menos uno de los hijos tenga ojos azules: {probabilidad:.10f}")
print(f"Media de parejas con al menos un hijo con ojos azules: {media:.2f}")