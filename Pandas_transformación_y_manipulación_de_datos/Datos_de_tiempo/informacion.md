# Para saber más: el tipo datetime

La clase datetime es un tipo de datos que representa una fecha y hora específicas en Python. Permite trabajar y manipular datos de año, mes, día, hora, minuto, segundo y microsegundo, así como días de la semana, como lunes, martes, miércoles, etc. Esta clase está definida en el módulo datetime y es fundamental para manipular fechas y horas en Python. Con él es posible realizar operaciones de cálculo de diferencias entre fechas, formatear fechas y horas en diferentes formatos, además de ser muy útil para analizar datos que involucran series temporales.

Con la biblioteca Pandas es posible realizar diversas operaciones con fechas y horas, como convertir datos de cadena a datetime, filtrar datos en función de intervalos de tiempo específicos, agregar datos por hora, día, mes o año, entre otras funcionalidades. Por tanto, con esta biblioteca es posible realizar diversas operaciones con fechas de forma sencilla y eficiente dentro de un conjunto de datos.

Biblioteca datetime

Podemos trabajar directamente con datetime a través de la biblioteca datetime, una biblioteca estándar de Python que proporciona clases para trabajar con fechas y horas. Con esta biblioteca, puede crear objetos de fecha y hora, realizar cálculos de tiempo, formatear fechas y horas en diferentes formatos y mucho más.

Dentro de la biblioteca datetime, existe la clase de fecha y hora, que representa una fecha y hora específicas. Vea un ejemplo:
```python
import datetime

# creando un objeto datetime con la fecha y hora actual
ahora = datetime.datetime.now()

print("Fecha y hora actual:", ahora)
```
En este ejemplo, el método now() de la clase datetime se utiliza para crear un objeto que representa la fecha y hora actuales. El objeto resultante se almacena en la variable ahora y luego se imprime en la pantalla usando la función print().

Otra clase importante en la biblioteca datetime es la clase date, que representa solo una fecha. Vea un ejemplo:
```python
import datetime
# creando un objeto date con la fecha de hoy
hoy = datetime.date.today()

print("Fecha de hoy:", hoy)
```
En este ejemplo, el método today() de la clase date se utiliza para crear un objeto que representa la fecha de hoy. El objeto resultante se almacena en la variable hoy y luego se imprime en la pantalla usando la función print().

La biblioteca datetime también le permite realizar operaciones matemáticas con fechas y horas. Vea un ejemplo de cómo calcular la diferencia entre dos fechas:
```python
import datetime

# creando dos objetos date con fechas diferentes
data_1 = datetime.date(2022, 1, 1)
data_2 = datetime.date(2023, 1, 1)

# calculando la diferencia entre las dos fechas
diferencia = data_2 - data_1

print("Diferencia entre las dos fechas:", diferencia)
```
En este ejemplo, se crean dos objetos date con fechas diferentes. Luego se utiliza el operador de resta para calcular la diferencia entre las dos fechas. El resultado se almacena en la variable diferencia y luego se imprime en la pantalla usando la función print().

