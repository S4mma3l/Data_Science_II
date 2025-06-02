## Para saber más: lidiando con datos nulos

Tratar datos nulos en una base de datos es muy importante porque estos datos faltantes pueden interferir directamente en la calidad de los análisis y los resultados obtenidos. Cuando hay datos nulos en un conjunto de datos, pueden surgir problemas como sesgo, reducción de la precisión y falta de precisión en la información obtenida.

Además, algunos análisis y modelos estadísticos no pueden manejar la presencia de datos faltantes. Por lo tanto, el tratamiento de los datos nulos es fundamental para garantizar la confiabilidad y la precisión de los análisis y decisiones basadas en estos datos.

Existen varias formas de tratar datos nulos con Pandas. Algunas de las formas principales son:

Eliminar los datos nulos: Es posible eliminar las filas o columnas que contienen valores nulos utilizando el método dropna(). Este método elimina todas las filas o columnas que tienen al menos un valor nulo.

Llenar los datos nulos: Utilizando el método fillna(), podemos llenar los valores nulos con un valor específico. Además, también es posible utilizar argumentos específicos del método fillna(), como method="ffill" o method="bfill", para llenar los valores nulos con el valor anterior o posterior, respectivamente.

Interpolar los datos nulos: Es posible utilizar el método interpolate() para llenar los valores nulos con valores interpolados, es decir, valores calculados a partir de los valores vecinos.

Es importante elegir la mejor forma de tratar los datos nulos según la situación específica y el objetivo del análisis de datos.

### Método drop()

El método drop() de la biblioteca Pandas permite eliminar una o más filas y/o columnas de un DataFrame. Esta eliminación se puede realizar de forma permanente en el DataFrame original. Es posible especificar los índices de las filas y/o columnas que se deben eliminar, así como el eje en el que debe ocurrir la eliminación.

Suponga que tenemos el siguiente DataFrame, guardado en una variable llamada "datos":

Código para crear el DataFrame:

import pandas as pd

datos = pd.DataFrame([['Plaza', 'Cebolla', 2.5], 
                      ['Mercado', 'Cebolla', 1.99], 
                      ['Supermercado', 'Cebolla', 1.69], 
                      ['Plaza', 'Tomate', 4], 
                      ['Mercado', 'Tomate', 3.29], 
                      ['Supermercado', 'Tomate', 2.99], 
                      ['Plaza', 'Papa', 4.2], 
                      ['Mercado', 'Papa', 3.99], 
                      ['Supermercado', 'Papa', 3.69]],
                      columns = ['Comercio', 'Producto', 'Precio'])

DataFrame:

9.img[](p0oae5yk.png)

¿Cuál de los siguientes códigos se podría utilizar para eliminar de forma permanente las filas en las que, en la columna "Comercio", tenemos "Supermercado"?

[](Metodo_drop.py)

### Realizando selecciones

El equipo de Machine Learning solicitó realizar otro filtro en nuestra base de datos. Esta vez, el filtro sería para obtener la siguiente información:

¿Cuáles son los apartamentos que tienen un área mayor de 80 m² o un alquiler menor de MXN 4.000,00?

Con base en esto, ¿cuál de las siguientes opciones presenta un código que se puede utilizar para obtener la información solicitada?
```python
seleccion = (df['Area'] > 80) | (df['Valor'] < 4000)
df[seleccion]
```

Muy bien, de esta manera, estamos realizando el filtro exactamente como lo solicitó el equipo de Machine Learning.

###  Para saber más: exportando diferentes formatos

Pandas proporciona varios métodos para guardar archivos en diferentes formatos. Algunos ejemplos son:

to_csv(): Guarda el DataFrame en un archivo CSV (Valores Separados por Comas).

to_excel(): Guarda el DataFrame en un archivo de Excel.

to_json(): Guarda el DataFrame en un archivo JSON (Notación de Objetos JavaScript).

Estos son solo algunos ejemplos, existen otros métodos disponibles en Pandas para guardar archivos en diferentes formatos. Si deseas conocerlos, consulta la documentación: https://pandas.pydata.org/docs/user_guide/io.html#io-tools-text-csv-hdf5

### Lo que aprendimos en esta aula:

    Verificar si una base de datos tiene datos nulos;
    Tratar los datos nulos;
    Eliminar filas y columnas de un DataFrame;
    Realizar diferentes selecciones en una base de datos;
    Guardar datos en formato csv;
    Utilizar el método replace para reemplazar valores en una base de datos.

