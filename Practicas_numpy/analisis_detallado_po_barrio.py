import pandas as pd
import matplotlib.pyplot as plt

# 1. Carga los datos
url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'
inmuebles = pd.read_csv(url, sep=';')
print("Primeras filas del DataFrame:\n", inmuebles.head())

# 2. Explora los datos (opcional, pero recomendado para recordar la estructura)
print("\nInformación general del DataFrame:\n", inmuebles.info())

# 3. Calcula el precio de alquiler promedio, habitaciones promedio y baños promedio por barrio
#    - `groupby('Barrio')`: Agrupa el DataFrame por la columna 'Barrio'. Esto crea grupos donde todos los registros
#      pertenecen al mismo barrio.
#    - `[['Valor', 'Habitaciones', 'Banos']].mean()`: Selecciona las columnas 'Valor', 'Habitaciones' y 'Banos'
#      dentro de cada grupo (barrio) y calcula la media (promedio) de sus valores. El doble corchete `[['...']]`
#      se usa para obtener un DataFrame como resultado.
promedio_por_barrio = inmuebles.groupby('Barrio')[['Valor', 'Habitaciones', 'Banos']].mean()
print("\nPromedio de alquiler, habitaciones y baños por barrio:\n", promedio_por_barrio)

# 4. Identifica el barrio con el alquiler promedio más alto y más bajo
#    - `sort_values('Valor', ascending=False)`: Ordena el DataFrame `promedio_por_barrio` según la columna 'Valor'
#      de forma descendente (`ascending=False`), de mayor a menor.
barrio_mayor_promedio = promedio_por_barrio.sort_values('Valor', ascending=False).iloc[0]
#    - `.iloc[0]`: Selecciona la primera fila del DataFrame ordenado, que corresponde al barrio con el mayor promedio.
print("\nBarrio con el alquiler promedio más alto:\n", barrio_mayor_promedio)

barrio_menor_promedio = promedio_por_barrio.sort_values('Valor', ascending=True).iloc[0]
#    - `sort_values('Valor', ascending=True)`: Ordena de forma ascendente (de menor a mayor).
#    - `.iloc[0]`: Selecciona la primera fila, que ahora es el barrio con el menor promedio.
print("\nBarrio con el alquiler promedio más bajo:\n", barrio_menor_promedio)

# 5. Determina la cantidad de propiedades de cada tipo en cada barrio
#    - `groupby(['Barrio', 'Tipo'])`: Agrupa el DataFrame por dos columnas: primero por 'Barrio' y luego, dentro de cada
#      barrio, por 'Tipo' de inmueble.
#    - `.size()`: Calcula el tamaño (la cantidad de filas) de cada grupo resultante.
#    - `.unstack()`: Transforma el resultado de la agrupación. Si 'Tipo' era un índice, ahora se convierte en columnas,
#      y los valores son los conteos. Los valores faltantes (barrios sin un tipo específico) se llenan con `NaN`.
cantidad_por_tipo_barrio = inmuebles.groupby(['Barrio', 'Tipo']).size().unstack(fill_value=0)
#    - `fill_value=0`: Reemplaza los valores `NaN` con 0 para una mejor visualización.
print("\nCantidad de propiedades por tipo en cada barrio:\n", cantidad_por_tipo_barrio)

# 6. Crea un gráfico de barras del precio de alquiler promedio para los 10 barrios más caros
#    - `promedio_por_barrio.sort_values('Valor', ascending=False)`: Ordena los barrios por su alquiler promedio de mayor a menor.
#    - `.head(10)`: Selecciona las primeras 10 filas, correspondientes a los 10 barrios más caros.
#    - `.plot(kind='bar', figsize=(12, 6))`: Crea un gráfico de barras. `kind='bar'` especifica el tipo de gráfico,
#      y `figsize` establece el tamaño de la figura.
promedio_top_10_barrios = promedio_por_barrio.sort_values('Valor', ascending=False).head(10)
promedio_top_10_barrios['Valor'].plot(kind='bar', figsize=(12, 6), color='skyblue')
plt.title('Precio de Alquiler Promedio para los 10 Barrios Más Caros')
plt.xlabel('Barrio')
plt.ylabel('Precio Promedio')
plt.xticks(rotation=45, ha='right') # Rotar las etiquetas del eje x para mejor legibilidad
plt.tight_layout() # Ajusta el diseño para evitar que las etiquetas se superpongan
plt.show()

# 7. Selecciona propiedades en un barrio específico y muestra estadísticas descriptivas
barrio_seleccionado = 'Chapinero' # Elige el barrio que quieras analizar
propiedades_barrio = inmuebles.query('Barrio == @barrio_seleccionado')
#    - `query('Barrio == @barrio_seleccionado')`: Filtra el DataFrame `inmuebles` para seleccionar solo las filas donde
#      la columna 'Barrio' es igual al valor de la variable `barrio_seleccionado`. El `@` se usa para referenciar
#      variables Python dentro de la consulta de `query()`.
print(f"\nPropiedades en el barrio de {barrio_seleccionado}:\n", propiedades_barrio.head())

estadisticas_barrio = propiedades_barrio[['Valor', 'Habitaciones', 'Banos']].describe()
#    - `[['Valor', 'Habitaciones', 'Banos']]`: Selecciona las columnas numéricas para las que queremos las estadísticas.
#    - `.describe()`: Genera estadísticas descriptivas como la media, la desviación estándar, el mínimo, el máximo y los
#      cuartiles para cada columna seleccionada.
print(f"\nEstadísticas descriptivas de las propiedades en {barrio_seleccionado}:\n", estadisticas_barrio)