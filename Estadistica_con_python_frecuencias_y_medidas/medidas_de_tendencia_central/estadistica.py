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

# plt.show()  # muestra el gráfico

#  Medidas de tendencia central

# Media

df = pd.DataFrame(data = {'María': [8, 10, 4, 8, 6, 10, 8],
                          'Pedro': [10, 2, 0.5, 1, 3, 9.5, 10],
                          'Pablo': [7.5, 8, 7, 8, 8, 8.5, 7]},
                  index = ['Matemática',
                           'Portugués',
                           'Inglés',
                           'Geografía',
                           'Historia',
                           'Física',
                           'Química'])
df.rename_axis('Asignaturas', axis = 'columns', inplace = True)
print(df)

print(df.María.mean())  # media de las calificaciones de María

print(datos.groupby(['Sexo'])['Ingreso'].mean())  # media de los ingresos por sexo

#  Mediana

notas_maria = df['María'].sort_values()  # ordena las calificaciones de María
print(notas_maria)

n = notas_maria.shape[0]  # número de calificaciones de María
print(n)

notas_maria = notas_maria.reset_index()  # reinicia el índice de las calificaciones de María
print(notas_maria)

elemento_medio = (n + 1)/ 2  # elemento medio de las calificaciones de María
print(elemento_medio)

notas_maria.loc[elemento_medio -1]  # obtiene el elemento medio de las calificaciones de María

print(notas_maria['María'].median())  # media de las calificaciones de María

datos['Ingreso'].median()  # media de los ingresos
print(datos['Ingreso'].median())  # media de los ingresos por sexo

# Moda

datos.Ingreso.mode()  # moda de los ingresos
print(datos.Ingreso.mode())  # moda de los ingresos

datos.Altura.mode()  # moda de las alturas
print(datos.Altura.mode())  # moda de las alturas

# relacion entre las medidas de tendencia central

ax = sns.displot(datos.query("Ingreso < 20000").Ingreso, kde = True)
ax.figure.set_size_inches(10, 5)  # establece el tamaño de la figura
ax

plt.show()  # muestra el gráfico

'''
Interpretación General de la Asimetría:

    Tendencia Central (Distribución Simétrica): 
    Los datos se distribuyen de manera equilibrada alrededor de la media. La cola del gráfico es similar 
    en ambos lados. En este caso, la media, la mediana y la moda son aproximadamente iguales.
    
    Tendencia Izquierda (Asimetría Positiva o Asimetría a la Derecha): 
    La cola del gráfico se extiende más hacia la derecha. Esto significa que la mayoría de los datos se 
    agrupan en el lado izquierdo del gráfico. Generalmente, la media es mayor que la mediana y la moda (Media>Mediana>Moda).
    
    Tendencia Derecha (Asimetría Negativa o Asimetría a la Izquierda): 
    La cola del gráfico se extiende más hacia la izquierda. Esto significa que la mayoría de los 
    datos se agrupan en el lado derecho del gráfico. Generalmente, la media es menor que la mediana y la moda (Media<Mediana<Moda).
'''