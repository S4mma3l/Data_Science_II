import pandas as pd
# Importar un archivo CSV
datos = pd.read_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\Leyendo_archivos_CSV\data\superstore_data.csv') # Ruta del archivo CSV
# Mostrar las primeras filas del DataFrame
print(datos.head())

datos = pd.read_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\Leyendo_archivos_CSV\data\superstore_data.csv', nrows= 5) 
print("mostrando solo las primeras 5 filas del DataFrame con nrows")
print(datos)

datos = pd.read_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\Leyendo_archivos_CSV\data\superstore_data.csv', nrows= 5, usecols=['Id', 'Year_Birth', 'Income']) # Especificar las columnas que se desean importar
print("mostrando solo las primeras 5 filas del DataFrame con nrows y usecols")
print(datos)

datos = pd.read_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\Leyendo_archivos_CSV\data\superstore_data.csv', usecols=[0,1,4]) # Especificar las columnas por índice
print("mostrando solo las primeras 5 filas del DataFrame con usecols por índice")
print(datos.head())

# Guardar el DataFrame en un nuevo archivo CSV
datos.to_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\Leyendo_archivos_CSV\data\superstore_data_guardado.csv', index=False) # Guardar sin el índice

clientes_mercado = pd.read_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\Leyendo_archivos_CSV\data\superstore_data_guardado.csv') # Especificar la codificación si es necesario
print("mostrando el DataFrame guardado")
print(clientes_mercado.head())

# Importar un archivo CSV con un separador diferente
datos2 = pd.read_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\Leyendo_archivos_CSV\data\superstore_data_punto_coma.csv', sep=';') # Especificar el separador si es necesario

# Mostrar las primeras filas del segundo DataFrame
print("mostrando el DataFrame con separador punto y coma")
print(datos2.head())