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

# modelo de entrenamineto y prueba

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=5)

from sklearn.dummy import DummyClassifier

# El modelo simple para clasificar los datos

dummy = DummyClassifier()
dummy.fit(X_train, y_train)

print(dummy.score(X_test, y_test))

#  arbol de decision

from sklearn.tree import DecisionTreeClassifier

modelo_arbol = DecisionTreeClassifier(random_state=5)
modelo_arbol.fit(X_train, y_train)
print(modelo_arbol.score(X_test, y_test))

from sklearn.tree import plot_tree # graficar un arbol de decision
import matplotlib.pyplot as plt

valores_columnas = ['casado (a)',
                'divorciado (a)',
                'soltero (a)',
                'primaria',
                'secundaria',
                'superior',
                'default',
                'prestatario',
                'edad',
                'saldo',
                'ultimo_contacto',
                'ct_contactos']

plt.figure(figsize=(80,25))
plot_tree(modelo_arbol, feature_names=valores_columnas, filled=True, class_names=['no', 'si'], fontsize=6)
# plt.show()

print(modelo_arbol.score(X_train, y_train))

modelo_arbol = DecisionTreeClassifier(max_depth=3, random_state=5)
modelo_arbol.fit(X_train, y_train)
print(modelo_arbol.score(X_train, y_train))
print(modelo_arbol.score(X_test, y_test))

plt.figure(figsize=(15,6))
plot_tree(modelo_arbol, feature_names=valores_columnas, filled=True, class_names=['no', 'si'], fontsize=7)
# plt.show()

print(modelo_arbol.score(X_train, y_train))

# Normalizacion de datos

from sklearn.preprocessing import MinMaxScaler

normalizacion = MinMaxScaler()
X_train_normalizada = normalizacion.fit_transform(X_train)

print(pd.DataFrame(X_train_normalizada))

#  modelo KNN

from sklearn.neighbors import KNeighborsClassifier

modelo_knn = KNeighborsClassifier()
modelo_knn.fit(X_train_normalizada, y_train)

X_test_normalizada = normalizacion.transform(X_test)
print(modelo_knn.score(X_test_normalizada, y_test))

# Escogiendo y serializando el mejor modelo

lista = [('dummy', dummy, X_test), ('arbol', modelo_arbol, X_test), ('knn', modelo_knn, X_test_normalizada)]

for i in lista:
    print(f'La exactitud del modelo {i[0]} es: {i[1].score(i[2], y_test)}')

import pickle

with open('Clasificación_aprendiendo_a_clasificar_datos_con_Machine_Learning\\Selección_de_modelos\\datos\\modelo_onehotencoder.pkl', 'wb') as archivo:
    pickle.dump(one_hot, archivo)

with open('Clasificación_aprendiendo_a_clasificar_datos_con_Machine_Learning\\Selección_de_modelos\\datos\\modelo_champion.pkl', 'wb') as archivo:
    pickle.dump(modelo_arbol, archivo)

nuevo_dato = {
    'edad': [45],
    'estado_civil':['soltero (a)'],
    'escolaridad':['superior'],
    'default': ['no'],
    'saldo': [23040],
    'prestatario': ['no'],
    'ultimo_contacto': [800],
    'ct_contactos': [4]
}

nuevo_dato = pd.DataFrame(nuevo_dato)
print(nuevo_dato)

modelo_one_hot = pd.read_pickle('Clasificación_aprendiendo_a_clasificar_datos_con_Machine_Learning\\Selección_de_modelos\\datos\\modelo_onehotencoder.pkl')
modelo_arbol = pd.read_pickle('Clasificación_aprendiendo_a_clasificar_datos_con_Machine_Learning\\Selección_de_modelos\\datos\\modelo_champion.pkl')
nuevo_dato= modelo_one_hot.transform(nuevo_dato)
modelo_arbol.predict(nuevo_dato)

print(modelo_arbol.predict(nuevo_dato))