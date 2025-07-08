# ¿Por qué transformar los datos?

Acerca de la transformación de datos, marque la alternativa correcta:

Una de las principales razones para transformar algunos tipos de datos es intentar corregir la asimetría que la distribución de los datos pueda presentar.

¡Correcta! Este fue el principal objetivo de la transformación que llevamos a cabo en nuestro curso.

# Un poco más sobre las transformaciones logarítmicas

Usamos la biblioteca numpy para realizar la transformación de datos. numpy es un paquete fundamental para la computación científica en Python, que proporciona un conjunto muy amplio de operaciones matriciales y matemáticas.

Con base en nuestros videos, marque la opción que muestra la forma correcta de realizar la transformación logarítmica de la variable Valor, del DataFrame datos. Suponga que esta variable tiene algunos registros con valor cero.
Seleccione una alternativa
```python
import numpy as np
np.log(datos['Valor'] + 1)
```
¡Correcta! Como la variable tiene valores cero en algunos registros, la forma más correcta de transformación es agregar una constante, diferente de cero, a los datos, para evitar la pérdida de información, ya que log(0) no existe.

# Haga lo que hicimos en aula: Transformación de variables



Consolidando su conocimiento

Es hora de que sigas todos los pasos que he dado durante este video:

    Importar la biblioteca numpy
    Aplicar la transformación logarítmica a los datos del dataset
    Graficar la distribución de frecuencias de la variable dependiente transformada
    Graficar los diagramas de dispersión entre las variables transformadas del dataset
    Analizar la dispersión entre las variables transformadas

Si ya lo ha hecho, excelente. Si no es así, es importante que ejecutes lo que se vio en los videos para poder continuar con el siguiente video.


# Lo que aprendimos en esta aula:

    Como aplicar la transformación logarítmica a los datos del dataset.
    Como graficar la distribución de frecuencias de la variable dependiente transformada.
    Como graficar los diagramas de dispersión entre las variables transformadas del dataset.
    Cómo analizar la dispersión entre las variables transformadas.

