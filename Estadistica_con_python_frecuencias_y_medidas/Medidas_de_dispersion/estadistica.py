import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

datos = pd.read_csv("Estadistica_con_python_frecuencias_y_medidas\\Introduccion_a_la_estadistica_y_cuales_son_los_tipos_de_datos\\datos\\datos.csv")

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

notas_maria_dispersion = df[['María']]

notas_media_maria = notas_maria_dispersion.mean()[0]
print(f"Media de las notas de María: {notas_media_maria}")

notas_maria_dispersion['Desviacion'] = notas_maria_dispersion['María'] - notas_media_maria
print(notas_maria_dispersion)

notas_maria_dispersion['|Desviacion|'] = notas_maria_dispersion['Desviacion'].abs()
print(notas_maria_dispersion)

mad_notas_maria = stats.median_abs_deviation(notas_maria_dispersion['María'])
print(f"Desviación absoluta mediana de las notas de María: {mad_notas_maria}")

# Varianza
notas_maria_dispersion['(Desviacion)^2'] = notas_maria_dispersion['Desviacion'].pow(2)
print(notas_maria_dispersion)

notas_maria_dispersion['(Desviacion)^2'].sum() / (len(notas_maria_dispersion) - 1)
print(f"Varianza de las notas de María: {notas_maria_dispersion['(Desviacion)^2'].sum() / (len(notas_maria_dispersion) - 1)}")

notas_maria_dispersion['María'].var()
print(f"Varianza de las notas de María (usando pandas): {notas_maria_dispersion['María'].var()}")

# Desviación estándar
notas_maria_dispersion['Desviacion_Estandar'] = notas_maria_dispersion['(Desviacion)^2'].pow(0.5)
print(notas_maria_dispersion)

varianza_maria = notas_maria_dispersion['María'].var()

np.sqrt(varianza_maria)
print(f"Desviación estándar de las notas de María: {np.sqrt(varianza_maria)}")

desviacion_estandar_maria = notas_maria_dispersion['María'].std()
print(f"Desviación estándar de las notas de María (usando pandas): {desviacion_estandar_maria}")

df.mean() # Media
df.median() # Mediana
df.mode() # Moda
df.var() # Varianza
df.std() # Desviación estándar
print(f'la mediana de todo el dataframe es: {df.median()}'
      f'la moda de todo el dataframe es: {df.mode().iloc[0]}'
      f'la varianza de todo el dataframe es: {df.var()}'
      f'la desviación estándar de todo el dataframe es: {df.std()}',
      f'la media de todo el dataframe es: {df.mean()}')

data = pd.DataFrame(data = {'Maria': [7],
                          'Pedro': [6],
                          'Pablo': [8],
                          'Juan': [7.5],
                          'Ana': [6.5],
                          'Luis': [8.5]},
                          index=['Horas']
                          )

print(data)
data.std() # Desviación estándar
print(f'la desviación estándar de las horas es: {data.std(1)}')