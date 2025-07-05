# Importancia de las variables

Imagina que eres un(a) analista de datos trabajando en el Banco Bytebank. Este banco desea ofrecer a sus clientes préstamos con tasas de interés más precisas, basadas en un análisis detallado del valor de las propiedades. Para ello, debes desarrollar un modelo de regresión lineal que pueda predecir el precio de venta de casas en función de diversas características.

Inicialmente, ajustaste un modelo, utilizando solo el tamaño del primer piso como variable. Sin embargo, para mejorar tu modelo, decides explorar otros factores que pueden influir en el precio de venta, utilizando la herramienta pairplot para visualizar las relaciones entre estas variables y el precio.

¿Cuál de las siguientes afirmaciones describe mejor la importancia de incluir múltiples variables explicativas en el modelo de regresión lineal?

Al agregar más variables explicativas relacionadas con el precio de venta de las casas, el modelo se vuelve menos propenso a sesgos, ya que considera una gama más amplia de características que afectan el valor de la propiedad, proporcionando estimaciones más precisas.

La inclusión de más variables explicativas puede ayudar a reducir el sesgo y mejorar la precisión del modelo, considerando una variedad más amplia de factores que influyen en el precio de una propiedad.

# El papel del R² en la selección del modelo

En un proyecto de análisis de datos, un científico de datos compara cuatro modelos estadísticos para predecir el precio de las casas. Cada modelo utiliza un conjunto diferente de variables explicativas. El científico observa que los modelos con más variables tienen valores de R² más altos, pero es consciente de que esto puede no ser el único factor para elegir el mejor modelo. Con base en esta situación, ¿cuál de las siguientes afirmaciones es la más adecuada para seleccionar el modelo más apropiado? Elija una alternativa.

Prefiera el modelo con el R² ajustado más alto, ya que este tiene en cuenta el número de variables explicativas, ayudando a evitar el sobreajuste.

El R² ajustado es una medida más robusta que el R² simple, ya que penaliza la inclusión de variables que no contribuyen significativamente al modelo. Esto ayuda a equilibrar la complejidad del modelo con su capacidad explicativa, proporcionando una base más sólida para la elección del modelo.

# Para saber más: refinando la selección de modelos



En la clase sobre comparación de modelos de regresión lineal, exploramos cómo evaluar y seleccionar el modelo más adecuado utilizando el R² y otros criterios. Además de la selección manual que discutimos, existen métodos automáticos de selección de variables que pueden ser extremadamente útiles en situaciones donde el número de variables explicativas es grande. Estos métodos, como stepwise, backward y forward selection, siguen criterios predefinidos para agregar o eliminar variables del modelo de forma iterativa. Explora a continuación los métodos automáticos de selección de variables, que buscan equilibrar la complejidad del modelo y su capacidad explicativa.

    El método de forward selection comienza con un modelo sin variables explicativas y agrega una a una, eligiendo en cada paso la variable que más mejora el modelo de acuerdo con un criterio estadístico específico, como el menor valor de p-valor o el mayor aumento en el R² ajustado.
    El backward selection inicia con todas las variables posibles en el modelo y, de manera iterativa, elimina la variable que menos contribuye al modelo, nuevamente basándose en criterios como el p-valor o el impacto en el R² ajustado.
    El stepwise selection es una combinación de los dos métodos anteriores, donde las variables pueden ser agregadas o eliminadas en cada paso, dependiendo de su contribución a la mejora del modelo.

Estos métodos de selección automática son herramientas poderosas que ayudan en la identificación del modelo más parsimonioso, es decir, aquel que puede explicar los datos de manera eficiente sin ser excesivamente complejo. Sin embargo, es crucial que el científico de datos comprenda y supervise el proceso, ya que la elección automática puede, a veces, introducir sesgo o sobreajuste, especialmente si el criterio de selección no es bien elegido o si el modelo no es validado adecuadamente con datos nuevos o de prueba.

# En esta clase, aprendiste a:

    Utilizar el pairplot de Seaborn para visualizar relaciones entre múltiples variables e identificar cuáles pueden influir en el precio de venta de las casas.
    Agregar múltiples variables explicativas al modelo de regresión lineal para mejorar la precisión de las predicciones de precios.
    Comparar diferentes modelos de regresión lineal utilizando el R² y el R² ajustado, además de analizar la multicolinealidad y otros factores.
    Descubrir cómo interpretar los coeficientes del modelo de regresión lineal para entender el impacto de cada variable en el precio de las casas.
    Entender la importancia de elegir el modelo más adecuado para la predicción de precios, considerando la simplicidad, la precisión y la interpretabilidad.

