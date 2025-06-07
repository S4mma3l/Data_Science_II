# Otras formas de tratar el texto

Durante la clase tratamos el texto elemento por elemento usando el comando str que nos permitió trabajar con strings y usar sus métodos nativos. Pero existe otra forma de tratar estos valores elemento por elemento: mediante el método apply. Con eso en mente, considere el siguiente escenario:

Una empresa famosa quiere controlar las menciones de su marca en las redes sociales. Para ello, se recopilaron miles de informes de clientes sobre experiencias con su marca. Ahora, la misión es transformar estos textos para que puedan ser analizados.

Considerando que el DataFrame de pandas con los datos se llama df y que la columna experiencias_clientes contiene los relatos de los clientes sobre la marca, seleccione la alternativa que muestre correctamente el tratamiento de la transformación de letras a mayúsculas en la columna, utilizando el método apply.
```python
df['experiencias_clientes'] = df['experiencias_clientes'].apply(lambda x: x.upper())
```
Se usa apply para aplicar una función a cada elemento de una columna. En este caso, la función lambda se utiliza para transformar todas las letras de la columna experiencias_clientes a mayúsculas. Al usar la función lambda dentro del método apply, estamos aplicando la función elemento por elemento en la columna.

# Para saber más: profundizando en Regex



Regex (o expresión regular) es una secuencia de caracteres que define un patrón de búsqueda en un texto. Es una herramienta poderosa y versátil que le permite buscar, reemplazar y manipular patrones de texto de manera eficiente. Regex se usa ampliamente en diferentes áreas, incluida la programación, la ciencia de datos y el procesamiento de textos.

En la ciencia de datos, las expresiones regulares se utilizan a menudo para procesar datos de texto sin formato. Algunas de estas aplicaciones incluyen limpieza de datos, donde se pueden usar expresiones regulares para buscar y reemplazar ciertos caracteres. También se puede utilizar en proyectos de clasificación; un ejemplo es el uso de expresiones regulares para ayudar a encontrar patrones en el texto de los correos electrónicos, lo que ayuda a clasificar si son spam o no.

En general, las expresiones regulares permiten a los científicos de datos procesar, analizar y clasificar grandes volúmenes de datos de texto de forma eficiente y automatizada. El uso adecuado de expresiones regulares puede ayudar a extraer información valiosa de los datos de texto, además de facilitar la limpieza y organización de esos datos.

Puedes crear una expresión regular con la ayuda del sitio web regex101.com.(https://regex101.com/) Si quieres saber más sobre regex y su aplicación en bases de datos, vale la pena leer el artículo Principales casos de uso de Regex para procesamiento de datos(https://www.alura.com.br/artigos/principais-casos-uso-regex-para-tratamento-dados), que muestra una aplicación regex en banco de datos.

Puede estudiar expresiones regulares y aprender algunas de sus reglas básicas, como las presentadas en el curso, y a medida que se familiarice con el uso de expresiones regulares, podrá comenzar a explorar otras funciones y características más avanzadas para crear patrones más complejos en sus códigos.

#  Desafío: hazlo tú mismo



Aprendimos a manipular elementos textuales con el comando str. Luego, usamos expresiones regulares para limpiar elementos no deseados en el texto y, finalmente, transformamos el texto tratado en una lista, construyendo un token.

Durante las clases transformamos dos columnas descripcion_local y comodidades buscando la tokenización. Pero aún falta la columna descripcion_vecindad, que también merece la pena transformar.

Por lo tanto, en esta actividad te propongo realizar el proceso de tokenización para la columna descripcion_vecindad presente en el conjunto de datos datos_hosting.json.

No dudes en seguir los mismos pasos dados en clase o, si lo prefieres, realizar otras mejoras, como eliminar algunos caracteres o palabras vacías. En el apartado “Opinión del instructor” encontrarás una posible resolución para esta actividad.

# Desafío: trabajando en otros contextos



Pongamos nuevamente en práctica todo lo que aprendimos durante la clase. He puesto los 2 nuevos conjuntos de datos disponibles para descargar a continuación:

    Proyecto Desafío 1: Ventas Online - dados_vendas_clientes.json;
    Proyecto Desafío 2: Administración de Condominios - dados_locacao_imoveis.json.

Recuerda: Hay dos proyectos de tratamiento que se construirán durante el curso. Así que guarde su código de construcción para cada desafío para poder aplicarlo a desafíos posteriores.

Etapa 3

    Proyecto Desafío 1: Ventas Online

En el paso 2, trabajamos en la transformación de datos numéricos. Ahora podemos trabajar con valores textuales.

Debido a una inestabilidad en el sitio web de la empresa, tuvimos problemas con los nombres de los clientes durante el guardado. Esto resultó en una columna de nombres de clientes con una combinación de letras, mayúsculas y minúsculas, números y otros caracteres.

Sabiendo esto, manipula los textos de la columna Cliente para que el resultado sean los nombres de los clientes en letras minúsculas, con ausencia de caracteres especiales o números.

    Proyecto Desafío 2: Administración de Condominios

En el paso 2, trabajamos en transformar los datos numéricos. Ahora podemos trabajar con valores textuales.

Buscando explicar la organización de la identificación de los apartamentos, durante la creación del conjunto de datos se añadió el texto (blocoAP). Este texto informa que los nombres de los apartamentos están organizados con la letra mayúscula seguida del número del apartamento. Sin embargo, esto no aporta ninguna información a nuestros datos, por lo que resulta interesante eliminar este texto del conjunto de datos.

Con esto, manipule los textos de la columna apartamento para eliminar el texto (blocoAP) del DataFrame.

# En esta aula, aprendimos a:

    Manipular elementos textuales en un DataFrame;
    Trabajar con expresiones regulares (regex) para tratar el texto;
    Transformar textos en listas;
    Realizar el proceso de tokenización de strings.


