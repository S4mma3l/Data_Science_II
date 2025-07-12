import pandas as pd

datos = pd.read_csv('Clasificación_validación_de_modelos_y_métricas_de_evaluación\\Clasificando_datos\\desafio\\diabetes.csv')

print(datos.head())
print(datos.columns)

# -*- coding: utf-8 -*-
# =============================================================================
# IMPORTACIÓN DE BIBLIOTECAS
# =============================================================================
# Se importan las herramientas necesarias para el análisis.

# pandas: esencial para leer y manipular los datos (nuestro archivo CSV).
import pandas as pd

# scikit-learn: la biblioteca principal para machine learning en Python.
from sklearn.model_selection import train_test_split  # Para dividir los datos en conjuntos.
from sklearn.tree import DecisionTreeClassifier       # Algoritmo de Árbol de Decisión.
from sklearn.ensemble import RandomForestClassifier   # Algoritmo de Bosque Aleatorio.
from sklearn.metrics import confusion_matrix          # Para crear la matriz de confusión.

# seaborn y matplotlib: para crear gráficos y visualizaciones atractivas.
import seaborn as sns
import matplotlib.pyplot as plt

# =============================================================================
# DESAFÍO 1: LECTURA Y SEPARACIÓN DE DATOS (X e y)
# =============================================================================
print("--- 🚀 Iniciando Desafío 1: Lectura y Separación de Datos ---")

# Define la ruta donde se encuentra tu archivo.
# ¡Asegúrate de que 'diabetes.csv' esté en la misma carpeta que este script!
ruta_archivo = 'Clasificación_validación_de_modelos_y_métricas_de_evaluación\\Clasificando_datos\\desafio\\diabetes.csv'

# Lee el archivo CSV y lo carga en un DataFrame de pandas.
# Un DataFrame es como una tabla o una hoja de cálculo.
datos = pd.read_csv(ruta_archivo)

# Separa los datos en variables explicativas (X) y variable objetivo (y).
# La variable objetivo (y) es la columna que queremos predecir: 'diabetes'.
# Las variables explicativas (X) son todas las demás columnas que nos ayudarán a predecir.

# Para obtener X, eliminamos la columna 'diabetes' del DataFrame.
# El parámetro 'axis=1' le dice a pandas que estamos eliminando una columna.
X = datos.drop('diabetes', axis=1)

# Para obtener y, seleccionamos únicamente la columna 'diabetes'.
y = datos['diabetes']

# Imprimimos las primeras 5 filas de cada conjunto para verificar que la separación fue exitosa.
print("\n📋 Primeras 5 filas de las variables explicativas (X):")
print(X.head())
print("\n🎯 Primeras 5 filas de la variable objetivo (y):")
print(y.head())
print("--- ✅ Desafío 1 Completado ---\n")


# =============================================================================
# DESAFÍO 2: DIVISIÓN EN ENTRENAMIENTO, VALIDACIÓN Y PRUEBA
# =============================================================================
print("--- 🚀 Iniciando Desafío 2: División de Datos ---")

# Se definen los porcentajes para cada conjunto de datos.
porcentaje_prueba = 0.05      # 5% para el conjunto de prueba final.
porcentaje_validacion = 0.25  # 25% del resto se usará para validación.

# PRIMERA DIVISIÓN: Separamos el conjunto de prueba (5%) del resto (95%).
# 'X_resto' y 'y_resto' contendrán el 95% de los datos para entrenar y validar.
# 'X_prueba' y 'y_prueba' se guardan para el final, para una evaluación imparcial.
# El parámetro 'stratify=y' es MUY IMPORTANTE: asegura que la proporción de pacientes
# con y sin diabetes sea la misma en los nuevos conjuntos que en el original.
# 'random_state=42' es una semilla para que la división sea siempre la misma si
# ejecutas el código varias veces. Esto hace que tus resultados sean reproducibles.
X_resto, X_prueba, y_resto, y_prueba = train_test_split(
    X, y,
    test_size=porcentaje_prueba,
    random_state=42,
    stratify=y
)

# SEGUNDA DIVISIÓN: Del 95% restante, separamos entrenamiento y validación.
# 'X_entrenamiento' y 'y_entrenamiento' serán el 75% del 95% original (para entrenar).
# 'X_validacion' y 'y_validacion' serán el 25% del 95% original (para validar).
# De nuevo, usamos 'stratify' para mantener las proporciones.
X_entrenamiento, X_validacion, y_entrenamiento, y_validacion = train_test_split(
    X_resto, y_resto,
    test_size=porcentaje_validacion,
    random_state=42,
    stratify=y_resto
)

