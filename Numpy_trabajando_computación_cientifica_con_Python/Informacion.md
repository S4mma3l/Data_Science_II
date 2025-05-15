### Numpy: trabajando computación cientifica con Python

Introducción

En aplicaciones científicas, de ingeniería y principalmente de ciencia de datos, existe la necesidad de realizar cálculos numéricos especializados.

Cuando haces la suma de todos los valores de una columna en un software de hojas de cálculo o incluso operaciones matemáticas entre diferentes columnas, hay un código implementado para hacer estas operaciones posibles. De la misma manera, si has utilizado una función de una biblioteca de Python que realiza regresión lineal o un algoritmo de machine learning cualquiera, debes saber que este código es la traducción de un conjunto de ecuaciones matemáticas a código. Esta implementación necesita ser eficiente y fácil de comprender. Cuanto más cercano esté el código escrito a la escritura matemática, mejor.

En este contexto, en Python, surge NumPy. Esta es una poderosa biblioteca ampliamente utilizada que ha revolucionado el segmento de computación científica, principalmente debido al carácter abierto del lenguaje Python. Con NumPy, es posible realizar operaciones matemáticas complejas con matrices de forma eficiente y optimizada. ¿Pero qué es exactamente y cómo funciona NumPy?
¿Qué es NumPy?

NumPy, una abreviatura de Numerical Python, es una biblioteca de código abierto de Python para computación científica, un campo de estudio que utiliza recursos computacionales para comprender y resolver problemas. Esta biblioteca permite trabajar con la manipulación de objetos array multidimensionales, así como con sus derivados, como matrices, secuencias y otros. Además de eso, también posee una amplia variedad de operaciones rápidas con los arrays, incluyendo operaciones matemáticas y lógicas, manipulación de formato, ordenación y selección, herramientas de estadística y cálculo, y mucho más.

La biblioteca NumPy fue lanzada en 2005 por el científico de datos Travis Oliphant, con la propuesta de ser una herramienta rápida, eficiente y fácil de usar, permitiendo así la realización de cálculos numéricos y matemáticos a gran escala, a través de la funcionalidad llamada vectorización. Por eso, se ha convertido en una de las bases fundamentales para el análisis de datos, el aprendizaje automático (machine learning) y la computación científica en general, estando presente también en la construcción de varias bibliotecas de ciencia de datos, incluyendo: Pandas, Matplotlib, Scikit-learn, SciPy, y mucho más.

Una curiosidad sobre esta biblioteca es que también ha estado presente en trabajos de descubrimientos científicos importantes, como la detección de la primera imagen de un agujero negro y la detección de ondas gravitacionales.

¿Pero cómo funciona exactamente NumPy?
Estructuras básicas de NumPy

NumPy funciona a través de estructuras llamadas arrays, que son estructuras de datos homogéneas, es decir, donde los elementos poseen el mismo tipo. Estas estructuras pueden tener varios formatos y dimensiones, que varían según las necesidades de cada tipo de proyecto. De manera general, para varios tipos de aplicación, trabajamos hasta la tercera dimensión, pero existen casos donde podemos necesitar más.

El concepto de dimensiones puede aplicarse en Python a partir del concepto de listas anidadas (nested lists). Para eso, utilizaremos las siguientes estructuras:
img1[](a53vcw6n.png)

Escalar: Un elemento único, sin dimensiones. Puede ser un entero, flotante, hexadecimal, caracter y varios otros tipos de datos.

En Python, después de importar la biblioteca, definimos un escalar como:
```python
import numpy as np
np.array(42)
```
Array unidimensional: una lista de escalares donde podemos identificar cada uno de ellos por su posición, o índice, en la lista. Es necesario destacar que todos los elementos escalares aquí poseen el mismo tipo, y aunque no se especifique durante la definición del array, NumPy trabajará en una rutina para determinar el tipo que garantice la homogeneidad.
```python
np.array([4,5,22,20])
```
Array bidimensional: una lista de arrays unidimensionales, con el formato de una matriz (tabla), donde necesitamos especificar una posición de fila y una posición de columna para localizar un elemento escalar.

```python
np.array([3,2,7],
         [4,9,1],
         [5,6,8])
```
img 2[](ee8l4327.png)

Array tridimensional: una lista de arrays bidimensionales. Un ejemplo de aplicación de un array tridimensional es la matriz de imágenes RGB, como se puede observar en el funcionamiento de un televisor. En este caso, tenemos una estructura bidimensional (el formato de pantalla), donde podemos localizar un píxel con una referencia vertical y otra horizontal. Para cada píxel, también tenemos una representación de un array de 3 elementos, que es la unión de tres LEDs de colores rojo, verde y azul. Entonces, a nivel fundamental, podemos interpretar una imagen como:
img3[](i70aglfw.png)

