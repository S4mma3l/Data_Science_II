### Datos JSON en un DataFrame

A Gustavo se le asignó la tarea de analizar un archivo JSON que contiene información sobre las ventas de una tienda online.

El archivo "ventas.json" contiene información sobre las ventas realizadas por la tienda en los últimos tres meses. Él necesita cargar esta información en un DataFrame de la biblioteca Pandas para poder analizarla.

¿Qué comando se debe utilizar para leer el archivo JSON "ventas.json" con la biblioteca Pandas?
```python
pd.read_json('ventas.json')
```
¡Es eso mismo! La función read_json permite cargar un archivo JSON directamente en un DataFrame de la biblioteca Pandas.


### Para saber más: profundizando en la normalización

La normalización de datos es un proceso importante en la ciencia de datos que tiene como objetivo organizar y estandarizar datos para facilitar el análisis y la comparación entre ellos. Cuando se trata de datos en formato JSON (JavaScript Object Notation - Notación de objetos JavaScript), es común que estén anidados, lo que puede dificultar su análisis y manipulación.

La biblioteca Pandas cuenta con una función llamada json_normalize() que permite la transformación de datos a formato tabular, facilitando la visualización y análisis de las informaciones. A continuación, aprenderemos cómo usar esta función para normalizar diferentes tipos de JSON en DataFrames.

Normalizando un JSON simple

A continuación tenemos una variable llamada datos y dentro de ella hay un objeto JSON con tres llaves y sus respectivos valores:
```python
datos = {'Análisis': 'Principales indicadores de enfermedad cardíaca', 'Año': 2020, 'Numero_Pacientes':3}
```
Para normalizar esta variable, podemos pasarla dentro de la función json_normalize y analizar el DataFrame obtenido:
```python
df = pd.json_normalize(datos)
df
```
index	Análisis	Año	Numero_Pacientes
0	Principales indicadores de enfermedad cardíaca	2020	3

¡El resultado luce genial! Tenemos 3 columnas que son nuestras llaves y una fila que contiene los valores de cada llave.

Normalizando un JSON con múltiples niveles

Hay situaciones en las que el archivo JSON puede contener más de un objeto, como es el caso del siguiente ejemplo, en el que tenemos una lista, almacenada en la variable json_lista, que contiene dos objetos JSON:
```python
json_lista = [
    { 'ID': '01', 'Intervalo_edad': '55-59', 'Sexo_biologico': 'femenino'},
    { 'ID': '02', 'Intervalo_edad': '80 ó +', 'Sexo_biologico': 'femenino'}
]
```
Para normalizar esta lista podemos aplicar la función json_normalize:
```python
pd.json_normalize(json_lista)
```
index	ID	Intervalo_edad	Sexo_biologico
0	01	55-59	femenino
1	02	80 ó +	femenino

La función json_normalize() es capaz de convertir cada registro de la lista en una línea en forma tabular.

Normalizando un JSON con una lista anidada

Bueno, notamos que la función json_normalize() funciona muy bien en las situaciones anteriores, pero ¿qué pasa en otras situaciones?

Datos como un diccionario

Iniciemos observando la normalización cuando los datos son un diccionario. Tenemos un diccionario almacenado en la variable json_obj. Observe que en la llave “Salud” tenemos otro diccionario:
```python
json_obj = {
    'ID': '01',
    'Intervalo_edad': '55-59',
    'Sexo_biologico': 'Femenino',
    'Salud': {'Dificultad_caminar': 'No',
              'Actividad_fisica': 'Sí',
              'IMC': 16.6,
              'Enfermedad_cardiaca': 'No',
          }
      }
```
Haciendo la normalización:
```python
pd.json_normalize(json_obj)
```
index	ID	Intervalo_edad	Sexo_biologico	Salud.Dificultad_caminar	Salud.Actividad_fisica	Salud.IMC	Salud.Enfermedad_cardiaca
0	01	55-59	Femenino	No	Sí	16.6	No

El DataFrame generado tiene una columna para cada información contenida en el diccionario que estaba en “Salud”. Las columnas creadas tienen el prefijo “Salud.”, ya que la información proviene de esa misma llave.

Datos como una lista de diccionarios.

Ahora tenemos una lista de diccionarios almacenados en la variable json_list:
```python
json_list = [
    {
    'ID': '01',
    'Intervalo_edad': '55-59',
    'Sexo_biologico': 'Femenino',
    'Salud': {'Dificultad_caminar': 'No',
              'Actividad_fisica': 'Sí',
              'IMC': 16.6,
              'Enfermedad_cardiaca': 'No',
          }
      },
      {
          'ID': '02',
          'Intervalo_edad': '80 ó +',
          'Sexo_biologico': 'Femenino',
          'Salud': {'Dificultad_caminar': 'No',
                    'Actividad_fisica': 'Sí',
                    'IMC': 20.34,
                    'Enfermedad_cardiaca': 'Sí'}
       }
       ]
```
Haciendo la normalización:
```python
pd.json_normalize(json_list)
```
index	ID	Intervalo_edad	Sexo_biologico	Salud.Dificultad_caminar	Salud.Actividad_fisica	Salud.IMC	Salud.Enfermedad_cardiaca
0	01	55-59	Femenino	No	Sí	16.6	No
1	02	80 ó más	Femenino	No	Sí	20.34	Sí

