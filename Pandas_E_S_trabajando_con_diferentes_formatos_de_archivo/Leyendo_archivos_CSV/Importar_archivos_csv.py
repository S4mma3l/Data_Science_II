import pandas as pd
# Importar un archivo CSV
datos = pd.read_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\Leyendo_archivos_CSV\data\superstore_data.csv', sep=',')  # Especificar el separador si es necesario

# Mostrar las primeras filas del DataFrame
print(datos.head())

datos2 = pd.read_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\Leyendo_archivos_CSV\data\superstore_data_punto_coma.csv', sep=';') # Especificar el separador si es necesario

# Mostrar las primeras filas del segundo DataFrame
print(datos2.head())