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
from sklearn.model_selection import train_test_split
from statsmodels.formula.api import ols





sns.displot(datos['precio_de_venta'], kde = True, color='green')
plt.title('Distribucion del precio de venta de las casas')
# plt.show()

y = datos['precio_de_venta']
x = datos.drop(columns = 'precio_de_venta')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=230)

df_train = pd.DataFrame(x_train)
df_train['precio_de_venta'] = y_train

modelo_0 = ols('precio_de_venta ~ area_primer_piso', data=df_train).fit()
print(modelo_0.params)
print(modelo_0.summary())

print(modelo_0.rsquared)

print(modelo_0.resid)

modelo_0.resid.hist()
plt.title('Distribucion de los residuos del modelo 0')
# plt.show()

y_predict = modelo_0.predict(x_test)

from sklearn.metrics import r2_score

print(f' El coeficiente de determinacion del modelo 0 es R2 {round(r2_score(y_test, y_predict),2)}')








