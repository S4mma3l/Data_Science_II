# Escala de las variables

En un proyecto de machine learning, estás trabajando con un conjunto de datos que tiene dos características: "Edad" y "Ingreso Anual". La "Edad" varía de 18 a 80 años, mientras que el "Ingreso Anual" varía de $30,000 a $90,000. Ambas características son importantes para predecir si la persona comprará o no un producto.

Elige la alternativa que indica la principal razón para normalizar estos datos antes de entrenar tu modelo:
Seleccione una alternativa

Para evitar problemas numéricos durante el entrenamiento y garantizar que todas las características tengan el mismo impacto en el modelo.

La normalización garantiza que todas las características tengan el mismo impacto en el modelo, haciendo que las predicciones sean más justas y equilibradas.

# Para saber más: cómo funciona el KNN



El modelo k-Nearest Neighbors (KNN) es un algoritmo de machine learning ampliamente utilizado. Es una técnica simple, pero eficaz, que se basa en la idea de que los objetos similares tienden a estar cerca unos de otros en un espacio de características. A continuación, exploraremos cómo funciona el KNN y cómo toma decisiones de clasificación.
Funcionamiento

El algoritmo KNN opera calculando la distancia entre todos los elementos de la base de datos para determinar la clasificación de un registro, lo cual se realiza al verificar las clases de los elementos que están más cerca.

En esta dinámica, el primer paso consiste en definir un valor de 'k', que es la cantidad de vecinos más cercanos a considerar al momento de hacer la clasificación. La elección de este valor es importante y afecta el rendimiento del modelo. A continuación, se calcula la distancia entre todos los elementos y se almacenan los resultados de estas distancias.

Finalmente, para clasificar cada elemento, se seleccionan los 'k' elementos más cercanos a él y se realiza una votación. La votación consiste en seleccionar la clase que aparece con más frecuencia entre estos vecinos más cercanos.

La normalización de los datos es esencial para este algoritmo, porque se basa en cálculos de distancia. Además, es un algoritmo que demanda mucho computacionalmente cuando hay muchos datos, ya que necesita calcular las distancias entre todos los elementos de entrenamiento.

# Para saber más: Pickle



Después de crear los modelos de machine learning, comparar los resultados y seleccionar aquel que obtuvo el mejor rendimiento, es el momento de utilizar el modelo para clasificar nuevos datos del mundo real, que es desde el principio el objetivo real del proyecto. Sucede que el modelo generalmente se construye en un notebook y el entorno en el que se va a utilizar el modelo es diferente, en alguna aplicación, sitio o sistema.

Para poder utilizar el modelo, es necesario exportarlo, y es en ese momento que entra en escena el pickle. El módulo pickle en Python es una herramienta poderosa y versátil que permite la serialización y deserialización de objetos Python. Este proceso de serialización implica la conversión de objetos Python en una representación binaria que puede ser almacenada en un archivo. Más tarde, esta representación puede ser deserializada para recrear el objeto original.

Así, es posible almacenar modelos de machine learning en archivos pickle, para que puedan ser utilizados en otros programas. Él preserva completamente el estado del objeto, incluyendo todos los parámetros y configuraciones. Además, el formato binario generado por el pickle es independiente de la plataforma, lo que significa que es posible crear un archivo en un sistema operativo y cargarlo en otro sin problema de compatibilidad. Vale destacar que en versiones diferentes de Python esto puede ser un problema. Objetos serializados en una versión específica pueden no ser cargados correctamente en otra versión. Por lo tanto, es muy importante saber cuál es la versión del lenguaje y de las bibliotecas utilizadas en el proyecto para que sean replicadas dentro del sistema en el que se va a utilizar.

El proceso para utilizar el pickle involucra principalmente dos funciones:

    pickle.dump(objeto, archivo): Esta función permite almacenar un objeto Python en un archivo. El argumento objeto es el objeto que deseas serializar, y el argumento archivo es el objeto de archivo donde deseas almacenar la representación binaria.
    pickle.load(archivo): Esta función permite que deserialices (cargues) un objeto Python de un archivo. El argumento archivo es el archivo de donde deseas cargar la representación binaria.

También podemos usar la biblioteca pandas para hacer la lectura de archivos pickle. Para esto, basta con utilizar el método pd.read_pickle.

#  Desafío: hora de la práctica

Después de estudiar los conceptos de esta clase, ¡ha llegado el momento de practicar!

Vamos a practicar lo que se presentó en la clase a partir de algunas actividades, pero utilizando un conjunto de datos diferente al presentado en la clase. El tema de la base de datos es la de churn de clientes. El churn es una métrica que indica a los clientes que cancelan el servicio en un determinado período de tiempo.

Los desafíos siguen una secuencia de tareas, sirviendo como un proyecto secundario, que se realizará a lo largo de las clases del curso. Para realizar los desafíos, descarga la Base de datos - Desafío.

    La normalización de datos es una tarea importante para mantener todos los valores numéricos en una misma escala y garantizar que todas las características tengan el mismo impacto en el modelo. En esta tarea, realiza la normalización de la base de datos usando el MinMaxScaler.

    Con los datos normalizados, podemos utilizar el modelo KNN, que hace cálculos de distancia para encontrar los vecinos más cercanos. En esta actividad, crea un modelo KNN usando el KNeighborsClassifier con los datos normalizados y evalúa el rendimiento en los datos de prueba, también normalizados.

    Después de construir los modelos, es el momento de comparar los resultados y seleccionar aquel que tiene el mejor rendimiento. En este desafío, evalúa la tasa de acierto de los modelos DummyClassifier, DecisionTreeClassifier y KNeighborsClassifier que fueron construidos en los otros desafíos utilizando el método score y, a continuación, almacena el modelo con mejor precisión en un archivo pickle. Los modelos de transformación también necesitan ser almacenados, que es el caso del OneHotEncoder y del MinMaxScaler, en caso de que el KNN tenga el mejor rendimiento.

    Después de que el modelo está en producción, ya puede ser utilizado para clasificar nuevos datos. En este desafío, realiza la lectura de los archivos pickle de los modelos que fueron guardados en el desafío anterior y utiliza los modelos para hacer la predicción del siguiente registro:

nuevo_dato = pd.DataFrame({
    'score_credito': [850],
    'pais':['Francia'],
    'sexo_biologico':['Hombre'],
    'edad': [27],
    'años_de_cliente': [3],
    'saldo': [56000],
    'servicios_adquiridos': [1],
    'tiene_tarjeta_credito': [1],
    'miembro _activo': [1],
    'salario_estimado': [85270.00]
})

Recuerda que la práctica es fundamental para mejorar tus habilidades en Machine Learning. Con cada actividad, estás un paso más cerca de dominar cada vez más este conocimiento. ¡Manos a la obra y disfruta cada momento de esta jornada!


# En esta clase, aprendiste a:

    Normalizar datos para que estén en la misma escala;
    Construir un modelo de vecinos más cercanos usando el KNeighborsClassifier;
    Comparar los resultados de rendimiento de los modelos;
    Hacer predicciones con los modelos para nuevos datos;
    Exportar modelos usando la biblioteca pickle.

