import pandas as pd

datos = 'Pandas_transformación_y_manipulación_de_datos\\Datos_numericos\\data\\datos_hosting.json'

# Cargar el archivo JSON
archivos = pd.read_json(datos)

# Mostrar las primeras filas del DataFrame
print(archivos.head())

# normalizar los datos
datos2 = pd.json_normalize(archivos['info_inmuebles'])

# Mostrar las primeras filas del DataFrame normalizado
print(datos2.head())

columnas = list(datos2.columns)

# Mostrar las columnas del DataFrame normalizado
print("Columnas del DataFrame normalizado:")
print(columnas)

datos3= datos2.explode(columnas[3:])# Explosión de las columnas a partir de la cuarta columna

# Mostrar las primeras filas del DataFrame después de la explosión
print(datos3.head())

# remplazar indices duplicados
datos3.reset_index(inplace=True, drop=True)

# Mostrar información del DataFrame 
print("Información del DataFrame:")
print(datos3.info())

import numpy as np

datos3['max_hospedes'] = datos3['max_hospedes'].astype(np.int64) # Convertir la columna 'max_hospedes' a tipo int64

print(datos3.info())

col_numericas = ['cantidad_baños', 'cantidad_cuartos', 'cantidad_camas']

datos3[col_numericas] = datos3[col_numericas].astype(np.int64)

print(datos3.info())

datos3['evaluacion_general'] = datos3['evaluacion_general'].astype(np.float64)

print(datos3.info())

precio = datos3['precio']
print(precio)

datos3['precio'] = datos3['precio'].apply(lambda x: x.replace('$', '').replace(',', '').strip())
datos3['precio'] = datos3['precio'].astype(np.float64)
print(datos3.info())

datos3[['cuota_deposito', 'cuota_limpieza']] = datos3[['cuota_deposito', 'cuota_limpieza']].apply(lambda x: x.str.replace('$', '').str.replace(',', '').astype(np.float64))
print(datos3.info())
print(datos3.head())

print(datos3['descripcion_local'].str.lower()) # Convertir la columna 'descripcion_local' a minúsculas

datos3['descripcion_local'] = datos3['descripcion_local'].str.lower() # Convertir la columna 'descripcion_local' a minúsculas y asignar el resultado de nuevo a la columna
print(datos3['descripcion_local'].head())

print(datos3['descripcion_local'][3169])

datos3['descripcion_local'] = datos3['descripcion_local'].str.replace('[^a-zA-Z0-9\\-\']', ' ', regex=True) # Reemplazar los espacios en blanco por un espacio
datos3['descripcion_local'] = datos3['descripcion_local'].str.replace('(?<!\\w)-(?!\\w)', ' ', regex=True) # Reemplazar los guiones por un espacio

print(datos3['descripcion_local'].head())

# Tokenizacion de strings

datos3['descripcion_local'] = datos3['descripcion_local'].str.split()

print(datos3['descripcion_local'].head())

datos3['comodidades'] = datos3['comodidades'].str.replace('\\{|}|\\"', '', regex=True) # Reemplazar los caracteres '{', '}', '"' por un espacio

print(datos3['comodidades'].head())

datos3['comodidades'] = datos3['comodidades'].str.split(',') # Tokenizar la columna 'comodidades'
print(datos3['comodidades'].head())

# Datos de tiempo

dt_data = pd.read_json('Pandas_transformación_y_manipulación_de_datos\\Datos_de_tiempo\\data\\inmuebles_disponibles.json')

# Mostrar las primeras filas del DataFrame
print(dt_data.head())
print(dt_data.info())

dt_data['fecha'] = pd.to_datetime(dt_data['fecha'], format='%Y-%m-%d') # Convertir la columna 'fecha' a tipo datetime

print(dt_data.info())
print(dt_data.head())

dt_data['fecha'].dt.strftime('%Y-%m')

subset = dt_data.groupby(dt_data['fecha'].dt.strftime('%Y-%m'))['lugar_disponible'].sum() # Agrupar por mes y sumar los lugares disponibles
print(subset)
