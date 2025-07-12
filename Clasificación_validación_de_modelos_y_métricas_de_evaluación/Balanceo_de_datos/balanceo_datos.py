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
# plt.show()

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print('la precision es:', precision_score(y_val, y_previsto))
print('la sensibilidad (recall):',recall_score(y_val, y_previsto))
print('El f1 score:',f1_score(y_val, y_previsto))
print('la exactitud es:',accuracy_score(y_val, y_previsto))

# Curva ROC carcateristica receptiva operativa

from sklearn.metrics import RocCurveDisplay

roc = RocCurveDisplay.from_predictions(y_val, y_previsto,name= 'Arbol de Decicion')
# plt.show()

from sklearn.metrics import roc_auc_score
print(f'El arbol bajo la curva ROC es: {roc_auc_score(y_val, y_previsto)}')

from sklearn.metrics import PrecisionRecallDisplay

precition_recall = PrecisionRecallDisplay.from_predictions(y_val, y_previsto, name='Arbol de decision')
# plt.show()

from sklearn.metrics import average_precision_score
print(f'El score promedio de presicion vs recall es {average_precision_score(y_val, y_previsto)}')

from sklearn.metrics import classification_report
print(classification_report(y_val, y_previsto))

#  validacion cruzada

from sklearn.model_selection import KFold, cross_validate

modelo = DecisionTreeClassifier(max_depth=10)
kf = KFold(n_splits=5, shuffle=True, random_state=5)
cv_resultados = cross_validate(modelo, X, y, cv=kf)
print(cv_resultados)
print(cv_resultados['test_score'])

promedio = cv_resultados['test_score'].mean()
desvio_std = cv_resultados['test_score'].std()
print(f'El promedio de la exactitud es de : {promedio}')
print(f'El desvio estandar de la exactitud es de : {desvio_std}')
print(f'El intervalo de confianza es de: [{promedio - 2 * desvio_std}, {min(promedio + 2 * desvio_std,1)}]')

# validacion cruazada con sensibilidad

def intervalo_confianza(resultados):
    promedio = resultados['test_score'].mean()
    desvio_std = resultados['test_score'].std()
    return f'El intervalo de confianza es de: [{promedio - 2 * desvio_std}, {min(promedio + 2 * desvio_std,1)}]'

modelo = DecisionTreeClassifier(max_depth=10)
kf = KFold(n_splits=5, shuffle=True, random_state=5)
cv_resultados = cross_validate(modelo, X, y, cv=kf, scoring='recall')
print(cv_resultados)
print(cv_resultados['test_score'])

intervalo_confianza(cv_resultados)
print(intervalo_confianza(cv_resultados))

print(datos['moroso'].value_counts())
print(datos['moroso'].value_counts(normalize=True))


#  estratificacion de datos

from sklearn.model_selection import StratifiedKFold

modelo = DecisionTreeClassifier(max_depth=10)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=5)
cv_resultados = cross_validate(modelo, X, y, cv=skf, scoring='recall')
print(cv_resultados)
print(cv_resultados['test_score'])

print(intervalo_confianza(cv_resultados))

# Balanceo de los datos
# Oversampling

from imblearn.over_sampling import SMOTE

oversampling = SMOTE(random_state=10)
x_balanceado, y_balanceado = oversampling.fit_resample(X, y)
print(x_balanceado.shape)
print(y_balanceado.shape)
print(y_balanceado.value_counts())
print(y_balanceado.value_counts(normalize=True))

modelo = DecisionTreeClassifier(max_depth=10)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=5)
cv_resultados = cross_validate(modelo, x_balanceado, y_balanceado, cv=skf, scoring='recall')
print(cv_resultados)
print(cv_resultados['test_score'])

print(intervalo_confianza(cv_resultados))

# Pipeline para validacion

from imblearn.pipeline import Pipeline as imbpipeline

modelo = DecisionTreeClassifier(max_depth=10)
pipeline = imbpipeline([('oversample', SMOTE()), ('arbol', modelo)])
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=5)
cv_resultados = cross_validate(pipeline, X, y, cv=skf, scoring='recall')

print(intervalo_confianza(cv_resultados))

# Balanceo de los datos
# Undersampling

from imblearn.under_sampling import NearMiss

modelo = DecisionTreeClassifier(max_depth=10)
pipeline = imbpipeline([('undersample', NearMiss(version=3)), ('arbol', modelo)])
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=5)
cv_resultados = cross_validate(pipeline, X, y, cv=skf, scoring='recall')

print(intervalo_confianza(cv_resultados))

# Probando el modelo

undersample = NearMiss(version=3)
x_balanceado, y_balanceado = undersample.fit_resample(X, y)
modelo = DecisionTreeClassifier(max_depth=10)
modelo.fit(x_balanceado, y_balanceado)
print(modelo.score(x_balanceado, y_balanceado))
print(modelo.score(X_test, y_test))

y_previsto = modelo.predict(X_test)
print(classification_report(y_test, y_previsto))
visualizacion = ConfusionMatrixDisplay.from_predictions(y_test, y_previsto)
visualizacion.plot()
plt.show()