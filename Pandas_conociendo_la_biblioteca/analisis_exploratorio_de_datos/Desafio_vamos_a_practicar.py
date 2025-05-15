import pandas as pd
import matplotlib.pyplot as plt

url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'
inmuebles = pd.read_csv(url, sep=';')
inmuebles_comerciales = ['Conjunto Comercial/Sala', 'Edificio Completo',
                          'Tienda/Salón', 'Casa Comercial', 'Terreno Estándar',
                          'Cochera/Estacionamiento', 'Galpón/Depósito/Almacén',
                          'Tienda en Centro Comercial', 'Hotel',
                          'Loteo/Condominio', 'Industria',
                          'Galpón/Depósito/Almacén']
df = inmuebles.query('Tipo not in @inmuebles_comerciales')
df = df.query('Tipo == "Departamento"')

# 1. Calcular el promedio de habitaciones por departamento.
promedio_habitaciones_departamento = df['Habitaciones'].mean()
print(f"{promedio_habitaciones_departamento:.2f}")

# 2. Verificar cuántas colonias únicas existen en nuestra base de datos.
cantidad_colonias_unicas = df['Colonia'].nunique()
print(cantidad_colonias_unicas)

# 3. Analizar qué colonias tienen el promedio de alquiler más alto.
promedio_alquiler_por_colonia = df.groupby('Colonia')['Valor'].mean().sort_values(
    ascending=False)
print(promedio_alquiler_por_colonia.head().to_string())

# 4. Crear un gráfico de barras horizontales que muestre las 5 colonias con los
# promedios de alquiler más altos.
promedio_alquiler_por_colonia.head().plot(kind='barh', figsize=(10, 6),
                                        color='skyblue')
plt.show()