# Imprimimos las dimensiones (filas, columnas) de cada conjunto para verificar los tamaños.
print(f"Dimensiones de X (original): {X.shape}")
print(f"Dimensiones de y (original): {y.shape}\n")
print(f"Dimensiones de X_entrenamiento: {X_entrenamiento.shape} (para entrenar el modelo)")
print(f"Dimensiones de X_validacion:   {X_validacion.shape} (para validar y ajustar)")
print(f"Dimensiones de X_prueba:        {X_prueba.shape} (para la prueba final)")
print("--- ✅ Desafío 2 Completado ---\n")


# =============================================================================
# DESAFÍO 3: CREACIÓN Y EVALUACIÓN DE MODELOS
# =============================================================================
print("--- 🚀 Iniciando Desafío 3: Creación y Evaluación de Modelos ---")

# --- Modelo 1: Decision Tree Classifier (Árbol de Decisión) ---
# Creamos una instancia del modelo.
# 'max_depth=3' limita la profundidad del árbol a 3 niveles. Esto ayuda a
# prevenir el "sobreajuste" (que el modelo memorice los datos en lugar de aprender patrones).
modelo_arbol = DecisionTreeClassifier(max_depth=3, random_state=42)

# Entrenamos el modelo con los datos de entrenamiento.
# El método .fit() es el que realiza el aprendizaje.
modelo_arbol.fit(X_entrenamiento, y_entrenamiento)

# Evaluamos la precisión (accuracy) del modelo.
# .score() calcula el porcentaje de predicciones correctas.
acc_entrenamiento_arbol = modelo_arbol.score(X_entrenamiento, y_entrenamiento)
acc_validacion_arbol = modelo_arbol.score(X_validacion, y_validacion)

print("--- 🌳 Resultados del Decision Tree ---")
print(f"Precisión en Entrenamiento: {acc_entrenamiento_arbol:.2%}")
print(f"Precisión en Validación:    {acc_validacion_arbol:.2%}\n")


# --- Modelo 2: Random Forest Classifier (Bosque Aleatorio) ---
# Creamos una instancia del modelo. Un Random Forest es un conjunto de muchos árboles de decisión.
# 'max_depth=2' limita la profundidad de cada árbol en el bosque.
modelo_random_forest = RandomForestClassifier(max_depth=2, random_state=42)

# Entrenamos el modelo.
modelo_random_forest.fit(X_entrenamiento, y_entrenamiento)

# Evaluamos su precisión.
acc_entrenamiento_rf = modelo_random_forest.score(X_entrenamiento, y_entrenamiento)
acc_validacion_rf = modelo_random_forest.score(X_validacion, y_validacion)

print("--- 🌲🌲 Resultados del Random Forest ---")
print(f"Precisión en Entrenamiento: {acc_entrenamiento_rf:.2%}")
print(f"Precisión en Validación:    {acc_validacion_rf:.2%}")
print("--- ✅ Desafío 3 Completado ---\n")


# =============================================================================
# DESAFÍO 4: MATRIZ DE CONFUSIÓN
# =============================================================================
print("--- 🚀 Iniciando Desafío 4: Matriz de Confusión ---")

# --- Matriz para el Decision Tree ---
# 1. El modelo ya entrenado realiza predicciones sobre los datos de validación.
predicciones_arbol = modelo_arbol.predict(X_validacion)
# 2. Comparamos los valores reales ('y_validacion') con las predicciones para crear la matriz.
matriz_arbol = confusion_matrix(y_validacion, predicciones_arbol)

# --- Matriz para el Random Forest ---
# 1. Hacemos lo mismo con el segundo modelo.
predicciones_rf = modelo_random_forest.predict(X_validacion)
# 2. Calculamos su matriz de confusión.
matriz_rf = confusion_matrix(y_validacion, predicciones_rf)

# --- Visualización de las Matrices ---
# Creamos una figura que contendrá dos gráficos (1 fila, 2 columnas) para compararlos.
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Matrices de Confusión (Evaluadas con Datos de Validación)', fontsize=16)

# Gráfico para la matriz del Decision Tree
sns.heatmap(matriz_arbol, annot=True, fmt='d', cmap='Blues', ax=axes[0],
            xticklabels=['No Diabetes', 'Diabetes'], yticklabels=['No Diabetes', 'Diabetes'])
axes[0].set_title('Modelo: Decision Tree')
axes[0].set_xlabel('Predicción del Modelo')
axes[0].set_ylabel('Valor Real')

# Gráfico para la matriz del Random Forest
sns.heatmap(matriz_rf, annot=True, fmt='d', cmap='Greens', ax=axes[1],
            xticklabels=['No Diabetes', 'Diabetes'], yticklabels=['No Diabetes', 'Diabetes'])
axes[1].set_title('Modelo: Random Forest')
axes[1].set_xlabel('Predicción del Modelo')
axes[1].set_ylabel('Valor Real')

# Ajustamos el diseño y mostramos el gráfico.
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

print("📊 Visualización de matrices de confusión generada.")
print("--- ✅ Desafío 4 Completado ---")

# ==================================================