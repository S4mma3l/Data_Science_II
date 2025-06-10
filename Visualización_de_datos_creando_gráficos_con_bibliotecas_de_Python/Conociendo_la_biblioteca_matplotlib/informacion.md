# Para saber más: en qué se relaciona el plano cartesiano con la visualización



Mayza es una estudiante de Ciencia de Datos en busca de nuevos conocimientos y experiencias. En su proyecto más reciente, se encontró con un desafío: ¿cómo crear gráficos en Python que realmente transmitan la información necesaria? Con la mente inquieta y sedienta por respuestas, está trabajando en un proyecto que requiere la visualización de datos, pero no tiene idea de cómo puede comenzar. Al sumergirse en sus estudios, Mayza se encontró frecuentemente con el término plano cartesiano.

Seguramente ya has oído hablar sobre este término. Puede que haya sido en alguna clase de geografía, por ejemplo. Pero, ¿qué tiene que ver esto con la visualización de datos?

Imagina un mapa común, de esos que muestran calles, puntos turísticos y otras informaciones útiles para quien está viajando. Su objetivo principal es proporcionar orientaciones y referencias de forma clara y fácil de entender, al punto de ayudar al viajero a encontrar el camino correcto y tomar las mejores decisiones durante su viaje. El plano cartesiano sigue la misma idea, pero en lugar de calles y edificios, muestra información en forma de gráficos. Con él, podemos visualizar información compleja de manera intuitiva y eficiente, facilitando la toma de decisiones y la resolución de problemas gracias a los ejes que se cruzan en un punto central.

Con el uso del plano cartesiano, constituido por el eje X y el eje Y, es posible crear un sistema de coordenadas bidimensional que facilita la localización y análisis de datos. Estos ejes también son conocidos por los siguientes nombres:

    eje x: eje de las abscisas.
    eje y: eje de las ordenadas.

Los ejes son componentes esenciales debido a sus combinaciones, que posibilitan una mayor precisión en la identificación de puntos en un espacio bidimensional. En la figura abajo, tenemos la representación de un plano cartesiano conteniendo los ejes X y Y para ejemplificar. Con él podemos notar algunas características importantes:

    El eje X es horizontal.
    El eje Y es vertical.
    En el centro tenemos el origen, el valor 0 (cero).
    Hacia la derecha y hacia arriba tenemos valores positivos.
    Hacia la izquierda y hacia abajo tenemos valores negativos.

1.png[](Visualización_de_datos_creando_gráficos_con_bibliotecas_de_Python/Conociendo_la_biblioteca_matplotlib/datos/imagen1.png)

Como es posible constatar a través de estas representaciones, los ejes nos permiten especificar la ubicación exacta de un punto en un espacio bidimensional, de modo que los valores de X y Y son llamados coordenadas porque describen la ubicación del punto en relación al origen. En la figura abajo, tenemos un plano cartesiano conteniendo puntos de algunas coordenadas: (2,5), (1,2), (0,-1), (-1,-4) y (-2,-7). Considera la representación y observa los puntos disponibles. Así puedes visualizar mejor la relación entre ellos y entender patrones y tendencias en los datos.

2.png[](Visualización_de_datos_creando_gráficos_con_bibliotecas_de_Python/Conociendo_la_biblioteca_matplotlib/datos/imagen2.png)

Cuando creamos un gráfico, las coordenadas de los puntos son utilizadas para definir la posición de cada punto en el gráfico. Y una curiosidad interesante: el plano cartesiano y el eje de coordenadas son ampliamente usados en varios campos, incluyendo Matemáticas, Física, Ingeniería, Ciencia de Datos y muchos otros, siendo una herramienta fundamental para la representación de datos y para la visualización de resultados en diversos contextos.

¿Recuerdas la saga de Mayza? Después de explorar las posibilidades en sus estudios, Mayza comprendió el concepto de plano cartesiano y cómo esto puede ser útil en su proyecto de visualización de datos. Ahora necesita algunos insights para crear un gráfico y supo que tú puedes ayudarla en eso.

