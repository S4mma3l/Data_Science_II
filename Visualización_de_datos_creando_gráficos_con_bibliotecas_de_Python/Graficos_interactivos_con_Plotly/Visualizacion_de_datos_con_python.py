import pandas as pd

# --- Carga y preparación inicial del DataFrame principal (df) ---
df = pd.read_csv('Visualización_de_datos_creando_gráficos_con_bibliotecas_de_Python\\Conociendo_la_biblioteca_matplotlib\\datos\\inmigrantes_canada.csv')
print("--- DataFrame 'df' (inicial) ---")
print(df)

# Imprime información general del DataFrame 'df'.
print("\n--- Información de 'df' (inicial) ---")
print(df.info())

# Establece la columna 'Pais' como índice del DataFrame.
# La operación se realiza in-place, por lo que df se modifica directamente.
df.set_index('Pais', inplace=True)
print("\n--- DataFrame 'df' (después de set_index) ---")
print(df.head()) # Muestra las primeras filas con el nuevo índice


# --- Procesamiento de datos para Colombia (datos_colombia) ---
# Generamos una lista de años como strings
anos = list(map(str, range(1980, 2014)))
print("\n--- Lista de años ---")
print(anos)

# Seleccionamos los datos de 'Colombia' del DataFrame 'df'
colombia = df.loc['Colombia', anos]
print("\n--- Serie 'colombia' ---")
print(colombia)

# Creamos un diccionario con los datos de 'Colombia'
col_dict = {"Ano":colombia.index.tolist(), "Inmigrantes":colombia.values.tolist()}
print("\n--- Diccionario 'col_dict' ---")
print(col_dict)

# Creamos un DataFrame 'datos_colombia' a partir del diccionario
datos_colombia = pd.DataFrame(col_dict)
print("\n--- DataFrame 'datos_colombia' ---")
print(datos_colombia)


# --- Resumen estadístico de datos_colombia ---
# Mostramos un resumen estadístico del DataFrame 'datos_colombia'
print("\n--- Resumen estadístico de 'datos_colombia' ---")
print(datos_colombia.describe())


# --- Procesamiento de datos para América del Sur (sudamerica, sudamerica_sorted) ---
# Filtramos los datos de 'América del Sur' del DataFrame 'df'
sudamerica = df.query('Region == "América del Sur"')
print("\n--- DataFrame 'sudamerica' ---")
print(sudamerica)

# Ordenamos los datos de 'sudamerica' por el total de inmigrantes
sudamerica_sorted = sudamerica.sort_values(by='Total', ascending=True)
print("\n--- DataFrame 'sudamerica_sorted' ---")
print(sudamerica_sorted)


# --- Creación de top_10 ---
# Filtramos los top 10 países con más inmigrantes a Canadá
top_10 = df.sort_values(by='Total', ascending=False).head(10)
print("\n--- DataFrame 'top_10' ---")
print(top_10)

# El resto del código en tu ejemplo se refiere a la creación y personalización de gráficos
# con Matplotlib y Seaborn, así como la configuración de paletas de colores,
# que no generan DataFrames nuevos sino visualizaciones.

import plotly.express as px  # Importa la biblioteca plotly.express para gráficos interactivos.

fig = px.line(
    datos_colombia, 
    x='Ano', 
    y='Inmigrantes',
    title='Inmigrantes de Colombia a Canadá (1980-2013)',
    labels={'Ano': 'Año', 'Inmigrantes': 'Número de Inmigrantes'},
)

fig.update_traces(line_color='green', line_width=2)  # Actualiza el color y el ancho de la línea del gráfico.
fig.update_layout(width=1800, height=900, xaxis={'tickangle':-45}, font_family='Arial', font_size=14, font_color='grey')  # Establece el tamaño del gráfico.
fig.write_html("Visualización_de_datos_creando_gráficos_con_bibliotecas_de_Python\\Graficos_interactivos_con_Plotly\\data\\inmigrantes_colombia_plotly.html")

fig.show()  # Muestra el gráfico interactivo.

sudamerica.drop(['Continente', 'Region', 'Total'], axis=1, inplace=True)  # Elimina columnas innecesarias del DataFrame 'sudamerica'.
print("\n--- DataFrame 'sudamerica' después de eliminar columnas ---")
print(sudamerica)

sudamerica = sudamerica.T  # Transpone el DataFrame 'sudamerica'.
print("\n--- DataFrame 'sudamerica' transpuesto ---")
print(sudamerica)

fig = px.line(
    sudamerica, 
    x=sudamerica.index,
    y=sudamerica.columns,
    title='Inmigrantes Sudamericanos a Canadá (1980-2013)',
    color= 'Pais',
    markers=True,
    labels={'value': 'Número de Inmigrantes', 'variable': 'País'},
)

fig.update_layout(width=1800, height=900, xaxis={'tickangle':-45}, font_family='Arial', font_size=14, font_color='grey')  # Establece el tamaño del gráfico.
fig.write_html("Visualización_de_datos_creando_gráficos_con_bibliotecas_de_Python\\Graficos_interactivos_con_Plotly\\data\\inmigrantes_sudamerica_plotly.html")

fig.show()  # Muestra el gráfico interactivo.