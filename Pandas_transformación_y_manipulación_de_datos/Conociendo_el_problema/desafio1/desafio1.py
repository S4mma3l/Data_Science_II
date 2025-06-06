import pandas as pd
import json # Necesario para cargar el archivo JSON
import os # Para construir la ruta del archivo de forma robusta

# --- 1. Carga y Normalización del Archivo JSON ---
# Ruta del archivo JSON de ventas
json_file_path = os.path.join(
    'Pandas_transformación_y_manipulación_de_datos',
    'Conociendo_el_problema',
    'desafio1',
    'dados_vendas_clientes.json'
)

# Carga el contenido del archivo JSON
try:
    with open(json_file_path, 'r', encoding='utf-8') as f:
        datos_json = json.loads(f.read()) # Se usa json.loads para leer el contenido como JSON
except FileNotFoundError:
    print(f"Error: El archivo '{json_file_path}' no se encontró.")
    print("Asegúrate de que la ruta sea correcta y que el archivo exista.")
    exit()

# La estructura JSON tiene una lista principal bajo la clave "dados_vendas".
# Cada elemento en esta lista tiene "Data de venda", "Cliente" (lista), y "Valor da compra" (lista).
# Para aplanar esto, primero normalizamos el nivel superior y luego 'explotamos' las listas anidadas.

# Normaliza el nivel principal para obtener un DataFrame con las listas de Clientes y Valores
df_temp = pd.json_normalize(datos_json['dados_vendas'])

# Mostramos las primeras filas del DataFrame temporal para verificar la estructura
print("--- DataFrame Temporal (Primeras 5 filas) ---")
print(df_temp.head())
print("\n--- Tipos de datos iniciales del DataFrame Temporal ---")

# Usamos explode para aplanar las listas de 'Cliente' y 'Valor da compra' en filas individuales.
# Es crucial que las listas de Cliente y Valor da compra en cada fila de df_temp tengan la misma longitud
# para que la alineación sea correcta después de explotar.
# Para este JSON específico, la forma más robusta es explotar por separado y luego unir por índice.
df_clientes_exploded = df_temp[['Data de venda', 'Cliente']].explode('Cliente').reset_index(drop=True)
df_valores_exploded = df_temp[['Data de venda', 'Valor da compra']].explode('Valor da compra').reset_index(drop=True)

# Reconstruimos el DataFrame final uniendo los DataFrames explotados por su índice.
# Asumimos que el orden se mantiene tras el explode y reset_index para cada bloque de 'Data de venda'.
df_ventas_normalizado = pd.DataFrame({
    'Data de venda': df_clientes_exploded['Data de venda'],
    'Cliente': df_clientes_exploded['Cliente'],
    'Valor da compra': df_valores_exploded['Valor da compra']
})

print("--- DataFrame de Ventas Normalizado (Primeras 5 filas) ---")
print(df_ventas_normalizado.head())
print("\n--- Tipos de datos iniciales del DataFrame Normalizado ---")
print(df_ventas_normalizado.dtypes)

# --- 2. Limpieza y Conversión de la Columna 'Valor da compra' ---
# La columna 'Valor da compra' es un string (objeto) y contiene "R$" y comas como separadores decimales.
# Para realizar cálculos, necesitamos convertirla a un tipo numérico (float).

# Paso 1: Eliminar "R$"
df_ventas_normalizado['Valor da compra'] = df_ventas_normalizado['Valor da compra'].str.replace('R$', '', regex=False)

# Paso 2: Reemplazar la coma (,) por un punto (.) para el separador decimal
df_ventas_normalizado['Valor da compra'] = df_ventas_normalizado['Valor da compra'].str.replace(',', '.')

# Paso 3: Convertir la columna a tipo numérico (float)
df_ventas_normalizado['Valor da compra'] = df_ventas_normalizado['Valor da compra'].astype(float)

print("\n--- DataFrame después de limpiar y convertir 'Valor da compra' (Primeras 5 filas) ---")
print(df_ventas_normalizado.head())
print("\n--- Tipos de datos después de la conversión ---")
print(df_ventas_normalizado.dtypes)

# --- 3. Agrupar por Cliente y Sumar el Valor Total de Compra ---
# Usamos el método `groupby()` para agrupar las ventas por cada 'Cliente'.
# Luego, aplicamos el método `sum()` a la columna 'Valor da compra' para obtener el total gastado por cada cliente.
gastos_por_cliente = df_ventas_normalizado.groupby('Cliente')['Valor da compra'].sum()

print("\n--- Gasto total por cliente ---")
print(gastos_por_cliente.head()) # Muestra los primeros resultados agrupados

# --- 4. Identificar al Cliente con la Mayor Compra ---
# Usamos `sort_values()` para ordenar los clientes por su gasto total de forma descendente.
# Luego, `head(1)` para obtener solo el cliente que más gastó.
cliente_mayor_compra = gastos_por_cliente.sort_values(ascending=False).head(1)

print("\n--- Cliente con la mayor compra de la semana ---")
print(cliente_mayor_compra)

# Si quieres extraer solo el nombre del cliente y el valor:
nombre_cliente_ganador = cliente_mayor_compra.index[0]
valor_compra_ganador = cliente_mayor_compra.iloc[0]

print(f"\n¡El cliente ganador del premio es: {nombre_cliente_ganador} con una compra total de R$ {valor_compra_ganador:.2f}!")