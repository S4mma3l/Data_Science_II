import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import yellowbrick
import matplotlib.pyplot as plt
import warnings # Importar warnings al inicio para usarlo luego

# Importaciones específicas para los modelos y métricas
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split, KFold, cross_validate, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
# from yellowbrick.regressor import PredictionError, ResidualsPlot # Comentados porque no se usan directamente aquí

# --- Carga de Datos y Preprocesamiento Inicial ---
# Carga el dataset desde la ruta especificada.
datos = pd.read_csv('IA_aumentada_previsión_de_atrasos_de_vuelos\\explorando_los_datos\\datos\\flights.csv')
print(f'Número de filas en el DataFrame: {datos.shape[0]}')
print(datos.head()) # Muestra las primeras filas del DataFrame.
print(datos.info()) # Muestra información sobre el DataFrame (tipos de datos, valores no nulos).
print(datos.describe(include='O')) # Muestra estadísticas descriptivas para columnas de tipo objeto (categóricas).


# Formula para en ancho de las barras de un histograma (Regla de Freedman-Diaconis)
def ancho_bins(df, columna):
    """
    Calcula el ancho óptimo de los bins para un histograma usando la regla de Freedman-Diaconis.
    
    Args:
        df (pd.DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna para la cual calcular el ancho de bin.
        
    Returns:
        float: El ancho calculado para los bins.
    """
    # Asegúrate de que la columna sea numérica y maneja NaNs.
    # Convertimos la Serie de Pandas a un arreglo de NumPy y eliminamos NaNs.
    # Esto previene el error 'TypeError: unhashable type: 'Series'' al asegurar
    # que np.percentile trabaje con un arreglo numérico limpio.
    col_data = df[columna].dropna().to_numpy() 
    
    # Asegurarse de que haya suficientes datos para calcular percentiles.
    # Si hay menos de 2 puntos, el cálculo de percentiles no es significativo.
    if len(col_data) < 2:
        print(f"Advertencia: No hay suficientes datos numéricos en la columna '{columna}' para calcular el ancho de bin. Usando un valor por defecto.")
        return 5 # Valor por defecto si no hay suficientes datos
        
    q75, q25 = np.percentile(col_data, [75, 25])
    iqr = q75 - q25
    
    # Manejar el caso donde el Rango Intercuartílico (IQR) es cero.
    # Si IQR es 0, todos los valores son iguales y un ancho de bin basado en IQR no tiene sentido.
    if iqr == 0:
        print(f"Advertencia: El rango intercuartílico (IQR) para la columna '{columna}' es cero. Usando un valor por defecto para el ancho de bin.")
        return 5 # Otro valor por defecto, o puedes elegir 1 si prefieres bins de tamaño 1 para valores discretos
    
    ancho = 2 * iqr * np.power(len(col_data), -1/3)
    return ancho

# Calcula el atraso promedio y la mediana de la columna 'delay'.
atraso_promedio = datos['delay'].mean()
atraso_mediana = datos['delay'].median()

print(datos.columns) # Imprime los nombres de todas las columnas del DataFrame.

# Creación de la columna 'date' combinando 'year' y 'day', luego convirtiéndola a datetime.
datos['date'] = datos['year'].astype(str) + '-' + (datos['day']+1).astype(str)
datos['date'] = pd.to_datetime(datos['date'], format='%Y-%j') # %Y: año, %j: día del año (1-366)
print(datos.head(2)) # Muestra las dos primeras filas con la nueva columna 'date'.

# Crea una columna 'is_weekend' (booleana) para indicar si la fecha es fin de semana.
datos['is_weekend'] = datos['date'].dt.weekday.isin([5, 6]) # 5 es Sábado, 6 es Domingo.
# Crea una columna 'day_name' con el nombre del día de la semana.
datos['day_name'] = datos['date'].dt.day_name()
print(datos.sample(5)) # Muestra una muestra aleatoria de 5 filas.
print(datos.info()) # Muestra la información actualizada del DataFrame.

# Importa el módulo warnings para controlar la visibilidad de advertencias.
warnings.filterwarnings('ignore') # Ignora las advertencias, útil en notebooks pero úsalo con precaución.

# Reemplaza valores en columnas específicas para convertirlos a formato numérico (0 o 1).
datos['schengen'] = datos['schengen'].replace({'schengen':1, 'non-schengen':0})
datos['is_holiday'] = datos['is_holiday'].replace({True :1 , False :0})
datos['is_weekend'] = datos['is_weekend'].replace({True :1 , False :0})

print(datos.sample(5)) # Muestra una muestra aleatoria después de las conversiones.

# Define una lista de columnas categóricas para One-Hot Encoding.
categoricas = ['airline', 'aircraft_type', 'origin', 'day_name']

