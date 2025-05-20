import pandas as pd
import matplotlib.pyplot as plt

# 1. Carga los datos
url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'
inmuebles = pd.read_csv(url, sep=';')

# 2. Filtra para incluir solo inmuebles residenciales
inmuebles_comerciales = ['Conjunto Comercial/Sala', 'Edificio Completo', 'Tienda/Salón', 'Casa Comercial',
                        'Terreno Estándar', 'Cochera/Estacionamiento', 'Galpón/Depósito/Almacén',
                        'Tienda en Centro Comercial', 'Hotel', 'Loteo/Condominio', 'Industria']
inmuebles_residenciales = inmuebles.query('Tipo not in @inmuebles_comerciales')
#    - `query('Tipo not in @inmuebles_comerciales')`: Selecciona las filas donde el valor de la columna 'Tipo'
#      NO (`not in`) está presente en la lista `inmuebles_comerciales`.
print("\nPrimeras filas de inmuebles residenciales:\n", inmuebles_residenciales.head())

# 3. Calcula el valor del alquiler promedio por tipo de inmueble residencial
promedio_alquiler_por_tipo_residencial = inmuebles_residenciales.groupby('Tipo')['Valor'].mean().sort_values()
#    - `groupby('Tipo')`: Agrupa por el tipo de inmueble.
#    - `['Valor'].mean()`: Calcula el promedio del 'Valor' para cada tipo.
#    - `.sort_values()`: Ordena los resultados por el valor promedio del alquiler.
print("\nValor del alquiler promedio por tipo de inmueble residencial:\n", promedio_alquiler_por_tipo_residencial)

# 4. Determina la cantidad promedio de habitaciones y baños por tipo de inmueble residencial
promedio_caracteristicas_por_tipo = inmuebles_residenciales.groupby('Tipo')[['Habitaciones', 'Banos']].mean()
#    - `[['Habitaciones', 'Banos']]`: Selecciona las columnas 'Habitaciones' y 'Banos' para calcular el promedio.
print("\nPromedio de habitaciones y baños por tipo de inmueble residencial:\n", promedio_caracteristicas_por_tipo)

# 5. Crea un gráfico de barras comparando el valor del alquiler promedio
promedio_alquiler_por_tipo_residencial.plot(kind='barh', figsize=(10, 6), color='lightcoral')
#    - `.plot(kind='barh', ...)`: Crea un gráfico de barras horizontales.
plt.title('Valor del Alquiler Promedio por Tipo de Inmueble Residencial')
plt.xlabel('Valor Promedio')
plt.ylabel('Tipo de Inmueble')
plt.tight_layout()
plt.show()

# 6. Utiliza groupby() y agg() para calcular múltiples estadísticas del valor del alquiler
estadisticas_alquiler_por_tipo = inmuebles_residenciales.groupby('Tipo')['Valor'].agg(['mean', 'median', 'std', 'min', 'max', 'count'])
#    - `.agg(['mean', 'median', 'std', 'min', 'max', 'count'])`: Aplica múltiples funciones de agregación a la columna 'Valor'
#      para cada grupo ('Tipo').
#        - 'mean': Calcula la media (promedio).
#        - 'median': Calcula la mediana (el valor central).
#        - 'std': Calcula la desviación estándar (la dispersión de los datos).
#        - 'min': Encuentra el valor mínimo.
#        - 'max': Encuentra el valor máximo.
#        - 'count': Cuenta el número de observaciones en cada grupo.
print("\nEstadísticas del valor del alquiler por tipo de inmueble residencial:\n", estadisticas_alquiler_por_tipo)