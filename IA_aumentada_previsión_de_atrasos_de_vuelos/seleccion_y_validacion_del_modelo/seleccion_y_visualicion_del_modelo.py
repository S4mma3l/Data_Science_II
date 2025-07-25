import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import yellowbrick
import matplotlib.pyplot as plt


# --- Tu código anterior (sin cambios) ---
datos = pd.read_csv('IA_aumentada_previsión_de_atrasos_de_vuelos\\explorando_los_datos\\datos\\flights.csv')
print(f'Número de filas en el DataFrame: {datos.shape[0]}')
print(datos.head())
print(datos.info())
print(datos.describe(include='O'))

# --- CORRECCIÓN EN LA FUNCIÓN ancho_bins ---
def ancho_bins(df, columna):
    # Asegúrate de que la columna sea numérica y maneja NaNs.
    # Convertimos la Serie a un arreglo de NumPy y eliminamos NaNs.
    col_data = df[columna].dropna().to_numpy() # Convertir a NumPy array y eliminar NaNs
    
    # Asegurarse de que haya suficientes datos para calcular percentiles
    if len(col_data) < 2: # Necesitamos al menos dos puntos para un rango
        print(f"Advertencia: No hay suficientes datos numéricos en la columna '{columna}' para calcular el ancho de bin. Usando un valor por defecto.")
        return 5 # Valor por defecto si no hay suficientes datos
        
    q75, q25 = np.percentile(col_data, [75, 25])
    iqr = q75 - q25
    
    # Manejar el caso donde IQR es cero (todos los valores son iguales)
    if iqr == 0:
        print(f"Advertencia: El rango intercuartílico (IQR) para la columna '{columna}' es cero. Usando un valor por defecto para el ancho de bin.")
        return 5 # Otro valor por defecto, o puedes elegir 1 si prefieres bins de tamaño 1 para valores discretos
    
    ancho = 2 * iqr * np.power(len(col_data), -1/3)
    return ancho

atraso_promedio = datos['delay'].mean()
atraso_mediana = datos['delay'].median()

print(datos.columns)

datos['date'] = datos['year'].astype(str) + '-' + (datos['day']+1).astype(str)
datos['date'] = pd.to_datetime(datos['date'], format='%Y-%j')
print(datos.head(2))

datos['is_weekend'] = datos['date'].dt.weekday.isin([5, 6])
datos['day_name'] = datos['date'].dt.day_name()
print(datos.sample(5))
print(datos.info())

import warnings
warnings.filterwarnings('ignore')

datos['schengen'] = datos['schengen'].replace({'schengen':1, 'non-schengen':0})
datos['is_holiday'] = datos['is_holiday'].replace({True :1 , False :0})
datos['is_weekend'] = datos['is_weekend'].replace({True :1 , False :0})

print(datos.sample(5))

categoricas = ['airline', 'aircraft_type', 'origin', 'day_name']

datos_codificados = pd.get_dummies(datos, columns=categoricas, dtype=int)
print(datos_codificados.sample(5))

# Limpieza de datos
print(datos[['arrival_time', 'departure_time']].corr())

df = datos_codificados.drop(columns=['flight_id', 'departure_time', 'day', 'year', 'date'])
print(df.sample(10))

# creacion de baseline

from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split

X = df.drop(columns=['delay'], axis=1)
y = df['delay']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

baseline = DummyRegressor()
baseline.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_pred_dummy = baseline.predict(X_test)

def calcular_regresion(y_test, y_pred):
    rmse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    metricas = {
        'RMSE': round(rmse**(1/2),4),
        'MAE': round(mae,4),
        'R2': round(r2,4)
    }
    return metricas

resultados_baseline = calcular_regresion(y_test, y_pred_dummy)
print("Resultados Baseline:")
print(resultados_baseline)

# uso de ramdom forest
from sklearn.ensemble import RandomForestRegressor

modelo = RandomForestRegressor( random_state=42, max_depth=5)
modelo.fit(X_train, y_train)
ypred = modelo.predict(X_test)
resultados_rf = calcular_regresion(y_test, ypred)
print("Resultados Random Forest:")
print(resultados_rf)

from yellowbrick.regressor import PredictionError
# visualizer = PredictionError(modelo, X_train, y_train, X_test=X_test, y_test=y_test) # Esta línea se ejecuta después de ResidualsPlot
from yellowbrick.regressor import ResidualsPlot
# viz = ResidualsPlot(modelo, X_train, y_train, X_test=X_test, y_test=y_test) # Esta línea se ejecuta después de PredictionError

# --- Aquí tu código de visualización de los gráficos de Matplotlib/Seaborn ---
# Asumo que esta parte viene justo después de la definición de tus métricas y modelos.
# Necesitas inicializar 'fig' y 'ax' correctamente aquí
fig, ax = plt.subplots(1, 2, figsize=(14, 6)) # 1 fila, 2 columnas para tus gráficos

# --- Boxplot ---
sns.boxplot(data=datos, y='delay', ax=ax[0])
ax[0].set_title('Boxplot de Atrasos')
ax[0].set_ylabel('Atraso (minutos)')
ax[0].axhline(y=atraso_promedio, color='r', linestyle='--', label=f'Atraso Promedio ({atraso_promedio:.2f})')
ax[0].legend()
ax[0].grid(axis='y', linestyle='--', alpha=0.7)

# --- Histograma ---
binwidth = ancho_bins(datos, 'delay') # Aquí se llama a la función corregida
sns.histplot(data=datos, x='delay', binwidth=binwidth, kde=True, ax=ax[1])
ax[1].set_ylabel('Número de vuelos')
ax[1].set_title('Histograma de Atrasos')
ax[1].set_xlabel('Atraso (minutos)')
ax[1].axvline(x=atraso_promedio, color='r', linestyle='--', label=f'Atraso Promedio ({atraso_promedio:.2f})')
ax[1].axvline(x=atraso_mediana, color='g', linestyle='--', label=f'Atraso Mediano ({atraso_mediana:.2f})')
ax[1].legend()
ax[1].grid(False)

plt.tight_layout()
plt.show()

# --- Visualizadores de Yellowbrick (si los quieres mostrar) ---
# Tienes que llamar a .show() en cada visualizador si quieres que se muestre.
# Y generalmente se muestran en ventanas separadas o en subplots específicos.
# Si los ejecutas sin .show(), simplemente se crean los objetos pero no se visualizan.
# Si quieres verlos, puedes descomentar y llamar a .show()
# visualizer = PredictionError(modelo, X_train, y_train, X_test=X_test, y_test=y_test)
# visualizer.show()

# viz = ResidualsPlot(modelo, X_train, y_train, X_test=X_test, y_test=y_test)
# viz.show()


# --- Realizando Cross Validation (tu código original) ---
from sklearn.model_selection import KFold, cross_validate

scoring = {
    'RMSE': 'neg_root_mean_squared_error',
    'MAE': 'neg_mean_absolute_error',
    'R2': 'r2',
}

cv = KFold(n_splits=5, shuffle=True, random_state=42)
cv_results = cross_validate(modelo, X_train, y_train, cv=cv, scoring=scoring)
print("Resultados de Cross Validation:")
print(cv_results)