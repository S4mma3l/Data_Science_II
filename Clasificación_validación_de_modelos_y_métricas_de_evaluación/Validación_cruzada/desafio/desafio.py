# -*- coding: utf-8 -*-
# ======================================================================
# PASO 0: IMPORTAR TODAS LAS BIBLIOTECAS NECESARIAS
# ======================================================================
import pandas as pd
import numpy as np  # Necesario para cálculos de media y desviación estándar

# Modelos a entrenar
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Métodos de validación cruzada y la función para ejecutarla
from sklearn.model_selection import (
    cross_val_score,
    KFold,
    StratifiedKFold,
    LeaveOneOut
)

# ======================================================================
# PASO 1: CARGA Y PREPARACIÓN DE LOS DATOS (VERSIÓN CORREGIDA)
# ======================================================================

# Define la ruta del archivo CSV. ¡Asegúrate de que esta ruta sea correcta!
ruta_archivo = r'Clasificación_validación_de_modelos_y_métricas_de_evaluación\Validación_cruzada\desafio\diabetes(1).csv'

try:
    # --- CORRECCIÓN CLAVE ---
    # Se quita `header=None` para que Pandas lea la primera fila del
    # archivo como los nombres de las columnas, que es el comportamiento correcto.
    df = pd.read_csv(ruta_archivo)
    
except FileNotFoundError:
    print(f"Error: No se encontró el archivo de datos en la ruta '{ruta_archivo}'.")
    print("Por favor, verifica que la ruta y el nombre del archivo CSV sean correctos.")
    exit()

# La línea `df.columns = [...]` se elimina porque ya no es necesaria.

# Separar las características (X) y la variable objetivo (y)
# Para la validación cruzada, usamos el conjunto de datos completo.
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# Se asegura que la columna objetivo sea de tipo numérico (entero).
# Esto previene errores de tipo de dato ('0' vs 0) en algunas métricas.
y = y.astype(int)


# Instanciar los modelos que vamos a evaluar
modelos = {
    'Regresión Logística': LogisticRegression(max_iter=1000, random_state=42),
    'Árbol de Decisión': DecisionTreeClassifier(random_state=42),
    'Bosque Aleatorio': RandomForestClassifier(random_state=42)
}

print("✅ Datos cargados y modelos listos para la validación cruzada.")
print("\n--- INICIO DE LA EVALUACIÓN ---\n")


# ======================================================================
# DESAFÍO 1: FUNCIÓN PARA CALCULAR EL INTERVALO DE CONFIANZA
# ======================================================================
print("="*60)
print("DESAFÍO 1: FUNCIÓN DE INTERVALO DE CONFIANZA")
print("="*60)

def calcula_intervalo_confianza(resultados_metricas, nombre_modelo):
    """
    Calcula e imprime el intervalo de confianza (con 2 desviaciones estándar)
    para una lista de resultados de métricas.
    """
    media = np.mean(resultados_metricas)
    desvio_estandar = np.std(resultados_metricas)
    limite_inferior = media - (2 * desvio_estandar)
    limite_superior = media + (2 * desvio_estandar)
    print(f"Intervalo de confianza ({nombre_modelo}): [{limite_inferior:.4f}, {limite_superior:.4f}]")

print("Función 'calcula_intervalo_confianza' definida.")


# ======================================================================
# DESAFÍO 2: VALIDACIÓN CRUZADA CON KFOLD (10 SPLITS)
# ======================================================================
print("\n" + "="*60)
print("DESAFÍO 2: VALIDACIÓN CRUZADA CON KFOLD (Métrica: Accuracy)")
print("="*60)

# Se define la estrategia de validación KFold
kfold = KFold(n_splits=10, shuffle=True, random_state=42)

for nombre, modelo in modelos.items():
    # Se ejecuta la validación cruzada. La métrica por defecto es la exactitud (accuracy).
    resultados = cross_val_score(modelo, X, y, cv=kfold)
    calcula_intervalo_confianza(resultados, nombre)


# ======================================================================
# DESAFÍO 3: VALIDACIÓN CRUZADA CON STRATIFIEDKFOLD (Métrica F1-Score)
# ======================================================================
print("\n" + "="*60)
print("DESAFÍO 3: VALIDACIÓN CRUZADA CON STRATIFIEDKFOLD (Métrica: F1-Score)")
print("="*60)

# StratifiedKFold asegura que la proporción de clases se mantenga en cada fold.
stratified_kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

for nombre, modelo in modelos.items():
    # Se ejecuta la validación cruzada especificando `scoring='f1'`.
    resultados_f1 = cross_val_score(modelo, X, y, cv=stratified_kfold, scoring='f1')
    calcula_intervalo_confianza(resultados_f1, nombre)


# ======================================================================
# DESAFÍO 4: VALIDACIÓN CRUZADA CON LEAVEONEOUT
# ======================================================================
print("\n" + "="*60)
print("DESAFÍO 4: VALIDACIÓN CRUZADA CON LEAVEONEOUT (Métrica: Accuracy)")
print("="*60)

# LeaveOneOut (LOOCV) usa cada muestra como un conjunto de prueba individual.
loocv = LeaveOneOut()

for nombre, modelo in modelos.items():
    # Se ejecuta la validación cruzada con LOOCV.
    resultados_loocv = cross_val_score(modelo, X, y, cv=loocv)
    
    # Como se pidió, solo calculamos e imprimimos la media de los resultados.
    print(f"Accuracy media con LeaveOneOut ({nombre}): {np.mean(resultados_loocv):.4f}")

print("\n--- FIN DE LA EVALUACIÓN ---")