# -*- coding: utf-8 -*-
# Paso 0: Importar todas las bibliotecas necesarias
# ----------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Modelos a entrenar
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Métricas de evaluación
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    RocCurveDisplay,
    PrecisionRecallDisplay,
    average_precision_score,
    auc,
    roc_curve
)

# ----------------------------------------------------
# Paso 1: Carga y Preparación de los Datos
# ----------------------------------------------------
# Define la ruta del archivo CSV. ¡Asegúrate de que esta ruta sea correcta!
ruta_archivo = r'Clasificación_validación_de_modelos_y_métricas_de_evaluación\Métricas_de_evaluación\desafio\diabetes(1).csv'

# Cargar los datos en un DataFrame de pandas
try:
    df = pd.read_csv(ruta_archivo)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta '{ruta_archivo}'.")
    print("Por favor, verifica que la ruta y el nombre del archivo sean correctos.")
    exit() # Termina el script si no se encuentra el archivo

# Usamos la lista de 6 columnas que coincide con tu archivo CSV.
df.columns = ['glicemia', 'presion_sanguinea', 'grasa_subcutanea_triceps', 
              'insulina', 'imc', 'diabetes']

# Separar las características (X) y la variable objetivo (y)
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# Dividir los datos en conjuntos de entrenamiento (80%) y prueba (20%)
# Usamos random_state para que la división sea siempre la misma y los resultados reproducibles.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42,
    stratify=y # Estratificar para mantener la proporción de clases en ambos conjuntos
)

# ----------------------------------------------------
# Paso 2: Entrenar los Modelos de Clasificación
# ----------------------------------------------------
# Crearemos un diccionario para almacenar nuestros modelos entrenados
# Esto facilitará iterar sobre ellos para la evaluación.
modelos = {
    'Regresión Logística': LogisticRegression(max_iter=1000, random_state=42),
    'Árbol de Decisión': DecisionTreeClassifier(random_state=42),
    'Bosque Aleatorio': RandomForestClassifier(random_state=42)
}

# Entrenar cada modelo con los datos de entrenamiento
print("Entrenando los modelos...")
for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    print(f"✅ Modelo '{nombre}' entrenado.")

print("\n--- INICIO DE LA EVALUACIÓN ---\n")

# ----------------------------------------------------
# Desafío 1: Métricas de Precisión, Recall y F1-Score
# ----------------------------------------------------
print("="*60)
print("DESAFÍO 1: MÉTRICAS DE CLASIFICACIÓN INDIVIDUALES")
print("="*60)

# Iteramos sobre cada modelo entrenado para calcular y mostrar sus métricas
for nombre, modelo in modelos.items():
    # Realizar predicciones con los datos de prueba
    y_pred = modelo.predict(X_test)
    
    # Calcular las métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Imprimir los resultados de forma clara
    print(f"\n métricas para el modelo: {nombre}")
    print(f"  - Accuracy (Exactitud General): {accuracy:.4f}")
    print(f"  - Precision (Precisión):        {precision:.4f}")
    print(f"  - Recall (Sensibilidad):        {recall:.4f}")
    print(f"  - F1-Score:                     {f1:.4f}")

# ----------------------------------------------------
# Desafío 2: Curva ROC y Métrica AUC
# ----------------------------------------------------
print("\n" + "="*60)
print("DESAFÍO 2: CURVA ROC Y AUC")
print("="*60)

# Crear una figura de matplotlib para plotear todas las curvas juntas
fig, ax = plt.subplots(figsize=(10, 8))

# Iterar sobre los modelos para dibujar cada curva ROC
for nombre, modelo in modelos.items():
    # RocCurveDisplay.from_estimator es una forma conveniente de generar
    # la predicción de probabilidad y la curva en un solo paso.
    RocCurveDisplay.from_estimator(modelo, X_test, y_test, name=nombre, ax=ax)

# Dibujar la línea de referencia (un clasificador aleatorio)
ax.plot([0, 1], [0, 1], 'k--', label='Clasificador Aleatorio')

# Personalizar el gráfico
plt.title('Curva ROC Comparativa de Modelos')
plt.xlabel('Tasa de Falsos Positivos (FPR)')
plt.ylabel('Tasa de Verdaderos Positivos (TPR)')
plt.legend()
plt.grid(True)
plt.show()

print("📈 Gráfico de Curva ROC generado.")

# ----------------------------------------------------
# Desafío 3: Curva Precisión vs. Recall y AP
# ----------------------------------------------------
print("\n" + "="*60)
print("DESAFÍO 3: CURVA PRECISIÓN-RECALL Y AVERAGE PRECISION (AP)")
print("="*60)

# Crear otra figura para la curva de Precisión-Recall
fig, ax = plt.subplots(figsize=(10, 8))

# Iterar sobre los modelos
for nombre, modelo in modelos.items():
    # Obtener la puntuación de "Average Precision" (AP) que resume la curva
    y_prob = modelo.predict_proba(X_test)[:, 1]
    ap_score = average_precision_score(y_test, y_prob)
    
    # Mostrar la curva usando PrecisionRecallDisplay.from_estimator
    # y añadir la puntuación AP a la leyenda.
    display_label = f'{nombre} (AP = {ap_score:.2f})'
    PrecisionRecallDisplay.from_estimator(modelo, X_test, y_test, name=display_label, ax=ax)

# Personalizar el gráfico
plt.title('Curva Precisión-Recall Comparativa de Modelos')
plt.xlabel('Recall (Sensibilidad)')
plt.ylabel('Precision (Precisión)')
plt.legend()
plt.grid(True)
plt.show()

print("📈 Gráfico de Curva Precisión-Recall generado.")


# ----------------------------------------------------
# Desafío 4: Informe de Clasificación (Classification Report)
# ----------------------------------------------------
print("\n" + "="*60)
print("DESAFÍO 4: INFORME COMPLETO DE CLASIFICACIÓN")
print("="*60)

# Iterar sobre los modelos para generar un informe completo para cada uno
for nombre, modelo in modelos.items():
    # Realizar predicciones
    y_pred = modelo.predict(X_test)
    
    # Generar el informe
    reporte = classification_report(y_test, y_pred, target_names=['No Diabético', 'Diabético'])
    
    # Imprimir el informe
    print(f"\n--- Informe para el modelo: {nombre} ---\n")
    print(reporte)

print("\n--- FIN DE LA EVALUACIÓN ---")

