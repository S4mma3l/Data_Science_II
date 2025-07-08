import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


datos = pd.read_csv('Regrecion_lineal_Tecnicas_avanzadas_de_modelado\\analisis_preliminar\\datos\\dataset.csv', sep=';')

print(datos.head())

print(datos.shape)
print(len(datos.columns))

print(datos.describe().round(2))

# Matriz de correlacion

print(datos.corr().round(2))

import seaborn as sns
import matplotlib.pyplot as plt


sns.set_palette('Accent')
sns.set_style('darkgrid')

ax = sns.boxplot(data=datos['Valor'], orient='h', width=0.3)

ax.figure.set_size_inches(10, 5)
ax.set_title('Precio de los Inmuebles', fontsize=20)
ax.set_xlabel('Dolares', fontsize=16)
ax

# plt.show()

ax = sns.distplot(datos['Valor'])


ax.figure.set_size_inches(10, 6)
ax.set_title('Distribuición de Frecuencias', fontsize=20)
ax.set_xlabel('Precio de los Inmuebles (US$)', fontsize=16)
ax

# plt.show()

ax = sns.pairplot(datos, y_vars='Valor', x_vars=['Area','Dist_Playa','Dist_Farmacia'], height=5)
ax.fig.suptitle('Dispersión entre las Variables', fontsize=10, y=1.05)
ax
# plt.show()

grid = sns.pairplot(datos, y_vars='Valor', x_vars=['Area','Dist_Playa','Dist_Farmacia'], height=5, kind='reg')
# Iterar sobre los ejes del pairplot para personalizar los colores
for i, ax_row in enumerate(grid.axes):
    for j, ax in enumerate(ax_row):
        if i == 0 and j < len(grid.x_vars): # Solo trabajamos en la primera fila (Valor vs. cada x_var)
            # Encontrar los scatter plots y cambiar su color
            scatter = ax.collections
            if scatter:
                scatter[-1].set_color('blue') # Cambiar el color de los puntos al azul

            # Encontrar las líneas de regresión y cambiar su color
            lines = ax.lines
            if lines and len(lines) > 0:
                lines[-1].set_color('green') # Cambiar el color de la línea de regresión al verde
                if len(lines) > 1:
                    lines[-2].set_color('lightgreen') # Cambiar el color del intervalo de confianza

grid.fig.suptitle('Dispersión entre las Variables', fontsize=10, y=1.05)


# plt.show()

import numpy as np

np.log(1)
print(np.log(1))

datos['log_valor'] = np.log(datos['Valor'])
datos['log_area'] = np.log(datos['Area'])
datos['log_dist_playa'] = np.log(datos['Dist_Playa']+1)
datos['log_dist_farmacia'] = np.log(datos['Dist_Farmacia']+1)

print(datos.head())



ax = sns.distplot(datos['log_valor'])
ax.figure.set_size_inches(10, 6)
ax.set_title('Distribucion de Frecuencias', fontsize=20)
ax.set_xlabel('log del precio de los Inmuebles', fontsize=16)
ax

plt.show()

ax = sns.pairplot(datos, y_vars='log_valor', x_vars=['log_area','log_dist_playa','log_dist_farmacia'], height=5, kind='reg')
ax.fig.suptitle('Dispersion entre las variables transformadas', fontsize=10, y=1.05)
ax
plt.show()

y = datos['log_valor']

x = datos[['log_area','log_dist_playa','log_dist_farmacia']]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2811)

import statsmodels.api as sm

X_train_con_constante = sm.add_constant(X_train)

print(X_train_con_constante.head())

modelo_statsmodels = sm.OLS(y_train, X_train_con_constante, hasconst=True).fit()

print(modelo_statsmodels.summary())

x = datos[['log_area','log_dist_playa']]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2811)

X_train_con_constante = sm.add_constant(X_train)

print(X_train_con_constante.head())

modelo_statsmodels = sm.OLS(y_train, X_train_con_constante, hasconst=True).fit()

print(modelo_statsmodels.summary())

from sklearn.linear_model import LinearRegression
from sklearn import metrics

modelo_sklearn = LinearRegression()

modelo_sklearn.fit(X_train, y_train)

print('R2={}'.format(round(modelo_sklearn.score(X_train, y_train),3)))

y_predicho = modelo_sklearn.predict(X_test)

print('R2={}'.format(round(metrics.r2_score(y_test, y_predicho),3)))

entrada = X_test[0:1]

print(entrada)

print(modelo_sklearn.predict(entrada)[0])

print(np.exp(modelo_sklearn.predict(entrada)[0]))

Area = 150
Dist_Playa = 1

entrada = [[np.log(Area), np.log(Dist_Playa+1)]]

print(modelo_sklearn.predict(entrada)[0])

print('USD$ {}'.format(round(np.exp(modelo_sklearn.predict(entrada)[0]),2)))

print(modelo_sklearn.intercept_)

print(np.exp(modelo_sklearn.intercept_))

print(modelo_sklearn.coef_)

print(np.exp(modelo_sklearn.coef_))

print(x.columns)

index=['Intercepto', 'log_area', 'log_dist_playa']

print(pd.DataFrame(data=np.append(modelo_sklearn.intercept_,modelo_sklearn.coef_), index=index, columns=['Parametros']))

y_predicho_train = modelo_sklearn.predict(X_train)

ax=sns.scatterplot(x=y_predicho_train, y=y_train)
ax.figure.set_size_inches(12, 6)
ax.set_title('Predicción X Real', fontsize=18)
ax.set_xlabel('log del Precio - Predicción', fontsize=14)
ax.set_ylabel('log del Precio - Real', fontsize=14)
ax

plt.show()

residuo=y_train-y_predicho_train

ax=sns.distplot(residuo)
ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuición de Frecuencias de los Residuos', fontsize=18)
ax.set_xlabel('log del Precio', fontsize=14)
ax
plt.show()