¿Entonces, vamos a crear nuestro primer gráfico ahora?


# Usando la sintaxis correcta para la creación de un gráfico

Alicia está observando el crecimiento de la población de Águas de San Pedro, un acogedor pueblo ubicado en el interior de San Pablo. Debido a los análisis que ha estado realizando, ha estado buscando algunas formas de representar visualmente la tendencia del crecimiento poblacional a lo largo del tiempo y ha decidido trazar un gráfico de líneas, porque, vamos a admitirlo, los gráficos son una forma muy buena de contar historias con números.

Afortunadamente, ya tiene todo lo que necesita: un DataFrame almacenado en una variable llamada df_aguas, que contiene el número de habitantes en la columna n_habitantes y los años en la columna ano. Para crear el DataFrame, se utilizó el siguiente comando:
```python
import pandas as pd

df_aguas = pd.DataFrame({'ano': [1970, 1980, 1991, 2000, 2010, 2020],
                         'n_habitantes': [830, 1091, 1697, 1883, 2703, 3500]})
```
¡Ahora es el momento de la verdad para Alicia! Necesita decidir cuál es la sintaxis correcta del comando para trazar un gráfico de líneas utilizando la biblioteca matplotlib y así visualizar el crecimiento poblacional de Águas de São Pedro a lo largo del tiempo. ¡Vamos allá! ¿Cuál de las siguientes opciones representa la sintaxis correcta del comando?

plt.plot(df_aguas['ano'], df_aguas['n_habitantes'])

Este código es correcto para trazar un gráfico de líneas con el eje X representando el año y el eje Y representando el número de habitantes en Águas de San Pedro, ya que el primer argumento siempre corresponde al eje X y el segundo al eje Y.

# Desafío: comparando tendencias migratorias



Ha llegado el momento de que pongas a prueba los conocimientos desarrollados durante la clase. Creamos un gráfico con la función plt.plot() para analizar las intrigantes tendencias de inmigración de Colombia a Canadá, desde 1980 hasta 2013. Ahora tenemos una nueva tarea: crear un gráfico de líneas comparando los números de inmigrantes de Brasil y Argentina a Canadá, los dos países más grandes de Sudamérica.

Prepárate para sumergirte en las fascinantes líneas que conectan estos países sudamericanos con el territorio canadiense. En esta misión, la elaboración de este gráfico puede ser útil para comprender las tendencias migratorias de estos países a Canadá a lo largo del tiempo y cómo se comparan entre sí. Al analizar estos factores, podemos obtener una visión más amplia del panorama migratorio en Sudamérica.

¡No te preocupes!

Esta nueva tarea es más desafiante, ya que requiere un análisis comparativo entre dos países. Sin embargo, también te permitirá obtener un aprendizaje enriquecedor. Por lo tanto, explora las diversas posibilidades y recuerda los elementos esenciales de un gráfico: título, etiquetas en los ejes x e y y las marcas del eje x, que deben definirse cada 5 años.

Además, tendrás que descubrir cómo agregar una leyenda para poder identificar la línea de cada país. Siguiendo estas instrucciones, habrás construido un gráfico sólido que te permitirá un análisis significativo y profundo.

Después de crear el gráfico, analiza el resultado obtenido y reflexiona sobre las siguientes preguntas:

    ¿Hay alguna tendencia o patrón común en los datos de ambos países?
    ¿Cuáles son los períodos con mayor número de inmigrantes en ambos países?
    ¿Estás listo para avanzar?

# Lo que aprendimos en esta clase:

    Extraer una serie de datos de un DataFrame;
    Importar el módulo pyplot de la biblioteca Matplotlib;
    Graficar un gráfico con la biblioteca Matplotlib;
    Cambiar los ticks de los ejes X e Y;
    Mostrar el gráfico con la función plt.show();
    Modificar el tamaño del gráfico;
    Agregar un título al gráfico;
    Agregar etiquetas a los ejes X e Y;
    Crear una figura;
    Modificar la frecuencia de los ticks del eje X en una figura.

