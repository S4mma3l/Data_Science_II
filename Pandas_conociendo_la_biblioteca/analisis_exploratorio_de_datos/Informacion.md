### Para saber más: entendiendo el método groupby

El método groupby de Pandas permite agrupar y resumir datos de un DataFrame basado en uno o más criterios. Estos criterios pueden ser variables numéricas o categóricas, como columnas o índices del DataFrame.

La idea detrás de groupby es dividir los datos en grupos basados en los criterios seleccionados y luego aplicar una operación a estos grupos. Esta operación puede ser una función de agregación, como suma, promedio, recuento, desviación estándar, entre otras, o incluso una operación personalizada definida por el usuario.

Este método tiene varios parámetros, algunos de los cuales son:

by: Este es el parámetro más común y se utiliza para especificar la columna o columnas por las cuales queremos agrupar. Como argumento, podemos pasar el nombre de una columna o una lista de nombres de columnas;

axis: Utilizamos este parámetro para especificar el eje a lo largo del cual queremos agrupar. El valor predeterminado es 0, lo que significa que se agruparán las filas. Si deseamos agrupar las columnas, debemos establecer este parámetro en 1;

sort: Este parámetro es un booleano (True o False) que indica si los grupos deben ordenarse por el valor de la columna de agrupación. El valor predeterminado es True;

dropna: Utilizamos este parámetro para controlar si los valores faltantes (NaN) se eliminarán o no durante el proceso de agrupación. El valor predeterminado es True.

Veamos un ejemplo simple utilizando groupby. Supongamos que tenemos el siguiente DataFrame:

Código del DataFrame:
```python
import pandas as pd

df = pd.DataFrame({
   'Animal': ['Perro', 'Gato', 'Elefante', 'Perro', 'Gato', 'Elefante'],
   'Color': ['Negro', 'Blanco', 'Gris', 'Marrón', 'Negro', 'Marrón'],
   'Cantidad': [2, 3, 1, 4, 2, 2]
})
df
```
DataFrame:

4.jpg[](z3yshtyn.png)

Aquí tenemos un DataFrame con datos sobre algunos animales. Usaremos groupby para agrupar los datos por tipo de animal y realizar la suma de la columna "Cantidad" para obtener el total de cada tipo de animal:
```python
df.groupby('Animal').sum(numeric_only=True)
```
Resultado:

5.jpg[](6dl31tk9.png)

También podemos usar el método groupby para agrupar datos por múltiples columnas. Por ejemplo, agrupemos por tipo de animal y también por color, y realicemos la suma de la columna "Cantidad":
```python
df.groupby(['Animal', 'Color'])[['Cantidad']].sum()
```
Resultado:

6.jpg[](e9sdzmw7.png)

Así, podemos observar que groupby es un método muy útil para situaciones en las que necesitamos dividir los datos en grupos para analizar el comportamiento de estos grupos. Utilizando este método, podemos responder preguntas específicas sobre nuestros conjuntos de datos. Si desea aprender más sobre este método, le sugiero dos artículos:

    Pandas GroupBy: Su guía para agrupar datos en Python; https://realpython.com/pandas-groupby/
    Explicación detallada del groupby de Pandas. https://towardsdatascience.com/pandas-groupby-aggregate-transform-filter-c95ba3444bbb

Ambos artículos están en inglés, pero se pueden traducir fácilmente utilizando la extensión de traducción de Google Chrome.

### Realizando selecciones con query

El método query es una herramienta de Pandas que permite seleccionar datos en un DataFrame utilizando las condiciones que especificamos. Utiliza una sintaxis similar a SQL y es útil cuando necesitamos filtrar nuestros datos.

Con base en esto, supongamos que el equipo de aprendizaje automático (ML) ha realizado la siguiente solicitud:

Seleccione solo las propiedades que tienen una o más suites.

¿Cuál de las siguientes opciones presenta la forma correcta de realizar esta selección?
```python
df.query('Suites >= 1')

Excelente! Al pasar la expresión 'Suites >= 1' al método query, especificamos que queremos seleccionar las filas en las que la columna "Suites" tiene un valor mayor o igual a 1.
```

### Métodos de la biblioteca Pandas

La biblioteca Pandas tiene diferentes métodos que nos ayudan a analizar y explorar nuestros datos. Utilizando estos métodos, podemos agrupar datos, realizar selecciones, contar el número de valores únicos, entre otras cosas.

Supongamos que necesitamos contar cuántas veces aparece cada barrio en nuestra base de datos. ¿Qué método podríamos utilizar para hacerlo?
```python
df['Barrio'].value_counts()

El método value_counts() de Pandas se utiliza para devolver una serie que contiene recuentos de valores únicos en una columna u objeto Series de Pandas.
```

### Para saber más: alterando los nombres de las columnas

Cuando trabajamos con bases de datos, en ocasiones puede ser necesario cambiar los nombres de las columnas. Por ejemplo, cuando creamos el siguiente DataFrame en nuestro proyecto:
```python
df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')
```
Obtuvimos el siguiente resultado:

7.jpg[](cjf4a84v.png)

Podemos ver que la columna con los porcentajes está nombrada como "Tipo". ¿Y si quisiéramos cambiar su nombre a "Porcentajes"?

En ese caso, podemos utilizar el método rename() para cambiar el nombre de esa columna. Este método nos permite especificar un diccionario que asocia el nombre antiguo de la columna con el nuevo nombre que deseamos asignar. Entonces, hagámoslo:
```python
# Guardando el DataFrame en una variable
df_ejemplo = df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')

# Cambiando el nombre de la columna "Tipo" a "Porcentajes"
df_ejemplo.rename(columns={'Tipo': 'Porcentajes'}, inplace=True)

# Visualizando el DataFrame
df_ejemplo
```
Hemos utilizado el parámetro inplace=True para que este cambio se aplique definitivamente en nuestro DataFrame df_ejemplo. Entonces, al visualizar el DataFrame, obtendremos el siguiente resultado:

8.jpg[](u8yy6969.png)

¡Y listo! Ahora también sabemos cómo cambiar nombres de columnas en un DataFrame.

# Lo que aprendimos en esta aula:

    Identificar qué hacer durante un proceso de análisis exploratorio;
    Calcular el promedio de valores de un DataFrame;
    Agrupar los datos según una columna específica utilizando groupby;
    Realizar selecciones utilizando el método query;
    Transformar Series en DataFrames;
    Ordenar valores de un DataFrame con sort_values;
    Graficar barras verticales y horizontales;
    Visualizar valores únicos con unique;
    Utilizar value_counts para contar valores únicos y calcular porcentajes;
    Cambiar nombres de columnas.

