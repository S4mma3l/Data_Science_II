# Visualizacion de datos con Python: Matplotlib, Seaborn y Plotly

import pandas as pd

df = pd.read_csv('Visualización_de_datos_creando_gráficos_con_bibliotecas_de_Python\\Conociendo_la_biblioteca_matplotlib\\datos\\inmigrantes_canada.csv')
print(df)

print(df.info())

print(df.set_index('Pais', inplace=True))

anos = list(map(str, range(1980, 2014)))# Generamos una lista de años como strings
print(anos)

colombia = df.loc['Colombia', anos] # Seleccionamos los datos de Colombia
print(colombia)

col_dict = {"Ano":colombia.index.tolist(), "Inmigrantes":colombia.values.tolist()} # Creamos un diccionario con los datos de Colombia
print(col_dict)

datos_colombia = pd.DataFrame(col_dict) # Creamos un DataFrame con los datos de Colombia
print(datos_colombia)

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4)) # Definimos el tamaño de la figura
plt.plot(datos_colombia['Ano'], datos_colombia['Inmigrantes']) # eje x: Años, eje y: Inmigrantes
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010', '2013'], rotation=45) # Rotamos las etiquetas del eje x
plt.title('Inmigrantes de Colombia a Canadá (1980-2013)') # Título del gráfico
plt.xlabel('Año') # Etiqueta del eje x
plt.ylabel('Número de Inmigrantes') # Etiqueta del eje y
# plt.show()


# Guardamos el gráfico en un archivo
fig, ax = plt.subplots(figsize=(8, 4)) # Creamos una figura y un eje
ax.plot(datos_colombia['Ano'], datos_colombia['Inmigrantes']) # Dibujamos la línea
ax.xaxis.set_major_locator(plt.MultipleLocator(5)) # Establecemos el intervalo de las etiquetas del eje x
ax.set_title('Inmigrantes de Colombia a Canadá \n (1980-2013)') # Título del gráfico
ax.set_xlabel('Año') # Etiqueta del eje x
ax.set_ylabel('Número de Inmigrantes') # Etiqueta del eje y
# plt.show() # Mostramos el gráfico

# grafico boxplot

fig, axs = plt.subplots(1, 2, figsize=(12, 6)) # Creamos una figura con dos ejes
axs[0].plot(datos_colombia['Ano'], datos_colombia['Inmigrantes'])
axs[0].set_title('Inmigrantes de Colombia a Canadá \n (1980-2013)') # Título del gráfico
axs[0].set_xlabel('Año') # Etiqueta del eje x
axs[0].set_ylabel('Número de Inmigrantes') # Etiqueta del eje y
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5)) # Establecemos el intervalo de las etiquetas del eje x
axs[0].grid(True) # Añadimos una cuadrícula al gráfico

axs[1].boxplot(datos_colombia['Inmigrantes']) # Creamos un boxplot
axs[1].set_title('Boxplot de Inmigrantes de Colombia a Canadá \n (1980-2013)') # Título del gráfico
axs[1].set_ylabel('Número de Inmigrantes') # Etiqueta del eje y
axs[1].set_xlabel('Numero de Inmigrantes') # Etiqueta del eje x
axs[1].grid(True) # Añadimos una cuadrícula al gráfico

# plt.show() # Mostramos el gráfico

print(datos_colombia.describe()) # Mostramos un resumen estadístico

# crear diferentes gráficos en una figura de colombia, argentina, peru y chile

fig, axs = plt.subplots(2,2, figsize=(10, 6)) # Creamos una figura con dos filas y dos columnas de ejes
fig.subplots_adjust(hspace=0.5, wspace=0.3) # Ajustamos el espacio entre los subgráficos
fig.suptitle('Número de Inmigrantes de América Latina a Canadá (1980-2013)', fontsize=16) # Título general de la figura

axs[0,0].plot(df.loc['Colombia', anos])
axs[0,0].set_title('Colombia') # Título del gráfico

axs[0,1].plot(df.loc['Brasil', anos])
axs[0,1].set_title('Brasil') # Título del gráfico

axs[1,0].plot(df.loc['Argentina', anos])
axs[1,0].set_title('Argentina') # Título del gráfico

axs[1,1].plot(df.loc['Perú', anos])
axs[1,1].set_title('Perú') # Título del gráfico

ymin = 0 # Valor mínimo del eje y
ymax = 7000 # Valor máximo del eje y

for ax in axs.ravel(): # Iteramos sobre todos los ejes
    ax.set_ylim(ymin, ymax) # Establecemos el rango del eje y
    ax.xaxis.set_major_locator(plt.MultipleLocator(5)) # Establecemos el intervalo de las etiquetas del eje x
    ax.set_xlabel('Año') # Etiqueta del eje x
    ax.set_ylabel('Número de Inmigrantes') # Etiqueta del eje y
    ax.grid(True) # Añadimos una cuadrícula al gráfico

for ax in axs.flat: # Iteramos sobre todos los ejes
    ax.xaxis.set_major_locator(plt.MultipleLocator(5)) # Establecemos el intervalo de las etiquetas del eje x
    ax.set_xlabel('Año') # Etiqueta del eje x
    ax.set_ylabel('Número de Inmigrantes') # Etiqueta del eje y
    ax.grid(True) # Añadimos una cuadrícula al gráfico

# plt.show() # Mostramos el gráfico

