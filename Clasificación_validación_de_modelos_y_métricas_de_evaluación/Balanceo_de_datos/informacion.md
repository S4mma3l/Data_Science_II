# Para saber más: balanceo de datos



En problemas de clasificación, podemos encontrarnos con bases de datos en las que la variable objetivo contenga clases muy desbalanceadas, es decir, categorías con frecuencias muy diferentes. Al entrenar un modelo con la variable desbalanceada, puede ser que el patrón de los datos para la clase dominante sobresalga en relación a la clase con menor frecuencia, generando un modelo con un desempeño muy bajo para clasificar la clase de menor frecuencia.

Para sortear estos problemas generados por la base de datos desbalanceada, podemos recurrir a dos soluciones que consisten en equilibrar los datos de la variable objetivo: undersampling y oversampling. Estas estrategias son útiles para que el modelo pueda comprender mejor el patrón de los datos, pero es importante destacar que también tienen desventajas y consideraciones que debemos analizar antes de utilizarlas.
Oversampling

La estrategia de oversampling consiste en aumentar la cantidad de datos de la clase que tiene menor frecuencia hasta que tenga la misma cantidad que la clase de mayor frecuencia. De esta manera, el modelo prestará más atención al patrón de los datos de la clase que tenía menor frecuencia al principio y podrá diferenciar mejor las dos clases.

Para aumentar la cantidad de datos necesitamos generar nuevos registros en la base de datos. Es posible utilizar un oversampling aleatorio para duplicar registros de manera aleatoria o usar una técnica como SMOTE para generar datos sintéticos con un patrón cercano a los datos existentes. La desventaja de esta estrategia es la posibilidad de sobreajuste del modelo, especialmente al utilizar el oversampling aleatorio. En este caso, el modelo puede especializarse demasiado en el patrón de los datos que son muy parecidos o idénticos, ya que son copiados o generados sintéticamente.
Undersampling

La estrategia de undersampling es contraria al oversampling y consiste en reducir la cantidad de datos de la clase que tiene mayor frecuencia hasta que tenga la misma cantidad que la clase de menor frecuencia. De esta forma, el modelo no prestará atención solo a los datos de mayor cantidad y podrá diferenciar mejor las dos clases.

Para reducir la cantidad de datos, necesitamos eliminar o borrar registros existentes. Es posible utilizar un undersampling aleatorio para seleccionar los registros que se mantendrán o usar técnicas que seleccionan o eliminan datos a partir de un patrón establecido. La principal desventaja de la estrategia de undersampling es la eliminación de datos que pueden ser muy importantes para la comprensión del problema, especialmente cuando esta eliminación se realiza sin ningún criterio, como es el caso del undersampling aleatorio.

Ambas estrategias son válidas para intentar mejorar el desempeño de un modelo de clasificación, pero debemos estar atentos al utilizarlas debido a los puntos negativos que son inherentes a cada uno de los métodos. En cualquier proyecto que utilice alguna de estas herramientas, se debe realizar un análisis para identificar si realmente ayudaron o perjudicaron el desempeño del modelo de clasificación.

# Para saber más: biblioteca imblearn



La clasificación de datos desbalanceados puede convertirse en una tarea bastante desafiante, ya que el enfoque tradicional de entrenar un modelo utilizando estos datos a menudo lleva a resultados muy insatisfactorios, donde el modelo tiende a favorecer la clase con mayor cantidad de datos en detrimento de la otra.

Para abordar este tipo de situación, la biblioteca imbalanced-learn, abreviada como imblearn, ofrece diversas técnicas y herramientas con el objetivo de equilibrar la distribución de las categorías de la variable objetivo y mejorar el rendimiento de los modelos de machine learning. Las técnicas consisten en algoritmos de reamostrado de oversampling, undersampling y algoritmos que combinan ambas estrategias simultáneamente.

Algunos de los algoritmos de oversampling de la biblioteca:

    RandomOversampler [https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.RandomOverSampler.html]
    SMOTE[https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html]
    ADASYN[https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.ADASYN.html]
    KMeansSMOTE[https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.KMeansSMOTE.html]

