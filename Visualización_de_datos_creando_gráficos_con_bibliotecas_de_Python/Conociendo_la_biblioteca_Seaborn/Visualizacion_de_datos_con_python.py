# Sección 1: Importar librerías y Cargar Datos

# Importa la librería pandas para manipulación de datos y creación de DataFrames.
import pandas as pd
# Importa la librería matplotlib.pyplot para la creación de gráficos.
import matplotlib.pyplot as plt

# Carga el archivo CSV 'inmigrantes_canada.csv' en un DataFrame de pandas.
# La ruta del archivo es relativa a la ubicación de ejecución del script.
df = pd.read_csv('Visualización_de_datos_creando_gráficos_con_bibliotecas_de_Python\\Conociendo_la_biblioteca_matplotlib\\datos\\inmigrantes_canada.csv')

# Establece la columna 'Pais' como el índice del DataFrame.
# `inplace=True` modifica el DataFrame original directamente.
df.set_index('Pais', inplace=True)

# Sección 2: Procesamiento de Datos para el Gráfico de Barras Horizontales

# Filtra el DataFrame para incluir solo los países de la 'Región' "América del Sur".
sudamerica = df.query('Region == "América del Sur"')

# Ordena los datos de los países de América del Sur por la columna 'Total' de forma ascendente.
# Esto es útil para que las barras se muestren en orden ascendente de valor.
sudamerica_sorted = sudamerica.sort_values(by='Total', ascending=True)

# seaborn
# Importa la biblioteca seaborn para visualización de datos.
import seaborn as sns

# Configura un tema de estilo para los gráficos de seaborn.
sns.set_theme()

top_10 = df.sort_values(by='Total', ascending=False).head(10)

print(top_10)

# Crea un gráfico de barras verticales utilizando seaborn.
ax = sns.barplot(data=top_10, x='Total', y=top_10.index, orient='h')
ax.set(title='Top 10 países con más inmigrantes en Canadá\n 1980 - 2013',
             xlabel='Numero de Inmigrantes',
             ylabel= 'Ano')  # Establece el título del gráfico.


fig, ax = plt.subplots(figsize=(8, 4))  # Crea una figura y un eje para el gráfico.
ax = sns.barplot(data=top_10, x='Total', y=top_10.index, orient='h')  # Crea un gráfico de barras horizontales.
ax.set_title('Top 10 países con más inmigrantes en Canadá\n 1980 - 2013',
       loc='left', fontsize=16)  # Establece el título del gráfico.
ax.set_xlabel('Numero de Inmigrantes', fontsize=14)  # Establece la etiqueta del eje x.
ax.set_ylabel(' ')  # Establece la etiqueta del eje y.

# plt.show()  # Muestra el gráfico creado con seaborn.

def generar_grafico(Palette):

    fig, ax = plt.subplots(figsize=(8, 4))  # Crea una figura y un eje para el gráfico.

    ax.set(xticklabels=[])

    ax = sns.barplot(data=top_10, x='Total', y=top_10.index, hue=top_10.index, orient='h', palette=Palette, legend=False)  # Crea un gráfico de barras horizontales.
    ax.set_title('Top 10 países con más inmigrantes en Canadá\n 1980 - 2013',
           loc='left', fontsize=16)  # Establece el título del gráfico.
    ax.set_xlabel('Numero de Inmigrantes', fontsize=14)  # Establece la etiqueta del eje x.
    ax.set_ylabel(' ')  # Establece la etiqueta del eje y.
    sns.despine()

    for i,j in enumerate(top_10['Total']): # Iteramos sobre los valores del total de inmigrantes
        ax.text(j + 20, i, str(j), color='black', fontsize=10, ha = 'left', va = 'center') # Añadimos el valor al lado de la barra

    plt.show()  # Muestra el gráfico creado con seaborn.

# Genera gráficos con diferentes paletas de colores.
sns.set_theme(style="whitegrid")  # Configura el tema de estilo para seaborn.
generar_grafico('Paired_r')  # Paleta de colores 'Paired'.
