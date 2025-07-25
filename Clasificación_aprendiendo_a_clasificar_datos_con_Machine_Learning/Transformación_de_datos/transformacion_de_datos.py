import pandas as pd

datos = pd.read_csv('Clasificación_aprendiendo_a_clasificar_datos_con_Machine_Learning\\Análisis_exploratorio\\datos\\marketing_inversiones.csv')

print(datos.head())
print(datos.info())
print(datos.describe())

# analizar como se encuentran los datos
import plotly.express as px

fig1 = px.histogram(datos, x='adherencia_inversion', text_auto=True)
fig2 =px.histogram(datos, x='estado_civil', text_auto=True, color='adherencia_inversion')
fig3 =px.histogram(datos, x='escolaridad', text_auto=True, color='adherencia_inversion')
fig4 =px.histogram(datos, x='default', text_auto=True, color='adherencia_inversion', barmode='group')
fig5 =px.histogram(datos, x='prestatario', text_auto=True, color='adherencia_inversion', barmode='group')


# fig5.show()

# analizar las varibles numericas

fig6 =px.box(datos, x='edad', color='adherencia_inversion')
fig7 =px.box(datos, x='saldo', color='adherencia_inversion')
fig8 =px.box(datos, x='ultimo_contacto', color='adherencia_inversion')
fig9 =px.box(datos, x='ct_contactos', color='adherencia_inversion')


# fig9.show()

print(datos)

#  variables explicativas

X = datos.drop('adherencia_inversion', axis=1)
y = datos['adherencia_inversion']

print(X) # esto es un Dataframe
print(y) # esto es un serie

# convertir variables en numericos
# no se pueden clasificar sin tener un valor claro para no sesgar el modelo
# OneHotEncoder convierte en una tabal de 1 y 0 dando valor 1 donde se reuiere

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder

colummnas = X.columns
one_hot = make_column_transformer((OneHotEncoder(drop='if_binary'), 
                                   ['estado_civil', 'escolaridad', 'default', 'prestatario']), 
                                   remainder='passthrough', sparse_threshold=0)

X = one_hot.fit_transform(X)
print(one_hot.get_feature_names_out(colummnas))

print(X)

pd.DataFrame(X, columns=one_hot.get_feature_names_out(colummnas))

print(pd.DataFrame(X, columns=one_hot.get_feature_names_out(colummnas)))

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

print(y)


