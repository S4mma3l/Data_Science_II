import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import yellowbrick
import matplotlib.pyplot as plt


datos = pd.read_csv('IA_aumentada_previsión_de_atrasos_de_vuelos\\explorando_los_datos\\datos\\flights.csv')
print(f'Número de filas en el DataFrame: {datos.shape[0]}')
print(datos.head())
print(datos.info())
print(datos.describe(include='O'))



# Formula para en ancho de las barras de un histograma

def ancho_bins(df, columna):
    q75, q25 = np.percentile(df[columna], [75, 25])
    iqr = q75 - q25
    ancho = 2 * iqr * np.power(len(df[columna]), -1/3)
    return ancho

atraso_promedio = datos['delay'].mean()
atraso_mediana = datos['delay'].median()

print(datos.columns)

datos['date'] = datos['year'].astype(str) + '-' + (datos['day']+1).astype(str)
datos['date'] = pd.to_datetime(datos['date'], format='%Y-%j')
print(datos.head(2))

datos['is_weekend'] = datos['date'].dt.weekday.isin([5, 6])
datos['day_name'] = datos['date'].dt.day_name()
print(datos.sample(5))
print(datos.info())

import warnings
warnings.filterwarnings('ignore')

datos['schengen'] = datos['schengen'].replace({'schengen':1, 'non-schengen':0})
datos['is_holiday'] = datos['is_holiday'].replace({True :1 , False :0})
datos['is_weekend'] = datos['is_weekend'].replace({True :1 , False :0})

print(datos.sample(5))

categoricas = ['airline', 'aircraft_type', 'origin', 'day_name']

datos_codificados = pd.get_dummies(datos, columns=categoricas, dtype=int)
print(datos_codificados.sample(5))

# Limpieza de datos
print(datos[['arrival_time', 'departure_time']].corr())

df = datos_codificados.drop(columns=['flight_id', 'departure_time', 'day', 'year', 'date'])
print(df.sample(10))