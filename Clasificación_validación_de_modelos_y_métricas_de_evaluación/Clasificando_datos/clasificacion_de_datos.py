import pandas as pd

datos = pd.read_csv('Clasificación_validación_de_modelos_y_métricas_de_evaluación\\Clasificando_datos\\Datos\\prestacar.csv')

print(datos.head())
print(datos.columns)

X = datos.drop(columns='moroso', axis=1)
y = datos['moroso']

print(X.head())
print(y.head())

from sklearn.tree import DecisionTreeClassifier

modelo = DecisionTreeClassifier()

modelo.fit(X, y)
print(modelo.score(X, y))
print(f'La exactitud del modelo es : {modelo.score(X, y)}')

from sklearn.model_selection import train_test_split

X, X_test, y, y_test = train_test_split(X, y, test_size=0.15, stratify=y, random_state=5)
X_train, X_val, y_train, y_val = train_test_split(X, y, stratify=y, random_state=5)

#  Sin validacion
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)
print(modelo.score(X_val, y_val))
print(modelo.score(X_test, y_test))
print(f'La exactitud del modelo con el conjunto de entrenamiento es de : {modelo.score(X_train, y_train)}')
print(f'La exactitud del modelo con el conjunto de validación es : {modelo.score(X_val, y_val)}')
print(f'La exactitud del modelo con el conjunto de testes : {modelo.score(X_test, y_test)}')


# Con validacion
modelo = DecisionTreeClassifier(max_depth=10)# validacion con max_depth=
modelo.fit(X_train, y_train)
print(modelo.score(X_val, y_val))
print(modelo.score(X_test, y_test))
print(f'La exactitud del modelo con el conjunto de entrenamiento es de : {modelo.score(X_train, y_train)}')
print(f'La exactitud del modelo con el conjunto de validación es : {modelo.score(X_val, y_val)}')
print(f'La exactitud del modelo con el conjunto de testes : {modelo.score(X_test, y_test)}')

from sklearn.metrics import confusion_matrix

y_previsto = modelo.predict(X_val)
matriz_de_confusion = confusion_matrix(y_val, y_previsto)
print(matriz_de_confusion)

from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

visualizacion = ConfusionMatrixDisplay(confusion_matrix=matriz_de_confusion, display_labels=('Cumplido', 'moroso'))
visualizacion.plot()
plt.show()