# -*- coding: utf-8 -*-
# ======================================================================
# PASO 0: IMPORTAR BIBLIOTECAS Y PREPARAR DATOS
# ======================================================================
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Modelos y herramientas de Scikit-learn
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

# Herramientas de Imbalanced-learn para balanceo y pipelines
# ¡Asegúrate de tener instalada la biblioteca: pip install imbalanced-learn!
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss

# ----------------------------------------------------------------------
# Carga de datos
# ----------------------------------------------------------------------
ruta_archivo = r'Clasificación_validación_de_modelos_y_métricas_de_evaluación\Validación_cruzada\desafio\diabetes(1).csv'

try:
    df = pd.read_csv(ruta_archivo)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo de datos en la ruta '{ruta_archivo}'.")
    exit()

X = df.drop('diabetes', axis=1)
y = df['diabetes'].astype(int)

# --- División en Entrenamiento y Prueba ---
# Este es un paso CRÍTICO. Separamos un 25% de los datos para la prueba final.
# TODO el análisis, validación cruzada y balanceo se hará SOLO en el conjunto de entrenamiento.
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y  # Estratificar para mantener la proporción de clases en ambos conjuntos
)

print("✅ Datos cargados y divididos en conjuntos de entrenamiento y prueba.")
print(f"Tamaño del conjunto de entrenamiento: {len(X_train)} registros.")
print(f"Tamaño del conjunto de prueba: {len(X_test)} registros.")
print("\n--- INICIO DE LA EVALUACIÓN ---\n")


# ======================================================================
# DESAFÍO 1: VERIFICAR EL DESBALANCE DE DATOS
# ======================================================================
print("="*60)
print("DESAFÍO 1: ANÁLISIS DEL DESBALANCE EN LA VARIABLE OBJETIVO")
print("="*60)

# Se calcula el porcentaje de cada clase en el conjunto de entrenamiento.
proporcion = y_train.value_counts(normalize=True) * 100
print("Porcentaje de cada clase en el conjunto de entrenamiento:")
print(proporcion)
print("\nSe observa un claro desbalance: la clase '0' (No Diabético) es mucho más frecuente que la clase '1' (Diabético).\n")

# Se genera un gráfico de conteo para visualizar el desbalance.
plt.figure(figsize=(8, 6))
sns.countplot(x=y_train, palette='viridis')
plt.title('Distribución de Clases en la Variable Objetivo (Diabetes)')
plt.xlabel('Clase (0: No Diabético, 1: Diabético)')
plt.ylabel('Cantidad de Registros')
plt.show()


# ======================================================================
# DESAFÍO 2: PIPELINE CON OVERSAMPLING (SMOTE)
# ======================================================================
print("\n" + "="*60)
print("DESAFÍO 2: VALIDACIÓN CRUZADA CON PIPELINE Y OVERSAMPLING (SMOTE)")
print("="*60)

# Se definen los modelos a evaluar.
modelos = {
    'Regresión Logística': LogisticRegression(max_iter=1000, random_state=42),
    'Árbol de Decisión': DecisionTreeClassifier(random_state=42),
    'Bosque Aleatorio': RandomForestClassifier(random_state=42)
}

# Almacenaremos los resultados para elegir al mejor al final.
resultados_f1 = {}

# Se define la estrategia de validación cruzada.
cv_stratified = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for nombre, modelo in modelos.items():
    # Se crea un pipeline que primero aplica SMOTE y luego ajusta el modelo.
    # Esto asegura que SMOTE se aplique solo a los datos de entrenamiento de cada fold.
    pipeline_smote = Pipeline([
        ('smote', SMOTE(random_state=42)),
        ('modelo', modelo)
    ])
    
    # Se evalúa el pipeline usando validación cruzada y la métrica F1-Score.
    score_f1 = cross_val_score(pipeline_smote, X_train, y_train, cv=cv_stratified, scoring='f1').mean()
    
    # Se guardan y se imprimen los resultados.
    resultados_f1[f'{nombre} con SMOTE'] = score_f1
    print(f"F1-Score medio para {nombre} con SMOTE: {score_f1:.4f}")


# ======================================================================
# DESAFÍO 3: PIPELINE CON UNDERSAMPLING (NearMiss)
# ======================================================================
print("\n" + "="*60)
print("DESAFÍO 3: VALIDACIÓN CRUZADA CON PIPELINE Y UNDERSAMPLING (NearMiss)")
print("="*60)

for nombre, modelo in modelos.items():
    # Se crea un pipeline que primero aplica NearMiss y luego ajusta el modelo.
    # NearMiss reduce el número de muestras de la clase mayoritaria.
    pipeline_nearmiss = Pipeline([
        ('nearmiss', NearMiss(version=3)),
        ('modelo', modelo)
    ])
    
    # Se evalúa el pipeline.
    score_f1 = cross_val_score(pipeline_nearmiss, X_train, y_train, cv=cv_stratified, scoring='f1').mean()
    
    # Se guardan y se imprimen los resultados.
    resultados_f1[f'{nombre} con NearMiss'] = score_f1
    print(f"F1-Score medio para {nombre} con NearMiss: {score_f1:.4f}")


# ======================================================================
# DESAFÍO 4: SELECCIÓN Y EVALUACIÓN FINAL DEL MEJOR MODELO
# ======================================================================
print("\n" + "="*60)
print("DESAFÍO 4: SELECCIÓN Y EVALUACIÓN FINAL DEL MEJOR MODELO")
print("="*60)

# Se elige la mejor estrategia y modelo basado en el F1-Score más alto.
mejor_estrategia = max(resultados_f1, key=resultados_f1.get)
mejor_puntuacion = resultados_f1[mejor_estrategia]

print(f"🏆 La mejor combinación fue: '{mejor_estrategia}' con un F1-Score de {mejor_puntuacion:.4f}\n")

# ---- Re-crear y entrenar el pipeline ganador con todos los datos de ENTRENAMIENTO ----
# Se extrae el nombre del modelo y la estrategia del texto.
nombre_modelo_ganador = mejor_estrategia.split(' con ')[0]
estrategia_ganadora = mejor_estrategia.split(' con ')[1]

modelo_final = modelos[nombre_modelo_ganador]
pipeline_final = None

if estrategia_ganadora == 'SMOTE':
    pipeline_final = Pipeline([
        ('smote', SMOTE(random_state=42)),
        ('modelo', modelo_final)
    ])
else: # NearMiss
    pipeline_final = Pipeline([
        ('nearmiss', NearMiss(version=3)),
        ('modelo', modelo_final)
    ])

# Se entrena el pipeline ganador con TODO el conjunto de entrenamiento.
print(f"Entrenando el pipeline final: {mejor_estrategia}...")
pipeline_final.fit(X_train, y_train)
print("Modelo final entrenado.\n")

# ---- Evaluación en el conjunto de PRUEBA (datos nunca antes vistos) ----
print("--- Evaluación Final en el Conjunto de Prueba ---")
predicciones_finales = pipeline_final.predict(X_test)

# Se genera y se imprime el informe de clasificación.
print("\nInforme de Métricas:")
print(classification_report(y_test, predicciones_finales, target_names=['No Diabético', 'Diabético']))

# Se genera y se muestra la matriz de confusión.
print("Matriz de Confusión:")
ConfusionMatrixDisplay.from_estimator(pipeline_final, X_test, y_test, cmap='Blues', values_format='d')
plt.title(f'Matriz de Confusión para\n{mejor_estrategia}')
plt.show()

print("\n--- FIN DEL PROYECTO ---")