# Interpretando Tablas de Frecuencia

Dada la siguiente tabla de frecuencia para la variable Sexo en un conjunto de datos:
Sexo	Frecuencia	Porcentaje (%)
Masculino	53250	69.3
Femenino	23590	30.7

¿Cuál de las siguientes afirmaciones es CORRECTA?

El número total de individuos en la muestra es 76840.

El número total de individuos es la suma de las frecuencias de hombres y mujeres (53250 + 23590 = 76840).

# Para saber más: análisis Bivariado con pd.crosstab

En el mundo del análisis de datos, a menudo es necesario explorar la relación entre dos variables categóricas. El código que hemos visto utiliza la función pd.crosstab de Pandas para crear una tabla de contingencia, que nos permite examinar cómo se distribuyen los valores de una variable (Ingreso en este caso) en función de las combinaciones de otras dos variables categóricas (Sexo y Color).

Veamos en detalle cómo funciona este código:
```python
porcentaje = pd.crosstab(datos.Sexo,
                         datos.Color,
                         aggfunc = 'mean',
                         values = datos.Ingreso)
porcentaje.rename(index = sexo,inplace = True)
porcentaje.rename(columns = color,inplace = True)
porcentaje
```
Explicación paso a paso:

    1. pd.crosstab(datos.Sexo, datos.Color...): Esta es la función principal que crea la tabla de contingencia.
    2. Los dos primeros argumentos (datos.Sexo y datos.Color) especifican las dos variables categóricas que se cruzarán.
    3. ```python aggfunc = 'mean':``` Indica que queremos calcular la media de datos.Ingreso para cada combinación de Sexo y Color. Podríamos usar otras funciones de agregación como sum, count, etc., dependiendo del análisis que queramos realizar.
    4. values = datos.Ingreso: Especifica la variable numérica cuyos valores se agregarán en cada celda de la tabla.
    5. porcentaje.rename(index = sexo, inplace = True): Esta línea renombra las etiquetas del índice (filas) de la tabla de contingencia utilizando los valores del diccionario sexo. El argumento inplace = True modifica la tabla directamente en lugar de crear una nueva.
    6. porcentaje.rename(columns = color, inplace = True): De manera similar, esta línea renombra las etiquetas de las columnas de la tabla utilizando los valores del diccionario color.
    7. porcentaje: Finalmente, se muestra la tabla resultante.

¿Qué nos muestra esta tabla?

La tabla resultante nos mostrará la media de Ingreso para cada combinación de Sexo y Color. Esto nos permite comparar, por ejemplo, si hay diferencias significativas en los ingresos promedio entre hombres y mujeres de diferentes etnias.

Te animo a experimentar con diferentes funciones de agregación y variables en pd.crosstab para descubrir patrones interesantes en tus datos. ¡El análisis bivariado es una herramienta poderosa para comprender mejor las relaciones entre variables en tus conjuntos de datos! ;))

# Lo que aprendimos en esta aula:

    Crear distribuciones de frecuencia (tablas de frecuencia) con la función value_counts () de pandas.
    Creación de distribuciones de frecuencia, cruzando dos variables, utilizando la función crosstab () de pandas.
    Creación de distribuciones de frecuencia, con clases personalizadas, utilizando las funciones value_counts () y cut () juntas.
    Utilizar la regla de Sturges para obtener un número óptimo de clases para un tamaño de muestra dado.
    Graficar el histograma, que es la representación gráfica de una distribución de frecuencias.

