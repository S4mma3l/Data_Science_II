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