# Realiza One-Hot Encoding en las columnas categóricas, convirtiéndolas en columnas numéricas binarias.
datos_codificados = pd.get_dummies(datos, columns=categoricas, dtype=int)
print(datos_codificados.sample(5)) # Muestra una muestra aleatoria del DataFrame codificado.

# Limpieza de datos: muestra la correlación entre 'arrival_time' y 'departure_time'.
print(datos[['arrival_time', 'departure_time']].corr())

# Crea un nuevo DataFrame 'df' eliminando columnas que no se usarán para el modelado.
df = datos_codificados.drop(columns=['flight_id', 'departure_time', 'day', 'year', 'date'])
print(df.sample(10)) # Muestra una muestra aleatoria del DataFrame final para el modelo.

# --- Creación de Baseline ---
# Define las características (X) y la variable objetivo (y).
X = df.drop(columns=['delay'], axis=1)
y = df['delay']

# División en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializa y entrena un modelo DummyRegressor como baseline.
baseline = DummyRegressor()
baseline.fit(X_train, y_train)

# Realiza predicciones con el modelo Dummy.
y_pred_dummy = baseline.predict(X_test)

# Define una función para calcular métricas de regresión.
def calcular_regresion(y_test, y_pred):
    """
    Calcula el RMSE, MAE y R2 para las predicciones de un modelo de regresión.
    
    Args:
        y_test (pd.Series or np.array): Los valores verdaderos de la variable objetivo.
        y_pred (np.array): Las predicciones del modelo.
        
    Returns:
        dict: Un diccionario con las métricas 'RMSE', 'MAE' y 'R2'.
    """
    # CORRECCIÓN: Para compatibilidad con versiones antiguas de scikit-learn (anteriores a 0.22).
    # 'mean_squared_error' no acepta 'squared=False' en versiones antiguas.
    # Calculamos el MSE y luego la raíz cuadrada para obtener el RMSE.
    mse = mean_squared_error(y_test, y_pred) # Ahora calcula solo el MSE
    rmse = np.sqrt(mse) # Y aquí calculamos la raíz cuadrada para obtener RMSE
    
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    metricas = {
        'RMSE': round(rmse,4), # Ahora usa la variable 'rmse' calculada arriba
        'MAE': round(mae,4),
        'R2': round(r2,4)
    }
    return metricas

# Calcula y muestra los resultados del modelo baseline.
resultados_baseline = calcular_regresion(y_test, y_pred_dummy)
print("Resultados Baseline:")
print(resultados_baseline)

# --- Uso de Random Forest ---
# Inicializa y entrena un modelo RandomForestRegressor.
modelo = RandomForestRegressor(random_state=42, max_depth=5)
modelo.fit(X_train, y_train)
# Realiza predicciones con el modelo de Random Forest.
ypred = modelo.predict(X_test)
# Calcula y muestra los resultados del modelo Random Forest.
resultados_rf = calcular_regresion(y_test, ypred)
print("Resultados Random Forest:")
print(resultados_rf)

# Importa clases de Yellowbrick para visualización de errores de regresión.
# Estas líneas están comentadas porque generalmente abren ventanas de gráficos separadas.
# Para verlos, deberías descomentarlos y llamar a .show() en cada visualizador.
from yellowbrick.regressor import PredictionError
# visualizer = PredictionError(modelo, X_train, y_train, X_test=X_test, y_test=y_test)
from yellowbrick.regressor import ResidualsPlot
# viz = ResidualsPlot(modelo, X_train, y_train, X_test=X_test, y_test=y_test)

# --- Código de visualización de gráficos Matplotlib/Seaborn ---
# Crea una figura con dos subgráficos (1 fila, 2 columnas) para mostrar el boxplot y el histograma.
fig, ax = plt.subplots(1, 2, figsize=(14, 6)) 

# --- Boxplot ---
sns.boxplot(data=datos, y='delay', ax=ax[0])
ax[0].set_title('Boxplot de Atrasos') # Título para el boxplot.
ax[0].set_ylabel('Atraso (minutos)') # Etiqueta del eje Y.
# Añade una línea horizontal para el atraso promedio.
ax[0].axhline(y=atraso_promedio, color='r', linestyle='--', label=f'Atraso Promedio ({atraso_promedio:.2f})')
ax[0].legend() # Muestra la leyenda.
ax[0].grid(axis='y', linestyle='--', alpha=0.7) # Añade una cuadrícula suave en el eje Y.

