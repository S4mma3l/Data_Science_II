import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import yellowbrick

print(f'Versión de pandas: {pd.__version__}')
print(f'Versión de numpy: {np.__version__}')
print(f'Versión de scikit-learn (sklearn): {sklearn.__version__}')
print(f'Versión de seaborn: {sns.__version__}')
print(f'Versión de yellowbrick: {yellowbrick.__version__}')

datos = pd.read_csv('IA_aumentada_previsión_de_atrasos_de_vuelos\\explorando_los_datos\\datos\\flights.csv')
print(f'Número de filas en el DataFrame: {datos.shape[0]}')
print(datos.head())
print(datos.info())
print(datos.describe(include='O'))