Para profundizar en los usos del tipo datetime, consulte el artículo Python datetime: ¿Cómo configuro la fecha y la hora en Python?(https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python) y también la documentación de la biblioteca datetime.(https://docs.python.org/3/library/datetime.html)

# Transformando texto en fechas

Usted es responsable de analizar los datos de una empresa que vende productos. Recibiste un conjunto de datos con información sobre las ventas realizadas en los últimos meses, pero notaste que la columna "Fecha de venta" está en formato de cadena (texto), no en formato de fecha. Para realizar el análisis es necesario convertir esta columna al formato de fecha.

Considere el siguiente conjunto de datos con información sobre las ventas de la empresa:
	Fecha de venta	valor
0	01/01/2022	100
1	05/02/2022	150
2	10/03/2022	200
3	15/04/2022	250
4	18/04/2022	80
5	20/04/2022	180

Seleccione la alternativa que transforme los datos de la columna Fecha de venta hacia un tipo datetime.

Para ayudarlo con sus pruebas, intente usar el siguiente código para crear el DataFrame datos y encontrar la solución para la actividad:
```python
import pandas as pd

# Creando el DataFrame con las informaciones
datos = pd.DataFrame({
    'Fecha de venta': ['01/01/2022', '05/02/2022', '10/03/2022', '15/04/2022','18/04/2022','20/04/2022'],
    'valor': [100, 150, 200, 250,80,180]
})

# Mostrando el DataFrame
print(datos)
```
```python
 datos['Fecha de venta'] = pd.to_datetime(datos['Fecha de venta'], format='%d/%m/%Y')
```
El formato especificado %d/%m/%Y coincide con el formato original de la fecha en el string. Usando la función pd.to_datetime convertimos la columna “Fecha de venta” y con el parámetro format='%d/%m/%Y' podemos indicar el formato correcto del string, que es "día/mes/año".


# Desafío: hazlo tú mismo



En esta clase, aprendimos cómo manipular datos temporales usando datetime. Entendimos cómo transformar una columna a fecha y hora y luego manipular estos datos. Aun así, no todos los datos del conjunto inmuebles_disponibles.json fueron tratados.

Durante las clases de este curso, descubrimos cómo transformar y trabajar con valores numéricos, por ejemplo, eliminando valores numéricos dentro de un texto y transformándolos en un tipo numérico, como int64 o float64.

Sabiendo esto, en esta actividad te propongo transformar los datos de la columna precio del conjunto de datos inmuebles_disponibles.json al tipo numérico float64. Recordando que, antes de hacer esto, debes llenar los valores vacíos de la columna con un valor. Una sugerencia: reemplazar con el string '0.0'.

No dudes en seguir los mismos pasos dados en clase o, si lo prefieres, realizar otras mejoras, como eliminar algunos caracteres o palabras vacías. En el apartado “Opinión del instructor” encontrarás una posible resolución para esta actividad.

# Desafío: trabajando en otros contextos

Pongamos nuevamente en práctica todo lo que aprendimos durante la clase. He puesto los 2 nuevos conjuntos de datos disponibles para descargar a continuación:

    Proyecto Desafío 1: Ventas Online - dados_vendas_clientes.json;
    Proyecto Desafío 2: Administración de Condominios - dados_locacao_imoveis.json.

Recuerda: Estos dos proyectos de tratamiento se construyeron durante el curso. Por lo tanto, considere desarrollos previos para realizar este paso final.

Etapa 4

    Proyecto Desafío 1: Ventas Online

En los pasos anteriores ya hemos trabajado con varios tipos de datos, ahora podemos trabajar con datos de tiempo.

En la columna Fecha de venta tenemos fechas en el formato 'día/mes/año' (dd/mm/AAAA). Transforme estos datos al tipo datetime y busque una forma de visualización de subconjunto que pueda contribuir al objetivo del contexto en el que se insertan los datos.

Si no recuerdas el problema del Proyecto Desafío 1, te dejo el texto de la situación a continuación para que sea más fácil encontrar la información:
```text
El objetivo de este proyecto es analizar los resultados de un evento con los clientes de una empresa de venta online. Se recopiló un conjunto de datos que contiene los clientes que gastaron más en productos dentro de los 5 días posteriores a la venta, que es la duración del evento. Este análisis identificará al cliente con la mayor compra esa semana, quien recibirá un premio de la tienda, y posteriormente, puede ayudar a la empresa a crear nuevas estrategias para atraer más clientes.
```

    Proyecto Desafío 2: Administración de Condominios

Al igual que en el Proyecto Desafío 1, trabajamos con todas las columnas excepto las que involucran fechas.

En las columnas datas_de_pagamento y datas_combinadas_pagamento tenemos fechas en el formato 'día/mes/año' (dd/mm/AAAA). Transforme estos datos al tipo datetime y busque una forma de visualización de subconjunto que pueda contribuir al objetivo del contexto en el que se insertan los datos.

Si no recuerdas el problema del Proyecto Desafío 2, te dejo el texto de la situación a continuación para que sea más fácil encontrar la información:
```text
Administrar condominios es una tarea que requiere mucha atención y organización. Entre las diver
```

# En esta aula, aprendimos a:

    Identificar el tipo de datos datetime;
    Transformar datos para el tipo datetime y
    Manipular columnas de tipo datetime a través de métodos.