Podemos ver que todos los valores anidados dentro de cada registro de la lista se han convertido en columnas separadas. ¿Qué pasa con los datos que normalizamos en el video anterior? ¿Recuerdas cómo su normalización se hizo de otra manera?

Resumiendo, vamos a copiar los datos del archivo paciente_2.json y vamos a guardarlos en una variable llamada datos_dict.
```python
datos_dict = {
  "Investigación": "Indicadores clave de enfermedades cardíacas",
  "Año": 2020,
  "Pacientes": [
    {
     "ID": "01",
      "Rango_edad": "55-59",
      "Sexo_biologico": "Mujer",
      "Raza": "Blanca",
      "IMC": 16.6,
      "Fumador": "Sí",
      "Consumo_alcohol": "No",
      "Salud_física": 3,
      "Salud_mental": 30,
      "Dificultad_caminar": "No",
      "Actividad_física": "Sí",
      "Salud_general": "Muy buena",
      "Horas_sueño": 5,
      "Problemas_salud": [
        "Diabetes",
        "Asma",
        "Cancer_piel"
      ]
    },
    {
      "ID": "02",
      "Rango_edad": "80 ó +",
      "Sexo_biologico": "Mujer",
      "Raza": "Blanca",
      "IMC": 20.34,
      "Fumador": "No",
      "Consumo_alcohol": "No",
      "Salud_física": 0,
      "Salud_mental": 0,
      "Dificultad_caminar": "No",
      "Actividad_física": "Sí",
      "Salud_general": "Muy buena",
      "Horas_sueño": 7,
      "Problemas_salud": [
        "AVC"
      ]
    },
    {
      "ID": "03",
      "Rango_edad": "65-69",
      "Sexo_biologico": "Masculino",
      "Raza": "Blanca",
      "IMC": 26.58,
      "Fumador": "Sí",
      "Consumo_alcohol": "No",
      "Salud_física": 20,
      "Salud_mental": 30,
      "Dificultad_caminar": "No",
      "Actividad_física": "Sí",
      "Salud_general": "Muy buena",
      "Horas_sueño": 8,
      "Problemas_salud": [
        "Diabetes",
        "Asma"
      ]
    }
  ]
}
```
Si intentamos normalizar estos datos:
```python
pd.json_normalize(datos_dict)
```
index	Investigación	Año	Pacientes
0	Indicadores clave de enfermedades cardíacas	2020	{'ID':'01','Rango_edad': '55-59', 'Sexo_b…

Podemos observar que nuestra lista anidada está colocada en una única columna Pacientes. Entonces, usaremos el siguiente código para normalizar los datos, especificando qué columna está anidada:
```python
pd.json_normalize(datos_dict['Pacientes'])
```
También podemos hacer esto usando el parámetro record_path como ['Pacientes']. Este parámetro se utiliza en la función pd.json_normalize() para especificar la ruta a los registros que deben ser normalizados en un DataFrame separado:
```python
pd.json_normalize(datos_dict, record_path=['Pacientes'])
```
Con ambos códigos el resultado es el mismo.
index	ID	Rango_edad	Sexo_biologico	Raza	...	Actividad_fisica	Salud_general	Horas_sueño	Problemas_salud
0	01	55-59	Mujer	Blanca	...	Sí	Muy buena	5	Diabetes,Asma,Cancer_piel
1	02	80 ó +	Mujer	Blanca	...	Sí	Muy buena	7	AVC
2	03	65-69	Masculino	Blanca	...	Sí	Muy buena	8	Diabetes,Asma

El resultado parece excelente, pero no incluye las columnas "Investigación" y "Año". Para incluirlas, podemos usar el parámetro meta para especificar otras columnas que queramos en el DataFrame.
```python
pd.json_normalize(
    datos_dict, 
    record_path =['Pacientes'], 
    meta=[‘Investigación’, 'Año']
)
```
index	ID	Rango_edad	Sexo_biologico	Raza	...	Actividad_fisica	Salud_general	Horas_sueño	Problemas_salud	Investigación	Año
0	01	55-59	Mujer	Blanca	...	Sí	Muy buena	5	Diabetes,Asma,Cancer_piel	Indicadores clave de enfermedades cardíacas	2020
1	02	80 ó +	Mujer	Blanca	...	Sí	Muy buena	7	AVC	Indicadores clave de enfermedades cardíacas	2020
2	03	65-69	Masculino	Blanca	...	Sí	Muy buena	8	Diabetes,Asma	Indicadores clave de enfermedades cardíacas	2020

¡De esa manera tenemos todas las columnas presentes en el DataFrame!

    Importante: En clase nosotros realizamos la normalización en un archivo con formato JSON. Sin embargo, la función json_normalize() sólo acepta un diccionario o una lista de diccionarios. Por esto, en el video se utilizó la estrategia de usar el código: pd.json_normalize(datos_pacientes_2['Pacientes']). Sin embargo, si intentamos utilizar parámetros de la función json_normalize en un archivo JSON, pueden surgir errores. Para solucionar esto, necesitamos importar el módulo json y leer los archivos según el siguiente código:
```python
#Importando la biblioteca Pandas
import pandas as pd

#Importando el módulo JSON
import json

#Leyendo el archivo json usando el módulo Python JSON
with open('pacientes_2.json','r') as f:
    datos = json.loads(f.read())

#Normalizando los datos con los parámetros record_path y meta
pd.json_normalize(datos, record_path='Pacientes', meta=['Investigación', 'Año'])
```
Y fue así que aprendimos cómo normalizar archivos JSON simples, con múltiples niveles y anidados.

### Para saber más: obteniendo archivos JSON de APIs

Para obtener datos en formato JSON podemos utilizar una API (Application Programming Interface). Es una interfaz de programación de aplicaciones que permite la comunicación entre diferentes programas o sistemas.

Hay varios formatos que se pueden utilizar en las API y uno de los más comunes es JSON (JavaScript Object Notation). JSON es un formato ligero para intercambiar información entre sistemas que utiliza la notación basada en objetos de JavaScript.

Tenemos la siguiente situación-problema:

“Una empresa de alimentos saludables tiene problemas con la popularidad de sus productos. A pesar de ofrecer opciones saludables, muchos clientes se muestran reacios a comprar los productos debido a la falta de información sobre los valores nutricionales de las frutas que se utilizan en la producción de alimentos”.

Ante esta situación podemos acceder a una API llamada Fruitvice para recopilar información detallada sobre los valores nutricionales de las frutas que se utilizan en los productos. Con esta información, la empresa podrá actualizar sus empaques y materiales de marketing para resaltar los valores nutricionales de las frutas y así atraer más clientes que buscan opciones saludables. Además, la empresa puede utilizar la información para desarrollar nuevos productos que satisfagan aún más las necesidades nutricionales de su clientela.

Una forma común de acceder a las API es a través de la biblioteca requests. Para eso, también es necesario importar el módulo json:
```python
import requests
import json
```
Los datos de API Fruitvice se obtendrán con la función request.get('url'). Dentro de ella pasamos la dirección API seguida de api/fruit/all para obtener los datos de todas las frutas.
```python
datos_frutas = requests.get('https://fruityvice.com/api/fruit/all')
```
Conseguimos recuperar los resultados utilizando la función json.loads(). Para ello es necesario pasar la variable datos_frutas, previamente creada con el atributo text que devuelve el contenido de la respuesta.
```python
resultado = json.loads(datos_frutas.text)
```
Luego podemos obtener una vista previa del DataFrame.
```python
pd.DataFrame(resultado)
```
index	genus	name	id	family	order	nutritions
0	Malus	Apple	6	Rosaceae	Rosales	{'carbohydrates': 11.4, 'protein': 0.3, 'fat': 0.4, 'calories': 52, 'sugar': 10.3}
1	Prunus	Apricot	35	Rosaceae	Rosales	{'carbohydrates': 3.9, 'protein': 0.5, 'fat': 0.1, 'calories': 15, 'sugar': 3.2}
2	Persea	Avocado	84	Lauraceae	Laurales	{'carbohydrates': 8.53, 'protein': 2, 'fat': 14.66, 'calories': 160, 'sugar': 0.66}
3	Musa	Banana	1	Musaceae	Zingiberales	{'carbohydrates': 22, 'protein': 1, 'fat': 0.2, 'calories': 96, 'sugar': 17.2}
4	Rubus	Blackberry 64	Rosaceae	Rosales	{'carbohydrates': 9, 'protein': 1.3, 'fat': 0.4, 'calories': 40, 'sugar': 4.5}	
5	Fragaria	Blueberry	33	Rosaceae	Rosales	{'carbohydrates': 5.5, 'protein': 0, 'fat': 0.4, 'calories': 29, 'sugar': 5.4}
6	Prunus	Cherry	9	Rosaceae	Rosales	{'carbohydrates': 12, 'protein': 1, 'fat': 0.3, 'calories': 50, 'sugar': 8}

¡Ahora sabemos cómo utilizar la biblioteca requests y el módulo JSON para obtener datos de las API!


# En esta aula, aprendimos a:

    Comprender qué es el formato JSON;
    Leer un archivo en formato JSON;
    Normalizar datos de un archivo JSON;
    Escribir un archivo en formato JSON;
    Obtener archivos JSON de las API.