Array multidimensional (n-dimensional): las operaciones de creación de arrays en NumPy no están limitadas solo a las dimensiones anteriores: es posible construir estructuras de cantidades mayores, tanto como sea necesario, siempre que los objetivos del mismo nivel tengan el mismo formato. Una manera de ilustrar estos nuevos niveles es a través del siguiente esquema:
img4[](vr8o7jyq.png)

En este esquema, cuando llegamos a la cuarta dimensión y más allá, es más difícil visualizar la matriz como un objeto geométrico. En su lugar, podemos interpretar una matriz de orden superior como un objeto matemático que contiene información sobre otros objetos matemáticos.

Por ejemplo, una matriz de cuarto orden puede ser vista como una matriz de matrices de matrices, es decir, cada elemento de la matriz es una matriz de matrices. Podemos interpretar esta matriz como un objeto matemático que contiene información sobre varios objetos matemáticos más simples.
Broadcasting

El broadcasting es una funcionalidad de NumPy que permite trabajar con operaciones en arrays de formas y tamaños diferentes, sin necesidad de crear copias de los datos. Por este motivo, es una técnica que ahorra tiempo y memoria. En muchos casos, el broadcasting puede reducir el número de líneas de código necesarias para realizar una determinada operación.

Por ejemplo, en la operación a continuación:
```python
import numpy as np

a = np.array([1,2],[3,4])
b = np.array([10,20])

a + b
```

En el ejemplo anterior, estamos trabajando con la suma de dos arrays con dimensiones diferentes, en este caso, un array bidimensional y un array unidimensional. Sin embargo, NumPy puede analizar las dimensiones a través de reglas preestablecidas y ejecutar la operación, retornando:
```python
array([[11,24],
       [13,24]])
```
NumPy en la computación científica

Siendo una biblioteca de Python, una gran ventaja de trabajar con NumPy es la posibilidad de integración con otras bibliotecas del gran ecosistema de Python. Esto abre espacio para trabajar con soluciones end-to-end, que van desde la recolección de datos, procesamiento, hasta la entrega del producto final, como por ejemplo un panel de control o un sistema con un análisis detallado de modelos de aprendizaje automático.

Esta característica, sumada al hecho de que la biblioteca es de código abierto y libre, convierte a NumPy en un gran competidor de otras soluciones presentes en el mercado y en la academia, como MATLAB, Octave, Scilab, entre otros.
### Instalación de NumPy

Al igual que con otras bibliotecas importantes en Ciencia de Datos, como Pandas, la instalación sugerida como la más sencilla en la documentación de NumPy es a través de la instalación de Anaconda.
img 5[](i70aglfw.png)

Anaconda es un entorno de desarrollo dirigido a Ciencia de Datos con Python y R, que descarga varias bibliotecas y software de uso popular en el campo. Entre las bibliotecas descargadas, también tenemos NumPy. Puedes aprender cómo descargar Anaconda en Windows a través de la documentación oficial de Anaconda. https://docs.anaconda.com/free/anaconda/install/windows/

Otra forma de descargar la biblioteca NumPy es utilizando el administrador de paquetes de Python, PIP.

Una vez que hayas descargado Python desde el sitio oficial (https://www.python.org/downloads/), podemos seguir estos pasos:

    Atención: Caso tu tengas más de un disco rigido en su computadora, es necesario garantir que la instalación esta siendo hecha en el mismo disco donde el Python fue instalado.

    Para empezar, debemos abrir el Símbolo del sistema de tu sistema operativo. En Windows, presiona las teclas de acceso directo Windows + R, escribe "simbolo del sistema", y haz clic en la opción "Ejecutar como administrador":
    img 6 [](ivf7xkl3.png) img 7[](d1tymran.png)

    El Símbolo del sistema se abrirá y mostrará la pantalla negra del terminal. En este momento, podemos verificar la versión de Python instalada en la máquina con el comando python --version y asegurarnos de que podemos continuar:
```python
    python --version
```
```python
    Python 3.12.0
```
    Si aún no tienes PIP instalado en la máquina, puedes descargarlo utilizando un módulo nativo de Python para eso, como el comando:
```python
    python -m ensurepip --upgrade
```
    Y ahora que ya tenemos PIP descargado en la máquina, podemos usarlo para instalar NumPy con el comando:
```python
    pip install numpy
```
    ¡Listo! Ahora tienes NumPy descargado en tu máquina.

Ir más allá

Si deseas sumergirte aún más en los contenidos de Pandas y Ciencia de Datos, aquí en Alura Latam tenemos la Formación Python para Data Science. La formación aborda las principales herramientas utilizadas en Ciencia de Datos con Python, como Pandas, NumPy, Matplotlib, Seaborn y mucho más. En ella, construimos varios proyectos prácticos para completar tu portafolio como profesional de datos.