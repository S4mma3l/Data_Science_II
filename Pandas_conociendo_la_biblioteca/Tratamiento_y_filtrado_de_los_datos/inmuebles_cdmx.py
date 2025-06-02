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

print(df.isnull().sum()) # Muestra la cantidad de valores nulos en cada columna del DataFrame filtrado
print(df.fillna(0))  # Rellena los valores nulos con 0

df = df.fillna(0)  # Rellena los valores nulos con 0
print(df.isnull().sum())  # Muestra la cantidad de valores nulos en cada columna del DataFrame

# remover registros inconsistentes

print(df.query('Valor == 0 | Condominio == 0').index)  # Filtra el DataFrame para mostrar solo los registros con 'Valor' menor a 0

df_remover = df.query('Valor == 0 | Condominio == 0').index  # Filtra el DataFrame para mostrar solo los registros con 'Valor' menor a 0
df.drop(df_remover,axis=0, inplace=True)  # Elimina los registros con 'Valor' menor a 0

print(df.query('Valor == 0 | Condominio == 0').index)

df.drop('Tipo', axis=1, inplace=True)  # Elimina la columna 'Tipo' del DataFrame
print(df.head(5))  # Muestra las primeras 5 filas del DataFrame filtrado

# Apartamentos que  tienen 1 dormitorio y un alquiler menor a MXM 4200

seleccion1 = df['Habitaciones'] == 1  # Filtra el DataFrame para mostrar solo los apartamentos con 1 dormitorio
print(seleccion1)  # Muestra la selección de apartamentos con 1 dormitorio
print(type(seleccion1))  # Muestra el tipo de objeto

df[seleccion1]  # Muestra el DataFrame filtrado para mostrar solo los apartamentos con 1 dormitorio
print(df[seleccion1]) # Muestra el DataFrame filtrado para mostrar solo los apartamentos con 1 dormitorio

seleccion2 = df['Valor'] < 4200  # Filtra el DataFrame para mostrar solo los apartamentos con alquiler menor a 4200
print(df[seleccion2])  # Muestra el DataFrame filtrado para mostrar solo los apartamentos con alquiler menor a 4200
print(df[seleccion2].max())  # Muestra el valor máximo del DataFrame filtrado
print(df[seleccion2].min())  # Muestra el valor mínimo del DataFrame filtrado

filtro1 = (seleccion1) & (seleccion2)  # Combina las selecciones para filtrar el DataFrame
print(df[filtro1])  # Muestra el DataFrame filtrado

df1 = df[filtro1]  # Crea un nuevo DataFrame con los apartamentos filtrados
print(df1)  # Muestra el nuevo DataFrame con los apartamentos filtrados

# Apartamentos que tienen al menos 2 dormitorios, un alquiler menos a MXN 10500 y una superficie mayor a 70 m2

filtro2 = (df['Habitaciones'] >= 2) & (df['Valor'] < 10500) & (df['Area'] > 70)  # Filtra el DataFrame para mostrar solo los apartamentos con al menos 2 dormitorios, alquiler menor a 10500 y superficie mayor a 70 m2
print(df[filtro2])  # Muestra el DataFrame filtrado

df2 = df[filtro2]  # Crea un nuevo DataFrame con los apartamentos filtrados
print(df2)  # Muestra el nuevo DataFrame con los apartamentos filtrados