Algunos de los algoritmos de undersampling de la biblioteca:

    RandomUnderSampler [https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.RandomUnderSampler.html]
    NearMiss [https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.NearMiss.html]
    ClusterCentroids [https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.ClusterCentroids.html]
    TomekLinks [https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.TomekLinks.html]

Algoritmos que combinan las dos técnicas de oversampling y undersampling:

    SMOTEENN [https://imbalanced-learn.org/stable/references/generated/imblearn.combine.SMOTEENN.html]
    SMOTETomek [https://imbalanced-learn.org/stable/references/generated/imblearn.combine.SMOTETomek.html]

Además de las técnicas de balanceo de datos, la biblioteca proporciona herramientas para la construcción de pipelines de datos(https://imbalanced-learn.org/stable/references/pipeline.html), algoritmos de machine learning(https://imbalanced-learn.org/stable/references/ensemble.html) para datos desbalanceados y cálculos de métricas de rendimiento de modelos.(https://imbalanced-learn.org/stable/references/metrics.html)

# Importancia del pipeline

Generalmente, en proyectos de machine learning, son necesarias etapas de transformación de datos para obtener modelos más eficientes. La secuencia de ejecución de todas las transformaciones y ajustes del modelo se conoce como pipeline.

Al utilizar ciertas transformaciones junto con la validación cruzada, como por ejemplo el oversampling de datos, necesitamos utilizar una función de organización del pipeline, de lo contrario, el resultado obtenido por el modelo será incorrecto. Selecciona la alternativa que indica el cambio de proceso del oversampling en la utilización de un pipeline con la validación cruzada:
Seleccione una alternativa

Con la utilización del pipeline, las transformaciones en los datos se realizan en cada conjunto de datos por separado después de la división de la validación cruzada.

El pipeline se utiliza para realizar la transformación en los datos en cada una de las divisiones de forma independiente, además, la transformación de oversampling se realiza solo en los datos de entrenamiento, manteniendo la proporción original de los datos reales en el conjunto de validación.

# Para saber más: versiones del NearMiss



El desequilibrio de clases es un problema común en tareas de clasificación en machine learning, como diagnósticos médicos, detección de fraudes y detección de anomalías, donde la frecuencia de ocurrencia de un evento es muy baja en relación con el total. Una de las estrategias para abordar este problema de datos desequilibrados es el undersampling, que busca reducir el número de muestras de la clase con mayor frecuencia.

Entre los algoritmos de undersampling, podemos mencionar el NearMiss, que consiste en seleccionar muestras de la categoría en mayor cantidad que tienen un patrón cercano a la categoría con menor cantidad, con el fin de preservar información importante para la modelación del problema. Al utilizar un criterio de selección de las muestras, este método es mucho más recomendado que el uso de un undersampling puramente aleatorio, que puede eliminar información relevante de los datos.

Para seleccionar las muestras, este algoritmo utiliza un método conocido como vecino más cercano. Este método se aplica en 3 pasos:

    1er paso: se calculan distancias entre todas las muestras de la clase con mayor frecuencia y de la clase con menor frecuencia.

    2º paso: a continuación, para cada muestra de la clase de menor frecuencia, se seleccionan n muestras de la clase de mayor frecuencia; por defecto, este número es 3 y de ahí proviene el nombre de vecinos más cercanos. Se seleccionan 3 vecinos más cercanos para cada muestra de la clase de menor frecuencia.

    3er paso: a partir de los elementos que fueron seleccionados, ocurre un nuevo proceso de selección para que quede con la misma cantidad de elementos de la clase de menor frecuencia. Esta selección final tiene 3 versiones diferentes:

NearMiss versión 1: se calcula un promedio entre las distancias de los 3 vecinos más cercanos de cada muestra de la clase de mayor frecuencia y se eligen aquellos que tengan la menor media de distancia.

NearMiss versión 2: se calcula un promedio entre las distancias de los 3 vecinos más lejanos de cada muestra de la clase de mayor frecuencia y se eligen aquellos que tengan la menor media de distancia.

NearMiss versión 3: se divide en dos etapas. Primero, para cada elemento de la clase de menor frecuencia, se eligen y almacenan M vecinos más cercanos, por defecto M también es de 3 vecinos. Luego se calcula el promedio de las distancias entre los elementos almacenados y los elementos de la clase de menor frecuencia y se eligen aquellos que tengan la mayor media de distancia.

Si desea saber más sobre las versiones del NearMiss, consulte la documentación de imbalanced-learn:

    Formulación matemática del NearMiss (https://imbalanced-learn.org/dev/under_sampling.html#mathematical-formulation)

# Desafío: otros métodos de balanceo



Durante la clase, exploramos dos estrategias de balanceo de datos: oversampling y undersampling. En cada una de ellas utilizamos un algoritmo diferente, el SMOTE para generar nuevos datos sintéticos y el NearMiss para mantener datos que tienen un patrón cercano entre las clases.

Estos no son los únicos algoritmos existentes y el oversampling y undersampling no necesitan ser utilizados de manera aislada. Es posible combinar las dos estrategias en una sola para equilibrar los puntos negativos de cada una de ellas. Esto no quiere decir que esta estrategia sea más efectiva en todas las ocasiones, pero es una opción que puede ser explorada en los proyectos.

Como desafío, utiliza el algoritmo SMOTEENN, que combina el oversampling con SMOTE y el undersampling con el ENN (Edited Nearest Neighbours), para balancear los datos y observa los resultados obtenidos por el modelo usando el pipeline y la validación cruzada.

Como un consejo, revisa la documentación del método SMOTEENN a partir de este enlace para identificar cómo importar el método y cómo utilizarlo.

# Desafío: hora de la práctica


Vamos a practicar el contenido que se presentó en la clase a partir de algunas actividades, pero utilizando un conjunto de datos diferente con datos de pacientes a ser diagnosticados con diabetes o no. Los desafíos siguen una secuencia de tareas, sirviendo como un proyecto secundario. Para realizar los desafíos, descarga la base de datos a partir de este material.

1 - El desbalanceo de los datos de la variable objetivo puede hacer que el modelo se incline a acertar los patrones de solo la categoría que tiene mayor cantidad, haciendo necesario en algunos casos un tratamiento específico de balanceo de datos. La etapa inicial es identificar si existe o no el desbalanceo de datos en la variable objetivo. Por eso, verifica la proporción de datos de la variable objetivo del conjunto de datos de diabetes. Este análisis puede hacerse a partir del porcentaje de datos, utilizando el método value_counts(normalize=True) o con la utilización de un gráfico de conteo, usando el gráfico countplot de la biblioteca seaborn para entender si hay un desbalanceo de datos.

2 - Al realizar el balanceo de datos en una validación cruzada, es necesario utilizar un pipeline, para que los datos de validación no sean balanceados, manteniéndose en el estándar de los datos del mundo real. Utiliza un pipeline que contenga el ajuste del modelo y el balanceo de los datos usando el oversampling con SMOTE, obteniendo la media del F1-Score de una validación cruzada con StratifiedKFold.

3 - Además del oversampling, es posible utilizar la estrategia de undersampling para hacer el balanceo de los datos. A pesar de ser estrategias distintas, ambas requieren de un pipeline por tratarse de balanceo de datos en una validación cruzada. Utiliza un pipeline que contenga el ajuste del modelo y el balanceo de los datos usando el undersampling con NearMiss en su versión 3, obteniendo la media del F1-Score de una validación cruzada con StratifiedKFold.

4 - Después de realizar diversas análisis y mejorar el rendimiento de los modelos, llega la etapa final, que consiste en seleccionar el modelo con mejor rendimiento y hacer la evaluación final en un conjunto de datos de prueba, que no ha sido visto durante el proceso de entrenamiento y validación. Elige el modelo que obtuvo el mejor rendimiento al comparar las estrategias de oversampling y undersampling y entrena un modelo usando todos los datos con la mejor estrategia. Realiza la evaluación del modelo usando los datos de prueba que fueron separados al inicio de los desafíos, obteniendo el informe de métricas y matriz de confusión.

# En esta clase, aprendiste a:

    Utilizar oversampling y undersampling en datos desbalanceados;
    Utilizar técnicas de balanceo de datos y entender sus ventajas y desventajas;
    Aplicar un pipeline junto con la validación cruzada;
    Probar modelos de clasificación.