# --- Histograma ---
binwidth = ancho_bins(datos, 'delay') # Calcula el ancho de los bins usando la función corregida.
sns.histplot(data=datos, x='delay', binwidth=binwidth, kde=True, ax=ax[1]) # Crea el histograma con estimación de densidad del kernel.
ax[1].set_ylabel('Número de vuelos') # Etiqueta del eje Y.
ax[1].set_title('Histograma de Atrasos') # Título para el histograma.
ax[1].set_xlabel('Atraso (minutos)') # Etiqueta del eje X.
# Añade líneas verticales para el atraso promedio y la mediana.
ax[1].axvline(x=atraso_promedio, color='r', linestyle='--', label=f'Atraso Promedio ({atraso_promedio:.2f})')
ax[1].axvline(x=atraso_mediana, color='g', linestyle='--', label=f'Atraso Mediano ({atraso_mediana:.2f})')
ax[1].legend() # Muestra la leyenda.
ax[1].grid(False) # Desactiva la cuadrícula para este subgráfico.

plt.tight_layout() # Ajusta automáticamente los subgráficos para evitar solapamientos.
# plt.show() # Muestra la figura con ambos gráficos.

# --- Visualizadores de Yellowbrick (si los quieres mostrar) ---
# Tienes que llamar a .show() en cada visualizador si quieres que se muestre.
# Y generalmente se muestran en ventanas separadas o en subplots específicos.
# Si los ejecutas sin .show(), simplemente se crean los objetos pero no se visualizan.
# Si quieres verlos, puedes descomentar y llamar a .show()
# visualizer = PredictionError(modelo, X_train, y_train, X_test=X_test, y_test=y_test)
# visualizer.show()

# viz = ResidualsPlot(modelo, X_train, y_train, X_test=X_test, y_test=y_test)
# viz.show()


# --- Realizando Cross Validation ---
# Define las métricas de scoring para la validación cruzada.
scoring = {
    # Métrica para RMSE (se usa 'neg_' porque scikit-learn maximiza las métricas).
    # No se usa 'squared=False' aquí, se asume que mean_squared_error_neg es MSE y se tomará la raíz cuadrada luego.
    'RMSE': 'neg_mean_squared_error', # CORRECCIÓN: Usar 'neg_mean_squared_error' en su lugar
    'MAE': 'neg_mean_absolute_error',     # Métrica para MAE
    'R2': 'r2',                           # Métrica para R2
}

# Configura la validación cruzada K-Fold.
cv = KFold(n_splits=5, shuffle=True, random_state=42)
# Realiza la validación cruzada y almacena los resultados.
cv_results = cross_validate(modelo, X_train, y_train, cv=cv, scoring=scoring)

# CORRECCIÓN: Para obtener RMSE y MAE positivos de los resultados de CV.
# Las métricas 'neg_root_mean_squared_error' y 'neg_mean_absolute_error' devuelven valores negativos,
# entonces se les quita el signo para mostrar el valor positivo del error.
cv_results['test_RMSE'] = np.sqrt(-cv_results['test_RMSE']) # Tomar la raíz cuadrada del MSE negativo para obtener RMSE
cv_results['test_MAE'] = -cv_results['test_MAE'] # Cambiar el signo de MAE

print("Resultados de Cross Validation:")
print(cv_results)

print(len(df.columns)) # Imprime el número de columnas en el DataFrame 'df'.

# Calcula la importancia de las características del modelo Random Forest.
importances = modelo.feature_importances_
# Crea un DataFrame con las importancias y las ordena de mayor a menor.
feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': (importances* 100).round(2)}).sort_values('Importance', ascending=False)

print("Importancias de las características:")
print(feature_importances)

# Prepara un DataFrame para almacenar los resultados de la evaluación con diferentes subconjuntos de características.
resultados = pd.DataFrame(index=['RMSE', 'MAE', 'R2'])
model_features = RandomForestRegressor(max_depth=5, random_state=42)
# Define un rango de cantidades de características a probar.
ct_features = [i if i != 0 else 1 for i in range(0,35,5)] # Asegura que al menos 1 característica sea seleccionada si i es 0

# Itera sobre las diferentes cantidades de características.
for i in ct_features:
    # Selecciona las 'i' características más importantes.
    selected_features = feature_importances['Feature'].values[:i]
    # Filtra los conjuntos de entrenamiento y prueba con las características seleccionadas.
    X_train_selected = X_train[selected_features]
    X_test_selected = X_test[selected_features]
    # Entrena el modelo con las características seleccionadas.
    model_features.fit(X_train_selected, y_train)
    # Realiza predicciones.
    y_pred_selected = model_features.predict(X_test_selected)
    # Calcula las métricas.
    metricas = calcular_regresion(y_test, y_pred_selected)
    # Almacena los resultados en el DataFrame.
    resultados[i] = list(metricas.values())

print(resultados) # Muestra los resultados.


