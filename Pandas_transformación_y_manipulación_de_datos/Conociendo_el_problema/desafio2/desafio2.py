import pandas as pd
import json # Necesario para cargar el archivo JSON
import os # Para construir rutas de archivo de forma robusta

# --- 1. Carga y Normalización del Archivo JSON ---
# Define la ruta del archivo JSON de datos de locación.
# Asegúrate de que este archivo esté en la misma ubicación que tu script,
# o ajusta la ruta para que sea la correcta en tu sistema.
# Por ejemplo, si está en un subdirectorio 'data':
# json_file_path = os.path.join('data', 'dados_locacao_imoveis.json')
json_file_path = 'Pandas_transformación_y_manipulación_de_datos\\Conociendo_el_problema\\desafio2\\dados_locacao_imoveis.json' # Ajusta esta ruta si es necesario

# Carga el contenido del archivo JSON
try:
    with open(json_file_path, 'r', encoding='utf-8') as f:
        datos_json = json.loads(f.read()) # Lee el contenido del archivo JSON
except FileNotFoundError:
    print(f"Error: El archivo '{json_file_path}' no se encontró.")
    print("Asegúrate de que la ruta del archivo sea correcta y que el archivo exista.")
    exit() # Sale del script si el archivo no se encuentra.

# El archivo JSON tiene la clave "dados_locacao" que contiene una lista de registros.
# Cada registro tiene "apartamento" (string), y luego listas para "datas_combinadas_pagamento",
# "datas_de_pagamento" y "valor_aluguel".

# --- Estrategia de Normalización y Aplanamiento ---
# Para aplanar las listas paralelas ("datas_combinadas_pagamento", "datas_de_pagamento", "valor_aluguel")
# y el "apartamento" que se repite para cada elemento de la lista,
# la mejor forma es normalizar el nivel superior y luego usar .explode()
# para cada una de las columnas de lista.

# Primero, crea un DataFrame a partir de la lista principal de registros
# La clave 'dados_locacao' es la raíz de la lista de diccionarios.
df_locacao_temp = pd.json_normalize(datos_json['dados_locacao'])

# Para aplanar las listas anidadas manteniendo la alineación:
# 1. Creamos un índice de "transacción" temporal que se repetirá para cada elemento explotado.
df_locacao_temp['transaction_idx'] = df_locacao_temp.index

# 2. Explotamos cada columna de lista, manteniendo el 'apartamento' y el 'transaction_idx' como identificadores.
df_apartamento_exploded = df_locacao_temp[['transaction_idx', 'apartamento']].explode('apartamento').reset_index(drop=True)
df_datas_combinadas_exploded = df_locacao_temp[['transaction_idx', 'datas_combinadas_pagamento']].explode('datas_combinadas_pagamento').reset_index(drop=True)
df_datas_pagamento_exploded = df_locacao_temp[['transaction_idx', 'datas_de_pagamento']].explode('datas_de_pagamento').reset_index(drop=True)
df_valor_aluguel_exploded = df_locacao_temp[['transaction_idx', 'valor_aluguel']].explode('valor_aluguel').reset_index(drop=True)

# 3. Unimos los DataFrames explotados por el 'transaction_idx'
# Es crucial que todas las listas en un registro original tengan la misma longitud.
# Si tienen diferentes longitudes, esto podría generar desalineaciones.
# Para este JSON, las longitudes de las listas son consistentes por registro.
df_locacao_normalizado = pd.DataFrame({
    'apartamento': df_apartamento_exploded['apartamento'],
    'data_combinada_pagamento': df_datas_combinadas_exploded['datas_combinadas_pagamento'],
    'data_de_pagamento': df_datas_pagamento_exploded['datas_de_pagamento'],
    'valor_aluguel': df_valor_aluguel_exploded['valor_aluguel']
})


print("--- DataFrame Final de Locación Normalizado (Primeras 10 filas) ---")
print(df_locacao_normalizado.head(10))

print("\n--- Información del DataFrame Normalizado ---")
df_locacao_normalizado.info()

print("\n--- Tipos de datos de las columnas ---")
print(df_locacao_normalizado.dtypes)