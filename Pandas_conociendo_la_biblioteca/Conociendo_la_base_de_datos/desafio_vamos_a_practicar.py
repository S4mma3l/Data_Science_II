import pandas as pd

url = 'https://gist.githubusercontent.com/ahcamachod/807a2c1cf6c19108b2b701ea1791ab45/raw/fb84f8b2d8917a89de26679eccdbc8f9c1d2e933/alumnos.csv'

alumnos = pd.read_csv(url)
print(alumnos.head(7))  # Muestra las primeras filas del DataFrame
print(alumnos.tail(5))  # Muestra las últimas filas del DataFrame
print(alumnos.shape)  # Muestra la forma del DataFrame (filas, columnas)
print(alumnos.info())  # Muestra información general del DataFrame

# Calcula las estadísticas descriptivas
estadisticas_descriptivas = alumnos.describe()

# Imprime las estadísticas descriptivas
print(estadisticas_descriptivas)