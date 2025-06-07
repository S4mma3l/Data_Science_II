# Para saber más: descripción de los datos



Cuando trabajamos con cualquier conjunto de datos, necesitamos saber qué información nos aportan esos datos, porque solo así podremos estudiarlos y analizarlos para desarrollar una solución de análisis y procesamiento de datos.

En este curso trabajaremos con el conjunto de datos presentes en el archivo datos_hosting.json y, para avanzar en nuestros estudios sobre los datos que proporciona este archivo, entenderemos qué información trae cada columna.

    evaluacion_general: se refiere a la puntuación media otorgada para evaluar el alojamiento en la propiedad.
    experiencia_local: describe las experiencias ofrecidas durante su estancia en la propiedad.
    max_hospedes: informa el número máximo de invitados que permite la ubicación.
    descripcion_local: describe la propiedad.
    descripcion_vecindad: describe el vecindario alrededor de la propiedad.
    cantidad_baños: informa el número de baños disponibles.
    cantidad_cuartos: informa el número de habitaciones disponibles.
    cantidad_camas: informa el número de camas disponibles.
    modelo_cama: informa el modelo de cama ofrecido.
    comodidades: informa las comodidades que ofrece la propiedad.
    cuota_deposito: informa la tarifa mínima de depósito para la seguridad del hosting.
    cuota_limpieza: informa el cargo cobrado por el servicio de limpieza.
    precio: se refiere al precio base a cobrar por la estancia diaria en la propiedad.


# Para saber más: precisión de valores numéricos

Por lo general, cuando los datos son muy grandes y tenemos poca memoria disponible, es habitual utilizar tipos de datos más compactos para reducir el consumo de memoria. Sin embargo, siempre es importante asegurarse de que la elección del tipo de datos no perjudique la precisión o exactitud de los resultados.

Cuando trabajamos con números enteros con Python, podemos tener diferentes tipos de datos, cada uno con sus limitaciones y características. Durante las clases trabajamos con int64, un número entero con precisión de 64 bits. Para entender el significado de esta precisión, es importante conocer algunos términos técnicos, como byte y bit:

    Byte: es una unidad de medida de información, que representa un conjunto de 8 bits.
    Bit: es la unidad de información más pequeña utilizada en los sistemas digitales, y puede tomar los valores de 0 o 1.

Tipo entero

Con los conceptos de bit y byte claros, podemos comprender mejor el significado de int64, que es el tipo de entero que utiliza 8 bytes de almacenamiento: 8 bits en cada byte, lo que da como resultado 64 bits en total. Este tipo de entero es capaz de representar números muy grandes, que pueden oscilar entre -9.223.372.036.854.775.808 y 9.223.372.036.854.775.807.

Además, tenemos otros números enteros cuya precisión se puede definir, como int32, un tipo de datos entero que utiliza 4 bytes - 8 bits en cada byte, lo que da como resultado 32 bits en total. Es capaz de representar números enteros menores que los representados por int64, con un máximo de -2.147.483.648 a 2.147.483.647.

Puede ser más común encontrar los tipos int64 y int32, pero puede ser necesario, en algunas situaciones, utilizar otros tipos de datos enteros, como int8 o int16. Tipos de datos como estos son útiles cuando necesita ahorrar más memoria y no trabaja con valores grandes. Puede consultar los tipos de números enteros en la siguiente tabla:
Tipo de dado	Número de bits	Valor mínimo	Valor máximo
int8	8	-128	127
int16	16	-32.768	32.767
int32	32	-2.147.483.648	2.147.483.647
int64	64	-9.223.372.036.854.775.808	9.223.372.036.854.775.807

La elección de qué valor de precisión dependerá de la situación y la naturaleza de los datos que se manipulan. Si los valores que se analizan son relativamente pequeños, el uso de int32, por ejemplo, puede ser suficiente y puede ahorrar espacio en la memoria. Sin embargo, si estuviéramos trabajando con datos científicos, por ejemplo, que requieren valores muy grandes, es posible que necesitemos usar int64.

Tipo float

Además de los números enteros, otros tipos de datos, como float, también utilizan esta opción de precisión como opción para controlar el espacio de memoria. Al igual que los números enteros, el tipo float también tiene opciones de precisión: entre los tipos más comunes se encuentran float32 y float64.

El tipo float64 es un número de punto flotante con 64 bits de precisión, que representa un número decimal de hasta 15 dígitos. Por otro lado, float32 es más pequeño tanto en su capacidad de bits, con 32 en total, como en su capacidad de precisión decimal, con capacidad de precisión de hasta 7 dígitos.

