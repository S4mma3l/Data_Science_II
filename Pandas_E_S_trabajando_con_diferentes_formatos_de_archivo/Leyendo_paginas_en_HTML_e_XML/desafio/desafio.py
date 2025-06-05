import pandas as pd

# URL del artículo de Wikipedia
url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_poblaci%C3%B3n"

# Usar pd.read_html para leer todas las tablas de la página
# Esto devolverá una lista de DataFrames, uno por cada tabla encontrada.
# tablas_poblacion = pd.read_html(url)[3]
# tablas_poblacion_2 = pd.read_html(url)[4]
tablas_poblacion_3 = pd.read_html(url)[5]


# Imprimir el número de tablas encontradas para saber cuántas hay
print(tablas_poblacion_3)

# INSPECCIONAR LAS COLUMNAS! ---
print("--- Nombres exactos de las columnas en tablas_poblacion_3 ---")
print(tablas_poblacion_3.columns.tolist())
print("-" * 50) # Separador visual

# Imprimir las primeras filas del DataFrame (para contexto)
print("--- Primeras filas de tablas_poblacion_3 ---")
print(tablas_poblacion_3.head())
print("-" * 50) # Separador visual

# Columnas a extraer
columnas_a_extraer = [
    'País (o territorio dependiente)',
    'Población estimada por la ONU para mediados del año  2000'
]

poblacion_filtrada = tablas_poblacion_3[columnas_a_extraer]

# Renombrar las columnas para mayor claridad
poblacion_filtrada.columns = ['Pais', 'Poblacion']

# Mostrar las primeras filas del DataFrame filtrado
print(poblacion_filtrada)

# Guardar el DataFrame filtrado en un archivo CSV
poblacion_filtrada.to_html('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo/Leyendo_paginas_en_HTML_e_XML/desafio/poblacion_dependientes.html', index=False)