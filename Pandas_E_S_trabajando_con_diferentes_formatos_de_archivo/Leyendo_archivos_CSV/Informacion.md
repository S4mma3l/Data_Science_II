### Para saber más: error de codificación - ¿cómo solucionarlo?

Giovanna es una científica de datos que trabaja en una empresa de comercio electrónico. Ella es responsable de analizar datos de ventas para identificar patrones y tendencias que puedan ayudar a la empresa a tomar decisiones informadas.

Recientemente, le asignaron una nueva tarea: analizar un archivo CSV que contiene información sobre las ventas de la empresa durante un período determinado. Para ello, Giovanna intentó leer un archivo CSV en Google Colab, usando la biblioteca Pandas con el siguiente comando:
```python
import pandas as pd
df = pd.read_csv('datos.csv')
```
Sin embargo, apareció el siguiente error:

En español, el mensaje significa UnicodeDecodeError: el códec 'utf-8' no puede decodificar el byte 0xff en la posición 0: byte de inicio inválido

Pero ¿qué significa eso? ¿Qué es esto de UTF-8?

El error de encoding ocurre cuando la biblioteca Pandas no puede interpretar correctamente los caracteres en un archivo CSV. Esto puede suceder cuando contiene caracteres especiales que la biblioteca Pandas no reconoce o cuando se guardó en un formato de codificación diferente al esperado.

Para resolver este error, es necesario identificar la codificación correcta del archivo CSV y especificarla al cargar el archivo con la biblioteca Pandas. Esta codificación predeterminada es UTF-8, pero en algunos casos, es posible que el archivo se haya guardado con una codificación diferente, como ISO-8859-1.

UTF-8 es una codificación de caracteres universal que se utiliza para representar caracteres de diferentes idiomas de una manera compatible con Internet y los sistemas de computadora en general. Las siglas UTF significan Unicode Transformation Format (Formato de Transformación Unicode) y el número 8 indica que esta codificación asocia una secuencia de 1 a 4 bytes (8 a 32 bits) a cada carácter.

La codificación UTF-8 se usa ampliamente en Internet y en sistemas informáticos de todo el mundo, ya que permite representar caracteres de diferentes idiomas en un solo conjunto de caracteres. Además, esta codificación puede preservar la compatibilidad con codificaciones más antiguas como ASCII, lo que la convierte en una opción popular para crear y compartir archivos de texto.

Quizás estés pensando ahora mismo: ¿cómo podría Giovanna descubrir cuál es la codificación del archivo que está intentando leer?

Hay algunas formas de resolver esto, sin embargo, tendremos la oportunidad de experimentar una forma práctica de hacerlo en el propio Google Colab. ¿Vamos allá?

Podemos usar una biblioteca llamada chardet para detectar el encoding de un archivo CSV. Para usar esta biblioteca en Google Colab, simplemente importela:
``` python
import chardet

Luego escribimos el siguiente bloque de código:

with open('datos.csv', 'rb') as file:
    print(chardet.detect(file.read()))
```
Observe que la primera línea de este código abre el archivo CSV en modo de lectura binaria rb y asigna el objeto del archivo devuelto a una variable llamada file.

En la segunda línea de código, el contenido del archivo CSV se lee usando el método read() y el resultado se pasa a la función chardet.detect(), que devuelve un diccionario que contiene información sobre la codificación más probable del archivo. El resultado se imprime con la función print() que muestra la codificación y la confianza asociada con esa codificación.

Al ejecutar el código Giovanna obtuvo el siguiente resultado:

{'encoding': 'UTF-16', 'confidence': 1.0, 'language': ''}

Ahora ella sabe que es probable que el archivo CSV esté codificado con UTF-16 con una confianza de 1.0. Para especificar la codificación correcta al cargar el archivo CSV con la biblioteca Pandas, puede utilizar un parámetro llamado encoding:

df = pd.read_csv('datos.csv', encoding='UTF-16')

De esta manera, la biblioteca Pandas cargará el archivo CSV usando la codificación UTF-16, lo que resolverá el error de codificación. Entonces, si alguna vez intentas leer un archivo y obtienes el mismo error, ¡recuerda este consejo!

Si deseas profundizar más en el tema, aquí te dejamos algunos enlaces a materiales que fueron utilizados como referencia:

    Instituto de Matemáticas y Estadística - IME/USP: Unicode y UTF-8 [](https://www.ime.usp.br/~pf/algoritmos/apend/unicode.html#detection)
    IBM: ¿Qué es Unicode? https://www.ibm.com/docs/pt-br/workload-automation/9.3.0?topic=support-what-is
    Kaggle: codificaciones de caracteres https://www.kaggle.com/code/alexisbcook/character-encodings/tutorial