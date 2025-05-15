import pandas as pd

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