# Repite el proceso para un rango diferente de características (10 a 14).
resultados = pd.DataFrame(index=['RMSE', 'MAE', 'R2'])
model_features = RandomForestRegressor(max_depth=5, random_state=42)
ct_features = range(10,15) # Rango de 10 a 14 características

for i in ct_features:
    selected_features = feature_importances['Feature'].values[:i]
    X_train_selected = X_train[selected_features]
    X_test_selected = X_test[selected_features]
    model_features.fit(X_train_selected, y_train)
    y_pred_selected = model_features.predict(X_test_selected)
    metricas = calcular_regresion(y_test, y_pred_selected)
    resultados[i] = list(metricas.values())

print(resultados) # Muestra los resultados para el segundo rango.

# Selecciona las 13 características más importantes para el siguiente paso (GridSearchCV).
selected_features = feature_importances['Feature'].values[:13]
X_selected_features = X[selected_features] # Crea un DataFrame con solo estas características.

print("Datos con características seleccionadas:")
print(X_selected_features) # Muestra las primeras filas del DataFrame con las características seleccionadas.

# Vuelve a dividir los datos en conjuntos de entrenamiento y prueba usando solo las características seleccionadas.
X_train, X_test, y_train, y_test = train_test_split(X_selected_features, y, random_state=42)

# --- Definición del Grid de Parámetros para GridSearchCV ---
# CORRECCIÓN: Se corrigió el nombre del parámetro 'min_samples_leaft' a 'min_samples_leaf'.
# Este era un 'ValueError: Invalid parameter' porque el nombre no era reconocido por RandomForestRegressor.
param_grip = {
    'max_depth': [5, 10, 15],
    'min_samples_leaf': [1, 2, 3], # ¡CORREGIDO! Nombre correcto del hiperparámetro.
    'min_samples_split': [2, 4, 6],
    'n_estimators': [100, 150, 200]
}

# Inicializa GridSearchCV para encontrar los mejores hiperparámetros.
# RandomState se pasa al RandomForestRegressor para reproducibilidad.
cv = KFold(n_splits=5, shuffle=True, random_state=42) # Usamos 'cv' como en tu original
model_grip = GridSearchCV(RandomForestRegressor(random_state=42),
                          param_grid=param_grip,
                          scoring='r2', # Métrica de evaluación para la búsqueda.
                          cv=cv)   # Estrategia de validación cruzada.
                          # n_jobs=-1, # Puedes descomentar esta línea si quieres usar todos los núcleos para acelerar GridSearchCV
                          # verbose=2) # Puedes descomentar esta línea para ver el progreso de GridSearchCV

# CORRECCIÓN: Llamar a .fit() solo una vez.
# La llamada a .fit() realiza la búsqueda de los mejores parámetros.
# Después de esta línea, los resultados se acceden a través de atributos como .best_params_.
model_grip.fit(X_train, y_train)

print("Mejores parámetros encontrados:")
# CORRECCIÓN: Acceder a los mejores parámetros con .best_params_ después de que model_grip.fit() haya terminado.
# No se debe llamar a .fit() de nuevo solo para imprimir los resultados.
print(model_grip.best_params_)

# CORRECCIÓN: Si deseas imprimir el objeto GridSearchCV completo después de su ajuste,
# puedes hacerlo con `print(model_grip)`. Si quieres el mejor estimador, usa `model_grip.best_estimator_`.
# La línea `print(model_grip.fit(X_train, y_train))` intentaba ajustar el modelo por segunda vez y luego imprimir el objeto ajustado.
# Ya has accedido a `.best_params_`, que es el resultado más útil de `GridSearchCV`.
# Elimina o comenta esta línea: print(model_grip.fit(X_train, y_train))

y_pred_grip = model_grip.predict(X_test) # Realiza predicciones con el mejor modelo encontrado.
metricas_model_grip = calcular_regresion(y_test, y_pred_grip) # Calcula las métricas para el modelo ajustado.
print("Métricas del modelo con GridSearchCV:")
print(metricas_model_grip) # Muestra las métricas del modelo ajustado con GridSearchCV.

resultados['model_grip'] = list(metricas_model_grip.values()) # Almacena las métricas del modelo ajustado en el DataFrame de resultados.
print(resultados) # Muestra el DataFrame de resultados actualizado con las métricas del modelo ajustado.

import pickle 
try:

    with open('IA_aumentada_previsión_de_atrasos_de_vuelos\\Optimizacion_de_hiperparametros\\datos\\champion.pkl', 'wb') as f:
        pickle.dump(model_grip.best_estimator_, f) # Guarda el modelo ajustado con GridSearchCV en un archivo pickle.
    print('Modelo serializado con exito')
except Exception as e:
    print(f'Error al serializar el modelo: {e}') # Maneja cualquier error

