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
plt.show()
