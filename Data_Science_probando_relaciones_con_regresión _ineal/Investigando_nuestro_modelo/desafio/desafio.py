# -*- coding: utf-8 -*-
# Importación de bibliotecas necesarias
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns
import matplotlib.pyplot as plt

# --- Carga de Datos ---
# Asegúrate de que la ruta al archivo sea la correcta
ruta_dataset = r'Data_Science_probando_relaciones_con_regresión _ineal\\Investigando_nuestro_modelo\\desafio\\usina.csv'

try:
    df_usina = pd.read_csv(ruta_dataset)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta '{ruta_dataset}'")
    exit()

# --- Cálculo del VIF ---
print("--- Verificación de Multicolinealidad (VIF) ---")

# 1. Separar las variables predictoras (X) de la variable objetivo (y)
# PE (Producción de Energía) es la variable objetivo
X = df_usina[['AT', 'V', 'AP', 'RH']]
y = df_usina['PE']

# 2. Crear una serie para almacenar los resultados del VIF
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

print(vif_data)

# -*- coding: utf-8 -*-
# Importación de las bibliotecas necesarias
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# --- 1. Carga de Datos ---
# Asegúrate de que la ruta al archivo sea la correcta.
# Esta ruta se basa en la estructura de tus carpetas mencionada anteriormente.
ruta_dataset = r'Data_Science_probando_relaciones_con_regresión _ineal\Agregando_otros_factores\desafio\hoteis.csv'

try:
    # Cargar el dataset en un DataFrame de pandas
    df_hoteles = pd.read_csv(ruta_dataset)
    print("Dataset de hoteles cargado correctamente.")
    print(df_hoteles.head())
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta '{ruta_dataset}'")
    # Salir del script si el archivo no se encuentra
    exit()

# --- 2. Creación del Modelo 1 (Regresión Lineal Simple) ---
# Este modelo predice el precio basándose únicamente en la cantidad de estrellas.
# Es un buen punto de partida para entender la relación más básica.
print("\n--- Construyendo Modelo 1: Simple (Precio ~ Estrellas) ---")

# La fórmula 'Preco ~ Estrelas' define que 'Preco' es la variable dependiente
# y 'Estrelas' es la variable independiente.
modelo_1 = smf.ols(formula='Preco ~ Estrelas', data=df_hoteles)

# Ajustamos (entrenamos) el modelo con los datos.
resultado_1 = modelo_1.fit()

# Imprimimos la tabla de resumen con todas las métricas del modelo.
print(resultado_1.summary())


# --- 3. Creación del Modelo 2 (Regresión Lineal Múltiple) ---
# Este modelo utiliza todas las variables disponibles para predecir el precio.
# Busca capturar una mayor complejidad de los factores que influyen en el precio.
print("\n--- Construyendo Modelo 2: Múltiple (Precio ~ Todas las variables) ---")

# La fórmula ahora incluye todas las variables predictoras, separadas por '+'.
formula_multiple = 'Preco ~ Estrelas + ProximidadeTurismo + Capacidade'
modelo_2 = smf.ols(formula=formula_multiple, data=df_hoteles)

# Ajustamos el modelo múltiple.
resultado_2 = modelo_2.fit()

# Imprimimos el resumen completo del segundo modelo.
print(resultado_2.summary())

# -*- coding: utf-8 -*-
# Importación de las bibliotecas de visualización
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Se asume que las siguientes variables ya existen de tu código anterior:
# - resultado_2: El modelo múltiple ya ajustado ('Preco ~ Estrelas + ...').
# - df_hoteles: El DataFrame con los datos.

# --- 1. Obtener los Residuos y Valores Predichos ---

# Los residuos son la diferencia entre el valor real y el valor predicho.
residuos = resultado_2.resid

# Los valores predichos son los valores que el modelo estimó.
valores_predichos = resultado_2.fittedvalues

# --- 2. Crear el Gráfico de Residuos ---

# Creamos una figura de dispersión con Plotly Express.
# Eje X: Valores predichos por el modelo.
# Eje Y: Residuos correspondientes a cada predicción.
fig = px.scatter(
    x=valores_predichos, 
    y=residuos,
    title='Gráfico de Residuos vs. Valores Predichos (Modelo 2)',
    labels={'x': 'Valores Predichos', 'y': 'Residuos'}
)

# Añadimos una línea horizontal roja en y=0. Esta es nuestra línea de referencia.
fig.add_hline(y=0, line_dash="dash", line_color="red")

# Centramos el título para una mejor estética.
fig.update_layout(title_x=0.5)

# Mostrar el gráfico interactivo.
fig.show()