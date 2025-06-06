import pandas as pd

datos = 'Pandas_transformación_y_manipulación_de_datos\\Conociendo_el_problema\\data\\datos_hosting.json'

# Cargar el archivo JSON
archivos = pd.read_json(datos)

# Mostrar las primeras filas del DataFrame
print(archivos.head())

# normalizar los datos
archivos_normalizados = pd.json_normalize(archivos['info_inmuebles'])

# Mostrar las primeras filas del DataFrame normalizado
print(archivos_normalizados.head())