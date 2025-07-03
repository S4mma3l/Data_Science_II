import pandas as pd

datos = pd.read_csv("Data_Science_probando_relaciones_con_regresión _ineal\\Ajustando_una_recta\\datos\\precios_casas.csv")

print(datos.head())

datos = datos.drop(columns= 'Id')

print(datos.columns)

corr = datos.corr()

print(corr['precio_de_venta'])

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

plt.scatter(datos['area_primer_piso'], datos['precio_de_venta'])
plt.title('Relacion entre el precio y el area')
plt.xlabel('Area en M2')
plt.ylabel('Precio en USD')
plt.show()

plt.scatter(datos['area_primer_piso'], datos['precio_de_venta'])
plt.axline(xy1=(40, 300000), xy2=(175, 1500000), color='red')
plt.title('Relacion entre el precio y el area')
plt.xlabel('Area en M2')
plt.ylabel('Precio en USD')
plt.show()

px.scatter(datos, x='area_primer_piso', y='precio_de_venta', trendline_color_override='red', trendline='ols')
plt.show()