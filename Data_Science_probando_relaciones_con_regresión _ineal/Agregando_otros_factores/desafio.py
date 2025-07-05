# -*- coding: utf-8 -*-
# Importación de las bibliotecas necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# --- Carga de Datos ---
# Especifica la ruta a tu archivo CSV.
# ¡Asegúrate de que la ruta sea correcta!
ruta_dataset = r'Data_Science_probando_relaciones_con_regresión _ineal\Agregando_otros_factores\desafio\hoteis.csv'

# Cargar el dataset en un DataFrame de pandas
try:
    df_hoteles = pd.read_csv(ruta_dataset)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta '{ruta_dataset}'")
    exit() # Salir del script si no se encuentra el archivo

# --- Análisis Exploratorio con PairPlot ---
print("Generando PairPlot para análisis inicial...")

# Crear el PairPlot con Seaborn para ver todas las relaciones.
# 'kind="reg"' añade una línea de regresión para ver tendencias.
# 'diag_kind="kde"' muestra la distribución de cada variable.
pair_plot = sns.pairplot(df_hoteles, kind='reg', diag_kind='kde')

# Añadir un título general al gráfico para mayor claridad
pair_plot.fig.suptitle('Análisis de Pares de Variables de Hoteles', y=1.02)

# Mostrar el gráfico
plt.show()

# Imprimir las primeras filas para confirmar que los datos se cargaron bien
print("\nPrimeras 5 filas del dataset:")
print(df_hoteles.head())