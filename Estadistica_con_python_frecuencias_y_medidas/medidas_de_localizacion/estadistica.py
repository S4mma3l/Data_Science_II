import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datos = pd.read_csv("Estadistica_con_python_frecuencias_y_medidas\\Introduccion_a_la_estadistica_y_cuales_son_los_tipos_de_datos\\datos\\datos.csv")

datos.Ingreso.quantile(0.25)  # primer cuartil
datos.Ingreso.quantile(0.5)   # mediana
datos.Ingreso.quantile(0.75)  # tercer cuartil

print(datos.Ingreso.quantile(0.25))  # primer cuartil
print(datos.Ingreso.quantile(0.5))   # mediana
print(datos.Ingreso.quantile(0.75))  # tercer cuartil

[i/10 for i in range(1, 10)]  # los percentiles del 10 al 90
print(datos.Ingreso.quantile([i/10 for i in range(1, 10)]))  # percentiles del 10 al 90
print(datos.Ingreso.quantile([i/100 for i in range(1, 100)]))  # percentiles del 10 al 90 con más precisión

ax = sns.displot(x=datos.Edad,
                 kind='hist', # Puedes especificar 'hist' para el histograma
                 cumulative=True, # Este es el argumento clave para la acumulación
                 bins=10,
                 # Puedes pasar argumentos de estilo directamente si son aceptados por displot
                 # o a través de 'kde_kws' o 'hist_kws' si se usan con 'kind' apropiado
                 # y tu versión de seaborn los soporta para estilos específicos (no para 'cumulative').
                 # Por ejemplo, para colores: color='skyblue'
                )

# Si quieres superponer un KDE acumulativo, podrías hacerlo por separado o asegurarte
# de que tu versión de displot lo soporte con el mismo llamado:
# ax = sns.displot(x=datos.Edad, cumulative=True, kind='kde') # Para solo KDE acumulativo

# Para tener ambos (hist y kde acumulativos) en la misma figura con displot,
# la forma más sencilla es usar 'kind' y 'cumulative' como se muestra.
# Sin embargo, displot generalmente crea un histograma O una KDE, no ambos fácilmente superpuestos
# si quieres que ambos sean acumulativos en la misma llamada de displot y con el mismo axis.
# Si la intención es un HISTOGRAMA acumulativo con una KDE acumulativa superpuesta,
# quizás sea mejor usar un 'histplot' directamente.

# Usando histplot para histograma acumulativo y kdeplot para la KDE acumulativa:
# Esto te da más control y es más claro si quieres ambas superpuestas.

# Crea la figura y el eje si aún no lo tienes
fig, ax = plt.subplots(figsize=(10, 5))

sns.histplot(x=datos.Edad,
             cumulative=True,
             bins=10,
             ax=ax,
             color='skyblue', # Color del histograma
             alpha=0.7 # Transparencia
            )

sns.kdeplot(x=datos.Edad,
            cumulative=True,
            ax=ax,
            color='red', # Color de la línea KDE
            linewidth=2,
            linestyle='--'
           )

ax.set_title("Distribución de frecuencia Acumulativa", fontsize=18)
ax.set_xlabel("Edad (Años)", fontsize=14) # Cambiado a "Edad (Años)" para mayor claridad
ax.set_ylabel("Frecuencia Acumulada", fontsize=14) # Ajustado a "Frecuencia Acumulada"

plt.grid(True, linestyle='--', alpha=0.6) # Añade una cuadrícula para mejor lectura
plt.show()


#  boxplot
ax = sns.boxplot(x = 'Altura', data= datos, orient='h', color='lightblue')

ax.figure.set_size_inches(10, 5)  # Ajusta el tamaño de la figura
ax.set_title('Altura de los participantes', fontsize=16)  # Título del gráfico
ax.set_xlabel('Altura (cm)', fontsize=14)  # Etiqueta del eje

plt.show()  # Muestra el gráfico

ax = sns.boxplot(x = 'Altura', y= 'Sexo', data= datos, orient='h', color='lightblue')

ax.figure.set_size_inches(10, 5)  # Ajusta el tamaño de la figura
ax.set_title('Altura de los participantes', fontsize=16)  # Título del gráfico
ax.set_xlabel('Altura (cm)', fontsize=14)  # Etiqueta del eje

plt.show()  # Muestra el gráfico