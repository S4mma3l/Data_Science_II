

En este curso, vamos a trabajar con el storytelling de la empresa Zoop, una gran minorista que atiende a todas las regiones de Brasil a través de su comercio electrónico. Es conocida por su amplia variedad de productos, buscando atender a todo tipo de público.

Como analista de datos de Zoop, has recibido una solicitud del Director de Datos para extraer los datos de ventas y el perfil de los clientes, y generar visualizaciones que ayuden en la construcción de informes, de acuerdo con algunos lineamientos proporcionados por las partes interesadas. Esto implica realizar un rápido análisis del público que tenemos en la tienda virtual y del ingreso de la empresa.

En total, se te presentarán 7 preguntas para que puedas contribuir en la construcción del storytelling del informe de la empresa. Estas preguntas serán respondidas a través de visualizaciones que puedan ser presentadas a la dirección de la empresa, destacando los datos de facturación, el perfil del cliente y otros indicadores que puedan ayudar en la toma de decisiones para su tienda online.

En este proyecto, importaremos dos bases de datos:

    Datos de clientes del comercio electrónico de Zoop, separados por el código identificador de la compra.
    Datos de ventas del comercio electrónico de Zoop en 2023, separados por el código identificador de la compra.

Estos datos serán leídos a través de enlaces (URL) del repositorio del proyecto en GitHub.

Nuestro objetivo es optimizar, mediante el uso de la IA generativa de ChatGPT, el proceso de análisis exploratorio de datos (AED) y la creación de visualizaciones utilizando el lenguaje Python. Todo este proceso tiene en cuenta el corto plazo para las entregas y la calidad de los resultados.

Antes de empezar… Necesitarás descargar el cuaderno del curso y subirlo a tu Google Colab. Para usar este entorno, es necesario tener una cuenta de Gmail, ya que todo el cuaderno se almacenará en Google Drive.

¿Todo listo? ¡Empecemos con el trabajo práctico! ¡Buen estudio y adelante!

# Generando un prompt para la exploración de datos

Daniela es una analista de datos en Serenatto - Café & Bistrô, una franquicia de restaurantes populares que ofrece una amplia variedad de platos de la cocina francesa e italiana. Ha recibido una solicitud para analizar, en poco tiempo, los datos de las ventas diarias de la sucursal de San José. Podemos observar una parte de los datos en la tabla a continuación:
id	fecha	producto	valor	metodo_pago
0	01-01-2024	Agua Mineral	3.00	Tarjeta de Débito
1	01-01-2024	Salteña	5.00	Tarjeta de Débito
2	01-01-2024	Petit Gateau	7.00	Tarjeta de Crédito
3	01-01-2024	Jugo de Fresa	4.50	Efectivo
4	01-01-2024	Crostini	8.00	Efectivo

Ella pensó en elaborar un pequeño prompt que realizara las siguientes tareas: leer el archivo .xlsx con los datos pasándolos a un DataFrame, cambiar el formato de la fecha a uno que pudiera ser fácilmente utilizado en visualizaciones, explorar brevemente los datos y crear una nueva base manteniendo solo las columnas con las fechas y los valores de las ventas.

Considerando las etapas descritas anteriormente, ¿cuál de los prompts a continuación tiene mayor probabilidad de ser interpretado correctamente por ChatGPT, generando así los tratamientos deseados por Daniela?

Crea un código en Python que lea la base de datos ventas.xlsx pasándola al DataFrame “df”. Cambia el formato de la columna “fecha” a datetime, donde la fecha originalmente está en el formato “DD-MM-YYYY”. Explora brevemente los datos y crea un DataFrame llamado “ventas” con solo las columnas “fecha” y “valor” de “df”.

Este es el prompt ideal, ya que especifica todos los procesos necesarios para lograr el comportamiento deseado, generando un nuevo DataFrame con los datos resumidos.


# Para saber más: como crear un buen prompt con chat gpt


Una de las habilidades más importantes para la interacción con IAs generativas como ChatGPT es la capacidad de crear buenos prompts, guiando la herramienta de acuerdo con tu conocimiento sobre el negocio. La creación de un prompt eficaz en ChatGPT es fundamental para obtener resultados precisos y relevantes para la resolución de problemas.

En el contexto de un proyecto de análisis de datos, como el que estamos trabajando aquí, un prompt bien elaborado puede ser la clave para obtener insights valiosos. A continuación, se presentan algunas buenas prácticas y ejemplos, teniendo en cuenta un proyecto simple de Ciencia de Datos:

Sé específico y directo:

Explica directamente lo que deseas que ChatGPT ejecute. Esto ayuda a la IA a entender mejor tu necesidad, proporcionando respuestas más precisas.

Ejemplo: “Realiza un análisis exploratorio de datos en la base ‘zoop_ventas.csv' usando las bibliotecas de manipulación de datos de Python. Presenta un resumen estadístico de las ventas por región”.

Proporciona contexto cuando sea necesario:

Informa a ChatGPT del contexto del proyecto, incluyendo datos, objetivos y restricciones. Esto puede mejorar significativamente la calidad de las respuestas. Sin embargo, evita información innecesaria que pueda confundir a la IA.

