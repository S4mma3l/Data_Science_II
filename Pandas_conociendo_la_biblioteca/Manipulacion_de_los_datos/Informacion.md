Supongamos que tenemos el siguiente DataFrame con información sobre algunos autos en venta:

Código para crear el DataFrame:
``` python
import pandas as pd

datos = {
    'Nombre': ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Escarabajo'], 
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
    'Modelo': [2019, 2003, 1991, 2019, 1990],
    'Kilometraje': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0],
    'Impuesto': [2000.0, 5000.0, 1700.0, 2200.0, 1000.0],
    'Descuento': [380.0, 450.0, 277.0, 400.0, 150.0]
}

df = pd.DataFrame(datos)
```
DataFrame:

10.jpg [](2l9ltbf3.png)

Necesitamos crear una columna llamada "Valor_total" que tenga el valor del automóvil, sumado al impuesto y menos el valor del descuento. ¿Cuál de las siguientes opciones presenta el código correcto para crear esta columna?
``` python
df['Valor_total'] = df['Valor'] + df['Impuesto'] - df['Descuento']
```

De esta manera, estamos creando correctamente una nueva columna a partir de operaciones entre las columnas "Valor", "Impuesto" y "Descuento", según se solicitó.

### Para saber mas: creando columnas

¡Claro! Con gusto te explico las diferentes formas de crear columnas en un DataFrame de Pandas en español.
Creación de Columnas en Pandas

Pandas ofrece varias maneras flexibles de añadir nuevas columnas a tus DataFrames, lo que te permite manipular y enriquecer tus datos de forma efectiva. Aquí te presento las principales:
1. Asignación Directa de Valores a una Nueva Columna

Esta es la forma más sencilla cuando ya tienes una lista o una Serie de valores que quieres asignar a la nueva columna. La longitud de tu lista o Serie debe coincidir con el número de filas de tu DataFrame.
```Python

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = [7, 8, 9] # Aquí se asigna directamente una lista como nueva columna 'C'
print(df)

Resultado:

   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
```
2. Creación de una Columna a Partir de Operaciones entre Otras Columnas

Este es un método muy común y potente para derivar nuevas columnas realizando cálculos con los datos de columnas existentes. Pandas alinea automáticamente las operaciones por índice, lo que lo hace muy eficiente.
```Python

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df['A'] + df['B'] # 'C' se crea sumando los valores de 'A' y 'B'
print(df)

Resultado:

   A  B  C
0  1  4  5
1  2  5  7
2  3  6  9
```
3. Uso del Método assign() para Crear Nuevas Columnas

El método assign() es particularmente útil cuando deseas mantener tu código encadenado (es decir, realizar varias operaciones en una sola línea de código sin modificar el DataFrame original en cada paso intermedio). assign() siempre devuelve una nueva copia del DataFrame con las columnas añadidas, dejando el DataFrame original intacto.

```python

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df = df.assign(C=[7, 8, 9]) # Se crea 'C' asignando directamente una lista
# También puedes crear columnas basadas en otras, por ejemplo:
# df = df.assign(C=df['A'] * 2, D=df['A'] + df['B'])
print(df)

Resultado:

   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
```
4. Uso del Método apply() para Aplicar una Función

Cuando necesitas realizar una operación más compleja que no es una simple suma o resta entre columnas, o si quieres aplicar una función personalizada fila por fila (o elemento por elemento), el método apply() es tu mejor aliado. A menudo se usa con funciones lambda para operaciones rápidas y en línea.
```Python

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df['A'].apply(lambda x: x * 2) # 'C' se crea aplicando una función lambda a cada valor de 'A'
print(df)

Resultado:

   A  B  C
0  1  4  2
1  2  5  4
2  3  6  6
```
Cada uno de estos métodos tiene su propio escenario óptimo de uso, dependiendo de la complejidad de la lógica para crear la nueva columna y de cómo prefieras estructurar tu código. link: https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html#how-to-create-new-columns-derived-from-existing-columns

### Lo que aprendimos en esta aula:

    Generar columnas numéricas;
    Insertar columnas categóricas;
    Definir columnas binarias;
    Realizar operaciones entre columnas;
    Utilizar el método apply;
    Crear funciones lambda.

