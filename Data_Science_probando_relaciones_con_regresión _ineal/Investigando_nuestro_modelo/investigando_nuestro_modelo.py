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

sns.pairplot(datos, y_vars=['area_primer_piso', 'area_segundo_piso', 'cantidad_banos'], x_vars=['precio_de_venta'])
# plt.show()

import statsmodels.api as sm

x_train = sm.add_constant(x_train)
print(x_train.head())

print(x_train.columns)


modelo_1 = sm.OLS(y_train, x_train[['const', 'area_primer_piso', 'tiene_segundo_piso', 'area_segundo_piso',
       'cantidad_banos', 'capacidad_carros_garage',
       'calidad_de_cocina_excelente']]).fit()

modelo_2 = sm.OLS(y_train, x_train[['const', 'area_primer_piso', 'tiene_segundo_piso', 
       'cantidad_banos', 'capacidad_carros_garage',
       'calidad_de_cocina_excelente']]).fit()

modelo_3 = sm.OLS(y_train, x_train[['const', 'area_primer_piso', 'tiene_segundo_piso', 
       'cantidad_banos', 'calidad_de_cocina_excelente']]).fit()

modelos =[modelo_0, modelo_1, modelo_2, modelo_3]

for i,j in enumerate(modelos):
    print(f'********************************\n********* El modelo {i} tiene el siguiente resumen ***********\n*************************')
    print(j.summary(),'\n\n')

for i,j in enumerate(modelos):
    print(f'El coeficiente de determinacion del modelo {i} es R2 {round(j.rsquared,2)}')

print(modelo_3.params)

from statsmodels.stats.outliers_influence import variance_inflation_factor as vif

explicativas_1 = ['const', 'area_primer_piso', 'tiene_segundo_piso', 'area_segundo_piso',
       'cantidad_banos', 'capacidad_carros_garage',
       'calidad_de_cocina_excelente']

explicativas_2 = ['const', 'area_primer_piso', 'tiene_segundo_piso', 
       'cantidad_banos', 'capacidad_carros_garage',
       'calidad_de_cocina_excelente']

explicativas_3 = ['const', 'area_primer_piso', 'tiene_segundo_piso', 
       'cantidad_banos', 'calidad_de_cocina_excelente']

# VIF

vif_1 =pd.DataFrame()
vif_1['variables'] = explicativas_1
vif_1['VIF'] = [vif(x_train[explicativas_1], i) for i in range(len(explicativas_1))]

print(vif_1)

vif_3 =pd.DataFrame()
vif_3['variables'] = explicativas_3
vif_3['VIF'] = [vif(x_train[explicativas_3], i) for i in range(len(explicativas_3))]

print(vif_3)

y_previsto_train = modelo_3.predict(x_train[explicativas_3])

fig = px.scatter(y=y_train, x=y_previsto_train, title='Valor Previsto vs Valor Real',
                 labels={'x': 'Valor Previsto', 'y': 'Valor Real'})
fig.show()

# residuos

residuos = modelo_3.resid
fig = px.scatter(y=residuos, x=y_previsto_train, title='Valor Previsto vs residuos',
                 labels={'x': 'Valor Previsto', 'y': 'residuos'})
fig.show()