fig, ax = plt.subplots(figsize=(8, 3)) # Creamos una figura y un eje
ax.plot(datos_colombia['Ano'], datos_colombia['Inmigrantes'], lw= 2.5, color = 'g') # Dibujamos la línea
ax.xaxis.set_major_locator(plt.MultipleLocator(5)) # Establecemos el intervalo de las etiquetas del eje x
ax.set_title('Inmigrantes de Colombia a Canadá \n (1980-2013)', fontsize = 18, loc= 'left') # Título del gráfico 
ax.set_xlabel('Año', fontsize = 14) # Etiqueta del eje x
ax.set_ylabel('Número de Inmigrantes', fontsize = 14) # Etiqueta del eje y
ax.yaxis.set_tick_params(labelsize=12) # Tamaño de las etiquetas del eje y
ax.xaxis.set_tick_params(labelsize=12) # Tamaño de las etiquetas del eje x
# ax.grid(True, linestyle = '--') # Añadimos una cuadrícula al gráfico

ax.spines['top'].set_visible(False) # Hacemos invisible el borde superior
ax.spines['right'].set_visible(False) # Hacemos invisible el borde derecho

# Guardamos el gráfico en un archivo
fig.savefig('Visualización_de_datos_creando_gráficos_con_bibliotecas_de_Python\\Personalizando_graficos_con_matplotlib\\data\\inmigrantes_colombia.png', 
            dpi=300, bbox_inches='tight', transparent=False) # Guardamos el gráfico en un archivo

# plt.show() # Mostramos el gráfico

sudamerica = df.query('Region == "América del Sur"') # Filtramos los datos de América del Sur

print(sudamerica)



colores = ['gray', 'magenta', 'lime', 'teal', 'navy', 'maroon', 
           'olive', 'coral', 'gold', 'silver', 'indigo', 'royalblue' ] # Lista de colores

fig, ax = plt.subplots(figsize=(12, 5)) # Creamos una figura y un eje
ax.barh(sudamerica.index, sudamerica['Total'], color=colores) # Dibujamos el gráfico de barras
ax.set_title('Número de Inmigrantes de América del Sur a Canadá \n (1980-2013)', fontsize=16, loc='left') # Título del gráfico
ax.set_xlabel(' ') # Etiqueta del eje x
ax.set_ylabel('Número de Inmigrantes', fontsize=14) # Etiqueta del eje y
ax.xaxis.set_tick_params(labelsize=12) # Tamaño de las etiquetas del eje x
ax.yaxis.set_tick_params(labelsize=12) # Tamaño de las etiquetas del eje y

# plt.show() # Mostramos el gráfico

sudamerica_sorted = sudamerica.sort_values(by='Total', ascending=True) # Ordenamos los datos de América del Sur por el total de inmigrantes

colores = ['gray', 'magenta', 'lime', 'teal', 'navy', 'maroon', 
           'olive', 'coral', 'gold', 'silver', 'indigo', 'royalblue' ] # Lista de colores

fig, ax = plt.subplots(figsize=(12, 5)) # Creamos una figura y un eje
ax.barh(sudamerica_sorted.index, sudamerica_sorted['Total'], color=colores) # Dibujamos el gráfico de barras
ax.set_title('Número de Inmigrantes de América del Sur a Canadá \n (1980-2013)', fontsize=16, loc='left') # Título del gráfico
ax.set_xlabel(' ') # Etiqueta del eje x
ax.set_ylabel('Número de Inmigrantes', fontsize=14) # Etiqueta del eje y
ax.xaxis.set_tick_params(labelsize=12) # Tamaño de las etiquetas del eje x
ax.yaxis.set_tick_params(labelsize=12) # Tamaño de las etiquetas del eje y

colores = [] # Lista para almacenar los colores
# Asignamos un color específico a Colombia y gris a los demás países
for pais in sudamerica_sorted.index: # Iteramos sobre los países
    if pais == 'Colombia':
        colores.append('red') # Si el país es Colombia, añadimos el color rojo
    else:
        colores.append('gray')

fig, ax = plt.subplots(figsize=(12, 5)) # Creamos una figura y un eje

ax.set_frame_on(False) # Desactivamos el marco del gráfico
ax.xaxis.set_visible(False) # Hacemos invisible el eje
ax.tick_params(axis='y', which='both', size=0) # Desactivamos las marcas del eje y

ax.barh(sudamerica_sorted.index, sudamerica_sorted['Total'], color=colores) # Dibujamos el gráfico de barras
ax.set_title('Número de Inmigrantes de América del Sur a Canadá \n (1980-2013)', fontsize=16, loc='left') # Título del gráfico
ax.set_xlabel(' ') # Etiqueta del eje x
# ax.set_ylabel('Número de Inmigrantes', fontsize=14) # Etiqueta del eje y
# ax.xaxis.set_tick_params(labelsize=12) # Tamaño de las etiquetas del eje x
ax.yaxis.set_tick_params(labelsize=12) # Tamaño de las etiquetas del eje y    

for i,j in enumerate(sudamerica_sorted['Total']): # Iteramos sobre los valores del total de inmigrantes
    ax.text(j + 20, i, str(j), color='black', fontsize=10, ha = 'left', va = 'center') # Añadimos el valor al lado de la barra

fig.savefig('Visualización_de_datos_creando_gráficos_con_bibliotecas_de_Python\\Personalizando_graficos_con_matplotlib\\data\\inmigrantes_sudamerica.png', 
            dpi=300, bbox_inches='tight', transparent=False) # Guardamos el gráfico en un archivo
# plt.show() # Mostramos el gráfico

print(fig.canvas.get_supported_filetypes()) # Mostramos los tipos de archivo soportados por el canvas