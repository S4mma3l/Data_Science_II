import pandas as pd

datos = pd.read_csv('Regrecion_lineal_Tecnicas_avanzadas_de_modelado\\analisis_preliminar\\datos\\dataset.csv', sep=';')

print(datos.head())

print(datos.shape)
print(len(datos.columns))

print(datos.describe().round(2))

# Matriz de correlacion

print(datos.corr().round(2))