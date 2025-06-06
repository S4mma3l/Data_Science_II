# Para saber más: bases de datos y SQLAlchemy



Las bases de datos son sistemas que permiten el almacenamiento, organización y recuperación de información de forma estructurada y eficiente. Se utilizan ampliamente en muchas áreas, desde la gestión empresarial hasta la investigación científica. Una base de datos bien diseñada puede mejorar significativamente la eficiencia y precisión de las operaciones de una organización.

Existen bases de datos relacionales y no relacionales. Las bases de datos relacionales representan y almacenan datos en tablas. Las bases de datos no relacionales, también conocidas como bases de datos NoSQL (Not Only SQL - No Sólo SQL), utilizan una variedad de estructuras de datos, como documentos, gráfos o pares llave-valor.

Python ofrece varios paquetes y bibliotecas para trabajar con bases de datos, incluyendo SQLite, MySQL, PostgreSQL, Oracle, MongoDB, entre otros. Uno de los paquetes más comunes utilizados para trabajar con bases de datos relacionales en Python es el paquete sqlite3 que ofrece soporte a bases de datos SQLite. Esta base de datos es liviana e integrada, no requiere un servidor separado para ejecutarse y está instalada de forma nativa en Google Colab.

Para trabajar con esta base de datos, podemos usar SQLAlchemy, una biblioteca de mapeo objeto-relacional (ORM), que permite interactuar con bases de datos relacionales usando código Python. Proporciona una capa de abstracción que permite a los desarrolladores trabajar con objetos Python en lugar de lidiar directamente con las complejidades del lenguaje SQL (Structured Query Language - Lenguaje de consulta estructurado).

Uno de los principales beneficios de utilizar SQLAchemy es la capacidad de crear código más legible y fácil de mantener. Con SQLAlchemy, las operaciones de la base de datos se realizan utilizando métodos en objetos Python, lo que hace que el código sea más claro y menos propenso a errores.

Además, SQLAlchemy ofrece soporte a consultas complejas en bases de datos, lo que permite a los desarrolladores extraer fácilmente información relevante de grandes conjuntos de datos. Esto es especialmente útil en aplicaciones que necesitan manejar grandes cantidades de datos.

Puede encontrar más detalles sobre la biblioteca SQLAchemy en la siguiente documentación. https://www.sqlalchemy.org/

# Para saber más: cláusulas SQL

SQL (Structured Query Language - Lenguaje de consulta estructurado) es un lenguaje de consulta utilizado en bases de datos relacionales para insertar, actualizar, consultar y administrar datos.

Para hacer todo esto, existen cláusulas SQL, que son componentes fundamentales de las sentencias SQL, permitiendo especificar detalles sobre cómo se va a realizar la consulta u operación de la base de datos. Las cláusulas se utilizan para filtrar, ordenar, agrupar y limitar los resultados de la consulta.

Las sentencias SQL pueden estar compuestas por una o más cláusulas que proporcionan información adicional sobre lo que se supone que debe hacer la consulta. Las cláusulas más comunes son:

    SELECT: especifica qué columnas deben seleccionarse en la consulta.
    FROM: Especifica las tablas de la base de datos que se consultarán.
    WHERE: Filtra los resultados de la consulta según una o más condiciones especificadas.
    ORDER BY: Ordena los resultados de la consulta en orden ascendente o descendente según una o más columnas.
    GROUP BY: agrupa los resultados de la consulta basados en una o más columnas.
    LIMIT: limita el número de filas devueltas por los resultados de la consulta.
    Tenemos un ejemplo sencillo de sintaxis SQL que utiliza el comando SELECT para consultar datos de una tabla de empleados en una base de datos:
```sql
SELECT nombre, apellido, salario
FROM empleados
WHERE departamento = 'ventas'
```
En esta declaración SQL, la cláusula SELECT se utiliza para especificar las columnas que desea consultar de la tabla "empleados", incluyendo "nombre", "apellido" y "salario". La cláusula FROM se utiliza para especificar la tabla que se desea consultar, que en este caso es "empleados".

La cláusula WHERE se utiliza para filtrar los resultados de la consulta según una condición específica. En este ejemplo, la condición es departamento = 'ventas', lo que significa que la consulta solo devolverá empleados que trabajan en el departamento de ventas.

En el próximo vídeo aprenderemos a utilizar algunas de estas cláusulas para realizar las primeras consultas SQL en la tabla que contiene datos de clientes de una institución financiera.

# read_sql y read_sql_table

Un equipo de análisis de datos está trabajando para extraer información de una tabla en una base de datos SQL. Decidieron utilizar la biblioteca Pandas para acceder a los datos. Para ello utilizaron las funciones read_sql y read_sql_table.

¿Cuál es la alternativa correcta sobre estas funciones?

Ambas funciones devuelven un objeto DataFrame.

¡Eso es! Ambas funciones devuelven un DataFrame.

# Lo que aprendimos

    Crear una base de datos local;
    Escribir en una base de datos;
    Realizar lectura en una consulta SQL;
    Actualizar una base de datos.