Ejemplo: "Estoy trabajando en un proyecto de análisis de ventas de una tienda minorista. La base de datos contiene información de ventas diarias por categoría de producto y región en 2023. Ayúdame a calcular la suma de las ventas de 'Electrónicos' por trimestre".

Especifica el formato de la respuesta:

Indica el formato deseado para la respuesta, como gráficos, tablas o explicaciones detalladas.

Ejemplo: "Crea un gráfico de líneas que muestre la evolución de las ventas a lo largo del último año, segmentado por categoría de productos".

Indica el nivel de detalle deseado:

Deja claro el nivel de detalle o profundidad de la explicación que estás buscando. Esto ayuda a la IA a ajustar la respuesta a tu necesidad de comprensión.

Ejemplo: "¿Podrías proporcionarme un ejemplo comentado de cómo usar la función groupby() de pandas para agrupar datos por categoría y calcular la suma total de ventas para cada grupo?"

Usa términos técnicos correctos:

Pon atención a la terminología específica relacionada con tu área de interés. Esto asegura que la IA comprenda el dominio de tu pregunta y responda de forma adecuada.

Ejemplo: “¿Cómo implemento un modelo de regresión lineal en Python usando scikit-learn para predecir ventas futuras con base en gastos de publicidad?”

Divide tareas complejas en etapas simples:

Si el proyecto involucra varias etapas, divídelo en partes más pequeñas e instruye a ChatGPT paso a paso. Esto facilita que la IA te ayude de manera eficaz.

Ejemplo:

"¿Cómo puedo manejar valores faltantes en mi conjunto de datos usando pandas?"

"¿Cuál es la mejor manera de visualizar la distribución de edades en mi conjunto de datos usando matplotlib?"

“¿Podrías ajustar el visual de la distribución de edades colocando las etiquetas y labels con tamaño 12 y color #CCCCCC?”

Mantente abierto a interacciones:

Esté siempre preparado(a) para realizar ajustes en tus prompts basados en las respuestas recibidas. La interacción puede ayudar a refinar las respuestas y obtener exactamente lo que necesitas.

Ejemplo: “Esta respuesta puede mejorar. ¿Qué tal si redondeamos los valores a dos decimales y mostramos en el gráfico solo los valores mayores a 1 millón (1e6)?”

Estos consejos son fundamentales en la construcción de prompts bien instruidos, como los que encontrarás a lo largo de este curso. Observa cómo se describen los pasos y acciones en los prompts del curso y cómo puedes aplicarlos en tu proyecto utilizando ChatGPT.

Asegúrate de comunicar tus intenciones de forma precisa, dividir tareas complejas en etapas manejables y proporcionar ejemplos cuando sea apropiado. Esto te ayudará a obtener respuestas más relevantes y útiles para tu proyecto, haciendo la interacción con el chat más eficaz.

# Ajustando el prompt

Juan está aprendiendo cómo utilizar ChatGPT en un proyecto de análisis de datos que pretende agregar a su portafolio. Durante su investigación, encontró dos bases que contenían datos sobre el PIB y los Valores Agregados de Bienes y Servicios.

La primera base (pib_estados) tiene el siguiente formato en sus primeras 10 líneas:
año	estado	region	pib	impuesto_liquido	va
0	2002	AC	Norte	2971301277	228471013
1	2002	AL	Noreste	11536852891	937933640
2	2002	AM	Norte	22093338008	3876992799
3	2002	AP	Norte	3173342678	199411105
4	2002	BA	Noreste	58842975944	8368251983
5	2002	CE	Noreste	28718840361	3677581705
6	2002	DF	Centro-Oeste	53902199799	6926279208
7	2002	ES	Sureste	27048996552	4743779770
8	2002	GO	Centro-Oeste	38629364574	4484244717
9	2002	MA	Noreste	15924002514	1357799240

La segunda base (va_estados) tiene el siguiente formato en sus primeras 10 líneas:
	año	estado	va_agropecuaria	va_industria	va_servicios	va_adespss
0	2002	AC	284337190	355041179	1071069387	1032382508
1	2002	AL	2474313378	2168565501	3530694271	2425346094
2	2002	AM	1239199988	7770508485	5965772157	3240864579
3	2002	BA	6612124525	11847928358	22322715730	9691955360
5	2002	CE	1885081291	5671628251	11594124567	5890424538
6	2002	DF	165416683	4089946543	21927573402	20792983964
7	2002	ES	784413923	8164182067	9766872482	3589748305
8	2002	GO	5051406044	8737191313	14922918441	5433604075
9	2002	MA	1867205923	2732201913	6537050283	3429745159

Juan desea concatenar las bases en una sola, manteniendo solo las columnas con el año, el estado, la región, el PIB, los impuestos líquidos, el valor agregado y el valor agregado de la agropecuaria. Así, Juan creó el siguiente prompt:
Crea un código que concatene las bases “pib_estados” y “va_estados” en una única tabla por año y estado, manteniendo las columnas con el año, el estado, la región, el PIB, los impuestos líquidos, el valor agregado y el valor agregado de la agropecuaria.

