# Para saber más: ¿Qué es HTML?



HTML (Hypertext Markup Language - Lenguaje de marcación de hipertexto) es el código que utilizamos para estructurar una página web y su contenido. HTML consta de una serie de elementos que se utilizan para delimitar o agrupar diferentes contenidos para que aparezca o actúe de una determinada manera.

Un documento HTML comienza con la etiqueta <html> y termina con la etiqueta </html>. También contiene un encabezado (<head>) que describe el título de la página y otras informaciones relevantes; y un cuerpo (<body>) que contiene el contenido de la página. El encabezado y el cuerpo están delimitados por las etiquetas <head> y </head>, y <body> y </body>, respectivamente.

Dentro del cuerpo podemos utilizar diversos elementos para crear la estructura del contenido. Observe cada detalle en el siguiente ejemplo:
```html
    tags <h1> a <h6>: crear títulos y subtítulos.
    tags <p>: crear párrafos.
    tags <ul> y <li>: crear listas no ordenadas.
    tags <img>: insertar imágenes.
    tags <table>, <tr>, <th> y <td>: crear tablas.
```
Además, podemos usar atributos en elementos HTML para especificar propiedades adicionales. Por ejemplo: podemos usar el atributo src en la etiqueta <img> para indicar la dirección de la imagen que queremos mostrar, o el atributo href en la etiqueta <a> para indicar la dirección del link que queremos crear.

##  Leyendo una tabla específica

Karina está trabajando en un proyecto de análisis de datos y necesita extraer una tabla que está en un archivo HTML. Para ello, decide utilizar la biblioteca Pandas que tiene una función llamada read_html y devuelve una lista de DataFrames de un archivo HTML.

¿Cuál de las siguientes alternativas utiliza correctamente esta función para mostrar la primera tabla contenida en el archivo?
```python
df = pd.read_html('archivo.html')[0]
```
Aquí obtenemos el primer elemento de la lista que devuelve la función read_html asignado a la variable df que corresponde a la primera tabla encontrada en el archivo HTML.

# Para saber mas: Que es xml?

XML es un lenguaje de marcación que permite crear y describir datos de forma estructurada y estandarizada. Está compuesto por líneas de comando que utilizan tags (etiquetas) para definir elementos y atributos de los datos.

La estructura básica de un documento XML está formada por:

    Una declaración inicial que indica la versión, el encoding y el tipo del documento.
    Un elemento raíz que contiene todos los demás elementos del documento.
    Elementos secundarios que pueden tener otros elementos o contenido de texto dentro de ellos.
    Atributos que proporcionan información adicional sobre los elementos.

Un ejemplo sencillo de un documento XML es:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<animales>
  <animal nombre="Mel" tipo="perro" color="marron"/>
  <animal nombre="Vick" tipo="gato" color="blanco"/>
</animales>
```
En este ejemplo, <animales> es el elemento raíz, <animal> es un elemento secundario con tres atributos (nombre, tipo y color) y Mely Vick son el contenido de texto de los elementos.

Podemos encontrar más información sobre la estructura XML en la página: XML para principiantes - Soporte de Microsoft.

# Entendiendo la estructura XML

Gabriel está analizando datos de una tienda online de productos electrónicos. Recibió un archivo XML que contiene informaciones sobre los productos de la tienda, como: nombre, precio y categoría.

<productos>
  <producto id="1">
    <nombre>Smartphone</nombre>
    <precio>4500.00</precio>
    <categoria>Celulares</categoria>
  </producto>
  <producto id="2">
    <nombre>Notebook</nombre>
    <precio>5000.00</precio>
    <categoria>Computadores</categoria>
  </producto>
  <producto id="3">
    <nombre>Tablet</nombre>
    <precio>2000.00</precio>
    <categoria>Celulares</categoria>
  </producto>
</productos>

Analice el archivo XML anterior y elija la alternativa correcta.

 El archivo XML se compone de un elemento raíz con nombre <productos> y tres elementos secundarios llamados <producto>, cada uno con un atributo id.

La alternativa describe correctamente la estructura del archivo XML. Hay un elemento raíz <productos> que contiene todos los demás elementos del documento. Los elementos secundarios <producto> tienen el atributo id.

### En esta aula, aprendimos a:

    Inspeccionar una página web;
    Leer datos de una página web;
    Escribir archivos HTML;
    Comprender cómo está estructurado el formato XML;
    Leer datos en formato XML;
    Escribir archivos en formato XML.

