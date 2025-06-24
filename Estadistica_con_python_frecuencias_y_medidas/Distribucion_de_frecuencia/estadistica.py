import pandas as pd

datos = pd.read_csv("Estadistica_con_python_frecuencias_y_medidas\\Introduccion_a_la_estadistica_y_cuales_son_los_tipos_de_datos\\datos\\datos.csv")

print(datos.head())

# Variables cualitativas

print(sorted(datos['Años de Estudio'].unique())) # verifica los valores únicos en la columna 'Años de Estudio'

print(sorted(datos['Sexo'].unique())) # verifica los valores únicos en la columna 'Sexo'

print(sorted(datos['Color'].unique()))

print(sorted(datos["Ciudad"].unique()))

# Variables cuantitativas

print(datos.Edad.min()) # valor mínimo de la columna 'Edad'
print(datos.Edad.max()) # valor máximo de la columna 'Edad'
print(f"La edad minima es {datos.Edad.min()} y la edad máxima es {datos.Edad.max()}")

# variavles continuas

print(f"La Altura minima es {datos.Altura.min()} y la Altura máxima es {datos.Altura.max()}")

# value_counts() para variables cualitativas

print(datos.Sexo.value_counts()) # cuenta la frecuencia de cada valor en la columna 'Sexo'
print(datos.Sexo.value_counts(normalize=True)*100) # cuenta la frecuencia relativa de cada valor en la columna 'Sexo' ver en porcentaje
print(datos.Sexo.value_counts(normalize=True).round(4)*100)  # cuenta la frecuencia relativa de cada valor en la columna 'Sexo' ver en porcentaje y redondeado a 4 decimales

frecuencia_sexo = datos.Sexo.value_counts()
print(frecuencia_sexo)

porcentaje_sexo = datos.Sexo.value_counts(normalize=True).round(4) * 100
print(porcentaje_sexo)

dist_frec_cualitativas = pd.DataFrame({'Frecuencia': frecuencia_sexo, 'Porcentaje %': porcentaje_sexo})

print(dist_frec_cualitativas)

dist_frec_cualitativas.rename_axis('Sexo', axis= 'columns', inplace=True)  # renombra el índice de las columnas
print(dist_frec_cualitativas)

dist_frec_cualitativas.rename(index= {0: 'Masculino', 1: 'Femenino'}, inplace=True)  # renombra los índices de las filas
print(dist_frec_cualitativas)

# crosstab para variables cualitativas

sexo = {0: 'Masculino', 
        1: 'Femenino'}

color = {0: 'Indigena',
         2: 'Blanco',
         4: 'Mestizo',
         6: 'Amarillo',
         8: 'Pardo',
         9: 'Sin declarar'}

frecuencia = pd.crosstab(datos.Sexo, datos.Color)  # crea una tabla de contingencia entre 'Sexo' y 'Color'

frecuencia.rename(index=sexo, inplace=True)  # renombra los índices de las filas
frecuencia.rename(columns=color, inplace=True)  # renombra los índices de las columnas

print(frecuencia)

frecuencia_porcentaje = pd.crosstab(datos.Sexo, datos.Color, normalize= True).round(4)*100  # crea una tabla de contingencia entre 'Sexo' y 'Color'

frecuencia_porcentaje.rename(index=sexo, inplace=True)  # renombra los índices de las filas
frecuencia_porcentaje.rename(columns=color, inplace=True)  # renombra los índices de las columnas

print(frecuencia_porcentaje)

# value_counts() para variables cuantitativas

print(datos.Ingreso.min())  # valor mínimo de la columna 'Ingresos'
print(datos.Ingreso.max())  # valor máximo de la columna 'Ingresos'

clases = [0, 1576, 3152, 7880, 15760, 200000]  # define los límites de las clases
labels = ['E', 'D', 'C', 'B', 'A']  # define las etiquetas de las clases

# pandas.cut() para crear clases de frecuencias
frecuencia_ingresos = pd.value_counts(
                             pd.cut(x = datos.Ingreso, 
                             bins=clases, 
                             labels=labels, include_lowest=True))  # crea las clases de frecuencias
print(frecuencia_ingresos)  # cuenta la frecuencia de cada clase

frecuencia_ingresos_porcentaje = pd.value_counts(
                             pd.cut(x = datos.Ingreso, 
                             bins=clases, 
                             labels=labels, include_lowest=True), normalize= True).round(3)*100 # crea las clases de frecuencias
print(frecuencia_ingresos_porcentaje)

dist_frec_cuant_personalizado = pd.DataFrame({'Frecuencia': frecuencia_ingresos, 'Porcentaje %': frecuencia_ingresos_porcentaje})

print(dist_frec_cuant_personalizado.sort_index(ascending=False))  # ordena el DataFrame por el índice de forma descendente

import numpy as np

print(datos.shape[0])  # número de filas del DataFrame

n = datos.shape[0]  # número de filas del DataFrame

k = 1 + (10/3 * np.log10(n))  # número de clases según la regla de Sturges
print(f"El número de clases según la regla de Sturges es: {k}")

frecuencia_sturges = pd.value_counts(
                             pd.cut(x = datos.Ingreso, 
                             bins=17,  # número de clases según la regla de Sturges
                             include_lowest=True)) # crea las clases de frecuencias
print(frecuencia_sturges)

frecuencia_sturges_porcentaje = pd.value_counts(
                             pd.cut(x = datos.Ingreso, 
                             bins=17,  # número de clases según la regla de Sturges
                             include_lowest=True), normalize= True).round(4)*100 # crea las clases de frecuencias
print(frecuencia_sturges_porcentaje)

dist_frec_cuant_amplitud_fija = pd.DataFrame({'Frecuencia': frecuencia_sturges, 'Porcentaje %': frecuencia_sturges_porcentaje})

print(dist_frec_cuant_amplitud_fija.sort_index(ascending=False))  # ordena el DataFrame por el índice de forma descendente

# Histograma

import seaborn as sns
import matplotlib.pyplot as plt

ax = sns.displot(datos.Altura, kde = False)

ax.figure.set_size_inches(10, 5)  # establece el tamaño de la figura
ax.set_titles("Distribucion de frecuencia de altura", fontsize = 18)  # establece el título del gráfico
ax.set_xlabels("Altura (Metros)", fontsize= 14)  # establece la etiqueta del eje x


ax = sns.displot(datos.Altura, kde = True)

ax.figure.set_size_inches(10, 5)  # establece el tamaño de la figura
ax.set_titles("Distribucion de frecuencia de altura - KDE", fontsize = 18)  # establece el título del gráfico
ax.set_xlabels("Altura (Metros)", fontsize= 14)  # establece la etiqueta del eje x

plt.show()  # muestra el gráfico