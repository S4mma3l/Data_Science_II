import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import yellowbrick
import matplotlib.pyplot as plt

print(f'Versión de pandas: {pd.__version__}')
print(f'Versión de numpy: {np.__version__}')
print(f'Versión de scikit-learn (sklearn): {sklearn.__version__}')
print(f'Versión de seaborn: {sns.__version__}')
print(f'Versión de yellowbrick: {yellowbrick.__version__}')

datos = pd.read_csv('IA_aumentada_previsión_de_atrasos_de_vuelos\\explorando_los_datos\\datos\\flights.csv')
print(f'Número de filas en el DataFrame: {datos.shape[0]}')
print(datos.head())
print(datos.info())
print(datos.describe(include='O'))

avg_delay = datos.groupby('airline')['delay'].mean().reset_index()
sns.barplot(x='airline', y='delay', data=avg_delay)
plt.title('Companias aerea vs atraso promedio')
plt.xlabel('Compañía Aérea')
plt.ylabel('Atraso Promedio (minutos)')
plt.show()

sns.countplot(x='airline', data=datos)
plt.title('Número de vuelos por compañía aérea')
plt.xlabel('Compañía Aérea')
plt.ylabel('Número de Vuelos')
plt.show()

avg_delay = datos.groupby('schengen')['delay'].mean().reset_index()
sns.barplot(x='schengen', y='delay', data=avg_delay)
plt.title('tipo de vuelo vs atraso promedio')
plt.xlabel('tipo de vuelo')
plt.ylabel('Atraso Promedio (minutos)')
plt.show()

sns.countplot(x='schengen', data=datos)
plt.title('Número de vuelos por tipo')
plt.xlabel('tipo de vuelo')
plt.ylabel('Número de Vuelos')
plt.show()

avg_delay = datos.groupby('is_holiday')['delay'].mean().reset_index()
sns.barplot(x='is_holiday', y='delay', data=avg_delay)
plt.title('Dias feriados vs atraso promedio')
plt.xlabel('Dias feriados')
plt.ylabel('Atraso Promedio (minutos)')
plt.show()


orden = datos['aircraft_type'].value_counts().index
sns.countplot(x='aircraft_type', data=datos, order=orden)
plt.title('Número de vuelos por tipo de aeronave')
plt.xticks(rotation=70)
plt.xlabel('tipo de Aeronave')
plt.ylabel('Número de Vuelos')
plt.show()

sns.histplot(data=datos, x='arrival_time', bins=30, kde=True)
plt.show()

# Formula para en ancho de las barras de un histograma

def ancho_bins(df, columna):
    q75, q25 = np.percentile(df[columna], [75, 25])
    iqr = q75 - q25
    ancho = 2 * iqr * np.power(len(df[columna]), -1/3)
    return ancho

binwidth = ancho_bins(datos, 'arrival_time')
print(f'Ancho de las barras del histograma: {binwidth}')

sns.histplot(data=datos, x='arrival_time', binwidth=binwidth, kde=True)
plt.show()

binwidth = ancho_bins(datos, 'departure_time')
sns.histplot(data=datos, x='departure_time', binwidth=binwidth, kde=True)
plt.show()

atraso_promedio = datos['delay'].mean()
atraso_mediana = datos['delay'].median()

fig, ax = plt.subplots(1, 2, figsize=(9, 4))

sns.boxplot(data=datos, y='delay', ax=ax[0])
ax[0].set_title('Boxplot de Atrasos')
ax[0].axhline(y=atraso_promedio, color='r', linestyle='--', label='Atraso Promedio')
ax[0].legend()

binwidth = ancho_bins(datos, 'delay')
sns.histplot(data=datos, x='delay', binwidth=binwidth, kde=True, ax=ax[1])
plt.ylabel('Numero de vuelos')
plt.grid(False)
ax[1].set_title('Histograma de Atrasos')
ax[1].axvline(x=atraso_promedio, color='r', linestyle='--', label='Atraso Promedio')
ax[1].axvline(x=atraso_mediana, color='g', linestyle='--', label='Atraso Mediano')
ax[1].legend()
plt.tight_layout()
plt.show()