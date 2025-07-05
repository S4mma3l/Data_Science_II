# Comparación entre R² de entrenamiento y prueba

El coeficiente de determinación (R²) es una métrica fundamental en modelos de regresión, ya que indica la proporción de la varianza en la variable de respuesta que es explicada por las variables explicativas. Considerando este contexto, ¿por qué es importante comparar el R² calculado con los datos de entrenamiento y también con los datos de prueba en modelos de regresión? Elige la alternativa correcta.

Para determinar si el modelo está sobreajustado a los datos de entrenamiento (overfitting), perdiendo la capacidad de generalización.

Comparar el R² de entrenamiento y prueba ayuda a identificar si el modelo está sobreajustado a los datos de entrenamiento (overfitting), lo que perjudica su capacidad de generalización. Si hay una diferencia muy grande entre los valores de entrenamiento y prueba, puede indicar que el modelo está siendo influenciado por patrones específicos de los datos de entrenamiento que no son generalizables a los datos de prueba.

# Para saber más: guardando el modelo en un archivo

Al desarrollar modelos de regresión con Statsmodels, es común querer guardar estos modelos para uso futuro, ya sea para implementación en producción, compartir con otros miembros del equipo o simplemente para respaldo. Una manera conveniente de hacer esto en Python es usando la biblioteca pickle, que permite serializar objetos de Python en archivos y deserializarlos de vuelta a objetos de Python. Esta biblioteca no necesita ser instalada, ya que viene por defecto en Python.

Vamos a explorar cómo guardar un modelo de regresión lineal de Statsmodels con la biblioteca pickle y luego cómo leer el archivo.
Cómo guardar el Modelo con Pickle

Después de entrenar el modelo, podemos guardarlo en un archivo usando la biblioteca pickle. Para ello, es necesario importar la biblioteca y luego podemos usar la función pickle.dump(), indicando el modelo y el archivo como parámetros.
```python
import pickle

# Nombre del archivo donde se guardará el modelo
nombre_archivo = 'modelo_regresion_lineal.pkl'

# Guardar el modelo en un archivo usando pickle
with open(nombre_archivo, 'wb') as archivo:
    pickle.dump(modelo, archivo)
```
Cargar el Modelo de vuelta con Pickle

Después de guardar el modelo, podemos cargarlo de vuelta para uso posterior. Para hacer esto, simplemente usamos el método pickle.load() utilizando el archivo como parámetro de la función.
```python
# Cargar el modelo de vuelta del archivo
with open(nombre_archivo, 'rb') as archivo:
    modelo_cargado = pickle.load(archivo)
```
A partir de la lectura del archivo, es posible utilizar el modelo para hacer predicciones y verificar métricas de la misma manera que usamos el modelo original.

Para más detalles sobre el uso de la biblioteca pickle, consulte la documentación. https://docs.python.org/3/library/pickle.html

# En esta clase, aprendiste a:

    Obtener la métrica R² del modelo a partir de datos de prueba;
    Entender la importancia de la comparación de métricas de entrenamiento y prueba para verificar la generalización del modelo;
    Utilizar el método predict para realizar la predicción de nuevos valores a partir de un modelo de regresión;
    Guardar un modelo de machine learning utilizando la biblioteca pickle;
    Leer archivos pickle para obtener el modelo en su estado original.