# Tratando números en strings

Para realizar un estudio financiero de distribución salarial en una empresa es necesario transformar los datos relativos a los cargos y prepararlos para un estudio estadístico.

Por lo tanto, al leer el archivo con los datos, te encuentras con el siguiente DataFrame:
	Cargo	Cantidad	Salario
0	Gerencia	2 personas	$10.000 reales
1	Coordinación	1 persona	$8.000 reales
2	Supervisión	3 personas	$7.000 reales
3	Analista	4 personas	$5.000 reales
4	Asistente	5 personas	$4.000 reales
5	Operación	3 personas	$3.500 reales
6	Asistente	2 personas	$3.000 reales
7	Prácticas	1 persona	$1.500 reales
8	Asesoría	1 persona	$2.500 reales
9	Consultoría	1 persona	$6.000 reales

Selecciona la alternativa que hace que los datos de las columnas cantidad y salario se conviertan en valores numéricos, es decir, columnas int y float sin existencia de texto que acompañe a cada valor.

Para ayudarlo con sus pruebas, intente usar el siguiente código para crear el DataFrame df y encontrar la solución para la actividad:
```python
import pandas as pd
import numpy as np

# datos de la empresa
datos = {
    'cargo': ['Gerencia', 'Coordinación', 'Supervisión', 'Analista', 'Asistente', 'Operación', 'Asistente', 'Prácticas', 'Asesoría', 'Consultoría'],
    'cantidad': ['2 personas', '1 persona', '3 personas', '4 personas', '5 personas', '3 personas', '2 personas', '1 persona', '1 persona', '1 persona'],
    'salario': ['$10.000 reales', '$8.000 reales', '$7.000 reales', '$5.000 reales', '$4.000 reales', '$3.500 reales', '$3.000 reales', '$1.500 reales', '$2.500 reales', '$6.000 reales']
}

# transformando el diccionario en DataFrame
df = pd.DataFrame(datos)

# df es el DataFrame con los datos de la empres
df
```


Eliminamos los textos que están alrededor de los números con apply y lambda.
```python
df['cantidad'] = df['cantidad'].apply(lambda x: x.replace(' personas', '').replace(' persona', ''))
df['salario'] = df['salario'].apply(lambda x: x.replace('$', '').replace(' reales', ''))
```
Luego, transformamos las columnas a tipo numérico con astype.
```python
df['cantidad'] = df['cantidad'].astype(np.int64)
df['salario'] = df['salario'].astype(np.float64)
```
La función replace reemplaza textos con valores vacíos '', eliminándolos de la cadena original. Luego, se debe usar astype para convertir las columnas a numéricas, con el tipo int64 para la columna cantidady float64 para la columna salario.


# Desafio



Pongamos nuevamente en práctica todo lo que aprendimos durante la clase. He puesto los 2 nuevos conjuntos de datos disponibles para descargar a continuación:

    Proyecto Desafío 1: Ventas Online - dados_vendas_clientes.json;
    Proyecto Desafío 2: Administración de Condominios - dados_locacao_imoveis.json.

Recuerda: Hay dos proyectos de tratamiento que se construirán durante el curso. Así que guarde su código de construcción para cada desafío para poder aplicarlo a desafíos posteriores.

Etapa 2

    Proyecto Desafío 1: Ventas Online

Leímos la base de datos en el desafío anterior, ahora podemos seguir adelante con la transformación de estos datos. Así, el nuevo desafío del proyecto 1 será dividido en algunas metas:

    Eliminar datos en listas dentro del DataFrame;
    Verificar tipos de datos;
    Identificar columnas numéricas;
    Transformar la columna numérica a tipo numérico.

    Proyecto Desafío 2: Administración de Condominios

Leímos la base de datos en el desafío anterior, ahora podemos seguir adelante con la transformación de estos datos. Entonces, de la misma manera que en el proyecto 1, el desafío del proyecto 2 está listado en algunas metas:

    Eliminar datos en listas dentro del DataFrame;
    Verificar tipos de datos;
    Identificar columnas numéricas;
    Transformar la columna numérica a tipo numérico.

# En esta aula, aprendimos a:

    Identificar y transformar elementos dentro de las listas en una nueva línea del DataFrame con explode;
    Transformar datos textuales en datos numéricos con el método astype;
    Tratar los textos con datos numéricos para transformarlos con apply;
    Tratar varias columnas elemento por elemento con applymap.