Con base en este prompt y lo que hemos aprendido a lo largo de las clases, ¿qué podemos agregar para mejorarlo? Elige las alternativas correctas.

Especificar detalles, como el nombre correcto de las columnas para que el código sea más preciso y requiera menos modificaciones.

Dejar claro el nombre de las columnas puede ayudar a crear un código menos genérico y más específico para el problema que deseas resolver.
Alternativa correta

Definir cuál será el lenguaje de programación que utilizará ChatGPT para crear el código deseado.

Dejar clara la elección del lenguaje de programación es extremadamente importante para guiar a la IA en la resolución del problema, de acuerdo con los paquetes específicos del lenguaje que estés utilizando.

# Desafio

Has recibido una nueva solicitud de las partes interesadas de Zoop, en la que será necesario agregar más columnas de otra base de datos a la tabla consolidada en el video anterior.

A diferencia de las actividades que estamos realizando en los videos de este curso, aquí también utilizaremos esta nueva base para la construcción de los visuales dentro de los ejercicios de "Manos a la obra", enfocándonos en las demandas presentadas en las instrucciones de los ejercicios.

Los archivos que vamos a utilizar en esta parte del proyecto son:

    Datos de clientes del e-commerce de Zoop, separados por el código identificador de la compra.
    Datos de ventas del e-commerce de Zoop en 2023, separados por el código identificador de la compra.
    Datos de clientes pre-registrados en Zoop Pay, la billetera digital de Zoop que está en proceso de implementación.

Estos datos se leerán a través de enlaces (URL) que compartimos a continuación:

url_clientes = "https://gist.githubusercontent.com/ahcamachod/d08898e1cc84c7271856e78d9558ca3d/raw/2f7e1fa53711efe6433a5c5ec79948f600591cb9/clientes_zoop.csv"
url_ventas = "https://gist.githubusercontent.com/ahcamachod/966d7162a3c3a2769b8770b35abf1bcc/raw/d79941b3fa46a450f3611589abd8663399c1277b/ventas_zoop.csv"
url_zoop_pay = "https://gist.githubusercontent.com/ahcamachod/ce728231a836a973c0df94a9f03ed871/raw/8db6da43d7cd94fcab937208067d0fceb521b78c/zoop_pay.csv"

Ahora que ya sabemos cuáles son los datos necesarios para la realización del proyecto, vamos a abrir el notebook mencionado anteriormente y realizar la siguiente actividad:

Construye y ejecuta un prompt en ChatGPT solicitando que lea las tres bases de datos y cree una única tabla concatenándolas. Recuerda ser bastante específico en cuanto al orden de las columnas y cuáles serán necesarias para realizar la concatenación de los datos, además de tratar la columna de fecha para el formato adecuado.

Consejo 1: Para facilitar el proceso, pide a ChatGPT que primero concatene los datos de clientes y ventas en una tabla llamada df y, finalmente, que concatene esta nueva tabla con la base de clientes pre-registrados en Zoop Pay, generando así la tabla consolidada con todos los datos. Este proceso puede realizarse paso a paso en dos prompts, por ejemplo.

Si necesitas ayuda, una opción de solución de la actividad estará disponible en la sección "Opinión del instructor".



# Lo que aprendimos en esta aula:

    Comprender el problema del negocio y la demanda para la extracción de datos.
    Explorar las bases de datos del proyecto y buscar insights para la creación de visuales.
    Definir qué tareas solicitaremos con el apoyo de la IA de ChatGPT.
    Crear un buen prompt para ChatGPT.
    Pedir sugerencias más precisas de visuales a ChatGPT.

# Con la asistencia de ChatGPT, logramos:

    Explorar brevemente los datos de ventas y el perfil del cliente de Zoop.
    Unir las bases y organizarlas para generar una tabla consolidada para los análisis.
    Investigar los posibles visuales que podemos crear para la narrativa del informe de Zoop.

# Buenas prácticas en la redacción del prompt

Para aprovechar los beneficios de la IA generativa de ChatGPT en la exploración de datos, es muy importante entender cómo crear prompts efectivos que logren los resultados deseados, basándonos en nuestro conocimiento del negocio.

Siguiendo lo que hemos aprendido hasta ahora, ¿cuáles de las opciones a continuación representan buenas prácticas para la redacción de prompts para la generación de visualizaciones de datos en Python?

Incluir información sobre la estructura de los datos y qué variables deseas visualizar.

Esta es una buena práctica en la redacción de un prompt, ya que incluir detalles sobre la estructura de los datos y qué variables deseas visualizar es esencial para crear visualizaciones de datos que destaquen las relaciones y patrones deseados para el usuario.
Alternativa correta

Especificar la biblioteca de visualización de datos que deseas usar (como matplotlib, seaborn o plotly).

Esta es una buena práctica en la redacción de un prompt, ya que diferentes bibliotecas tienen capacidades y sintaxis variadas. Esta descripción orienta a la IA en la generación de la respuesta para la sintaxis y las funcionalidades específicas de estas herramientas, asegurando que las instrucciones y el código generado sean compatibles con las preferencias del usuario y los requisitos técnicos del proyecto.

