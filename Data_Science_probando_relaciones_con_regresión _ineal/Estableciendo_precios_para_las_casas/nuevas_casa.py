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

x_test = sm.add_constant(x_test)

print(x_test.head(2))

prevision_3 = modelo_3.predict(x_test[['const', 'area_primer_piso', 'tiene_segundo_piso', 
       'cantidad_banos', 'calidad_de_cocina_excelente']])

print(f'El coeficiente r2 de la base de prevision es: {modelo_3.rsquared.round(2)}')

print(f'El coeficiente r2 con respecto a la base de entrenamiento es: {round(r2_score(y_test, prevision_3),2)}')


nuevo_inmueble = pd.DataFrame({
    'const': [1],
    'area_primer_piso': [120],
    'tiene_segundo_piso': [1],
    'cantidad_banos': [2],
    'calidad_de_cocina_excelente': [0]
})

print(modelo_0.predict(nuevo_inmueble['area_primer_piso']).round(2))

print(modelo_3.predict(nuevo_inmueble).round(2))

nuevas_casas = pd.read_csv('Data_Science_probando_relaciones_con_regresión _ineal\\Estableciendo_precios_para_las_casas\\datos\\nuevas_casas.csv', sep=';')

print(nuevas_casas.head(2))

modelo_3 = sm.OLS(y_train, x_train[['const', 'area_primer_piso', 'tiene_segundo_piso', 
       'cantidad_banos', 'calidad_de_cocina_excelente']]).fit()

nuevas_casas.drop(columns='Casa', inplace=True)

print(nuevas_casas)

# anadiendo una constante

nuevas_casas = sm.add_constant(nuevas_casas)

print(nuevas_casas.head(2))

# precio_casas = pd.DataFrame()
nuevas_casas['Precio de venta'] = modelo_3.predict(nuevas_casas).round(2)

print(nuevas_casas)

# Manos a la obra: estimando el valor de una casa

nuevo_inmueble = pd.DataFrame({
    'const': [1],
    'area_primer_piso': [98],
    'tiene_segundo_piso': [0],
    'cantidad_banos': [1],
    'calidad_de_cocina_excelente': [1]
})

print(modelo_0.predict(nuevo_inmueble['area_primer_piso']).round(2))

print(modelo_3.predict(nuevo_inmueble).round(2))