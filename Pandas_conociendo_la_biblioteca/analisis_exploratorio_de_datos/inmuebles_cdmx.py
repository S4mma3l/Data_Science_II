import pandas as pd
import matplotlib.pyplot as plt


url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'
# Cargar el archivo CSV desde la URL

inmuebles = pd.read_csv(url, sep=';')
print(inmuebles.head(10))  # Muestra las primeras filas del DataFrame
# para obtener ejemplos de los datos seria inmuebles.sample(10)
# para obtener los ultimos datos seria inmuebles.tail(10)

print(type(inmuebles))  # Muestra el tipo de objeto

# Caracteristicas generales del DataFrame
# exploracion inicial de los datos
print(inmuebles.sample(5))  # Muestra 5 filas aleatorias del DataFrame
print(inmuebles.shape)  # Muestra la forma del DataFrame (filas, columnas)
print(inmuebles.columns)  # Muestra los nombres de las columnas
print(inmuebles.info())  # Muestra información general del DataFrame
print(inmuebles['Tipo'])
print(inmuebles[['Habitaciones', 'Valor']])  # Muestra las columnas 'Habitaciones' y 'Valor'

# Demandas de ML
# Cuales son los valores promedio de alquiler por tipo de propiedad

print(inmuebles["Valor"].mean())  # Muestra el valor promedio de la columna 'Valor'

df_tipo_precio = inmuebles.groupby('Tipo')[['Valor']].mean().sort_values('Valor')  # Agrupa por 'Tipo' y calcula el promedio de 'Valor' y lo ordena
print(df_tipo_precio)  # Muestra el promedio de 'Valor' por 'Tipo'

# df_tipo_precio.plot(kind='barh', figsize=(12, 8), color='purple')  # Crea un gráfico de barras horizontal del DataFrame
# plt.show()  # Muestra el gráfico

print(inmuebles.Tipo.unique())  # Muestra los tipos únicos de propiedades

inmuebles_comerciales = ['Conjunto Comercial/Sala', 'Edificio Completo', 'Tienda/Salón', 'Casa Comercial', 
                         'Terreno Estándar', 'Cochera/Estacionamiento', 'Galpón/Depósito/Almacén', 
                         'Tienda en Centro Comercial', 'Hotel', 'Loteo/Condominio', 'Industria', 'Galpón/Depósito/Almacén']  # Obtiene los tipos únicos de propiedades

print(inmuebles.query('@inmuebles_comerciales not in Tipo'))  # Muestra las propiedades que no están en la lista de inmuebles comerciales

df = inmuebles.query('Tipo not in @inmuebles_comerciales')  # Filtra el DataFrame para excluir los inmuebles comerciales


df_tipo_precio = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')  # Agrupa por 'Tipo' y calcula el promedio de 'Valor' y lo ordena
print(df_tipo_precio)  # Muestra el promedio de 'Valor' por 'Tipo'
# df_tipo_precio.plot(kind='barh', figsize=(12, 8), color='purple')  # Crea un gráfico de barras horizontal del DataFrame
# plt.show()  # Muestra el gráfico


# Porcentaje de cada tipo de inmueble presente en nuestra base de datos

print(df.Tipo.unique())  # Muestra los tipos únicos de propiedades
print(df.Tipo.value_counts(normalize= True))  # Muestra el conteo de cada tipo de propiedad normalizado (porcentaje)

porcetaje_tipo = df.Tipo.value_counts(normalize=True).to_frame()  # Crea un DataFrame con el conteo normalizado de cada tipo de propiedad
porcetaje_tipo.plot(kind='barh', figsize=(12, 8), color='green', xlabel= 'Porcentajes', ylabel= 'Tipos')  # Crea un gráfico de barras horizontal del DataFrame
# plt.show()  # Muestra el gráfico

print(df.query('Tipo == "Departamento"'))  # Filtra el DataFrame para mostrar solo los departamentos

df = df.query('Tipo == "Departamento"')  # Filtra el DataFrame para mostrar solo los departamentos
print(df.head(5))  # Muestra las primeras 5 filas del DataFrame filtrado

print(df.shape)  # Muestra la forma del DataFrame filtrado (filas, columnas)
