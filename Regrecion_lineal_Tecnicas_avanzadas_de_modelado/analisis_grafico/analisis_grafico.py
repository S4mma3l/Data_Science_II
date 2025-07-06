import pandas as pd

datos = pd.read_csv('Regrecion_lineal_Tecnicas_avanzadas_de_modelado\\analisis_preliminar\\datos\\dataset.csv', sep=';')

print(datos.head())

print(datos.shape)
print(len(datos.columns))

print(datos.describe().round(2))

# Matriz de correlacion

print(datos.corr().round(2))

import seaborn as sns
import matplotlib.pyplot as plt


sns.set_palette('Accent')
sns.set_style('darkgrid')

ax = sns.boxplot(data=datos['Valor'], orient='h', width=0.3)

ax.figure.set_size_inches(10, 5)
ax.set_title('Precio de los Inmuebles', fontsize=20)
ax.set_xlabel('Dolares', fontsize=16)
ax

plt.show()

ax = sns.distplot(datos['Valor'])


ax.figure.set_size_inches(10, 6)
ax.set_title('Distribuición de Frecuencias', fontsize=20)
ax.set_xlabel('Precio de los Inmuebles (US$)', fontsize=16)
ax

plt.show()

ax = sns.pairplot(datos, y_vars='Valor', x_vars=['Area','Dist_Playa','Dist_Farmacia'], height=5)
ax.fig.suptitle('Dispersión entre las Variables', fontsize=10, y=1.05)
ax
plt.show()

grid = sns.pairplot(datos, y_vars='Valor', x_vars=['Area','Dist_Playa','Dist_Farmacia'], height=5, kind='reg')
# Iterar sobre los ejes del pairplot para personalizar los colores
for i, ax_row in enumerate(grid.axes):
    for j, ax in enumerate(ax_row):
        if i == 0 and j < len(grid.x_vars): # Solo trabajamos en la primera fila (Valor vs. cada x_var)
            # Encontrar los scatter plots y cambiar su color
            scatter = ax.collections
            if scatter:
                scatter[-1].set_color('blue') # Cambiar el color de los puntos al azul

            # Encontrar las líneas de regresión y cambiar su color
            lines = ax.lines
            if lines and len(lines) > 0:
                lines[-1].set_color('green') # Cambiar el color de la línea de regresión al verde
                if len(lines) > 1:
                    lines[-2].set_color('lightgreen') # Cambiar el color del intervalo de confianza

grid.fig.suptitle('Dispersión entre las Variables', fontsize=10, y=1.05)


plt.show()