# Proceso de estimación

Suponiendo que tenemos un conjunto de datos de entrenamiento, donde y_train son los datos de la variable dependiente y X_train son los datos de las variables explicativas. Indique la opción que muestra el código correcto para estimar un modelo de regresión lineal, utilizando la biblioteca scikit-learn.
Seleccione una alternativa
```python
from sklearn.linear_model import LinearRegression
modelo = LinearRegression()
modelo.fit(X_train, y_train)
```
¡Correcta! Exactamente cómo procedemos en nuestro video. A partir de ese momento, podemos consultar la información de la estimación, generar métricas y hacer predicciones utilizando el objeto modelo.

# Predicciones con los datos transformados

Nuestro modelo utiliza datos que fueron transformados para resolver un problema de asimetría. Usamos la transformación logarítmica y por lo tanto nuestras predicciones estarán en esta misma escala. Para convertir nuestros datos al formato inicial, realizamos una nueva transformación. Marque la opción que muestra la función numpy utilizada para esa conversión.

exp()

¡Correcta! La función exponencial es la inversa del logaritmo natural que usamos en nuestros datos.

#  Entendiendo el significado de los parámetros estimados

Considere la siguiente tabla con los coeficientes estimados del modelo:
	Parámetros
Intercepto	7.646667
log Área	1.058078
log Distancia a la Playa	-0.490612

Verifique la alternativa que contiene una interpretación incorrecta de nuestros parámetros.
Seleccione una alternativa

Manteniendo constante el valor del área, un aumento del 1% en la distancia de un inmueble a la playa genera, en promedio, un aumento del 1.06% en el precio del inmueble.

¡Correcta! Interpretación incorrecta, en este caso, la interpretación correcta sería: manteniendo constante el valor del área, un aumento del 1% en la distancia de un inmueble a la playa genera, en promedio, una disminución del 0,49% en el precio del inmueble.

# Comprobando los resultados de la estimación

Acerca de los resultados de la estimación, evalúe las siguientes afirmaciones:

    Los residuos del modelo se obtienen restando el valor observado de la variable dependiente (valor real) y el valor predicho por el modelo.

    Para graficar la distribución de frecuencia de los residuos, podemos usar la función distplot() de la biblioteca seaborn.

    Cuando graficamos la dispersión entre el valor real de la variable dependiente y los valores predichos por el modelo, esperamos encontrar una relación lineal bien ajustada (recta).

Seleccione una alternativa

Todas las declaraciones son correctas.

¡Correcta! Perfecto, asimilaste bien el contenido. Felicidades.

# Haga lo que hicimos en aula: Regresión Lineal con Scikit-Learn



Consolidando su conocimiento

Es hora de que sigas todos los pasos que he dado durante este video:

    Estimar el modelo lineal usando los datos de entrenamiento
    Obtener el coeficiente de determinación (R²) del modelo estimado
    Generar las predicciones para los datos de prueba del modelo
    Obtener el coeficiente de determinación (R²) para las predicciones del modelo
    Generar la predicción puntual del modelo
    Invertir la transformación para obtener la estimación en dólares
    Crear un simulador simple
    Obtener el intercepto del modelo
    Obtener los coeficientes de regresión
    Crear un DataFrame para almacenar los coeficientes del modelo
    Interpretar los coeficientes estimados
    Analizar gráficamente los resultados del modelo

Si ya lo ha hecho, excelente. Si no es así, es importante que ejecutes lo visto en los videos para poder continuar con los próximos cursos que tengan esto como prerrequisito.


# Lo que aprendimos en esta aula:

    Como estimar el modelo lineal utilizando los datos de entrenamiento
    Como obtener el coeficiente de determinación (R²) del modelo estimado
    Como generar las predicciones para los datos de prueba del modelo
    Como obtener el coeficiente de determinación (R²) para las predicciones del modelo
    Como generar la predicción puntual del modelo
    Como invertir la transformación para obtener la estimación en dólares
    Como crear un simulador simple
    Como obtener el intercepto del modelo
    Como obtener los coeficientes de regresión
    Como crear un DataFrame para almacenar los coeficientes del modelo
    Como interpretar los coeficientes estimados
    Como analizar gráficamente los resultados del modelo

