# Visualizando datos con gráficos interactivos

 Ricardo es un científico de datos que está analizando la variación de la temperatura a lo largo del tiempo en una región específica. Su tarea es crear un gráfico interactivo que muestre la evolución de la temperatura en los últimos años. Para ello, ha decidido utilizar la biblioteca Plotly y crear un gráfico con interactividad.

¿Cuál de las siguientes alternativas presenta la manera correcta de crear un gráfico de líneas interactivo y personalizarlo con la biblioteca Plotly?

Utilizar la función plotly.express.line() para crear el gráfico y luego personalizar el diseño utilizando la función fig.update_layout().

Para crear un gráfico de líneas interactivo con la biblioteca Plotly Express, es necesario utilizar la función plotly.express.line(). Además, es posible personalizar el diseño del gráfico utilizando la función fig.update_layout(), que nos permite definir parámetros como la anchura y altura del gráfico, el ángulo de las etiquetas del eje X, el título de los ejes X e Y, etc.

# Para saber más: animación de gráficos para mostrar cambios durante un lapso

Aprendimos a crear gráficos interactivos con la biblioteca Plotly, pero ¿sabías que es posible ir más allá y crear animaciones con esa misma biblioteca? Además de hacer nuestros gráficos más interactivos, las animaciones pueden traer aún más dinamismo y creatividad a nuestras visualizaciones.

Para ilustrar esta idea, mira la captura de pantalla de un notebook donde creé una animación con los datos de inmigración de Brasil a Canadá. El código que genera esta animación comienza mostrando la figura sin ninguna línea. Al hacer clic en el botón "Play", en la esquina superior izquierda de la figura, la línea comienza a aparecer en el primer tick del eje X, que corresponde al año 1980, y se mueve hasta llegar al final del eje X, mostrando la evolución de los datos a lo largo del tiempo:

Captura de pantalla del Google Colab mostrando la figura generada con la biblioteca Plotly con animación.

Con esto, podemos notar que la animación es una excelente manera de visualizar datos en evolución a lo largo del tiempo.

Te estarás preguntando: ¿cómo podemos crear una animación como esta? No te preocupes, estoy aquí para mostrarte el camino. ¡Te explicaré paso a paso!

1 - Después de obtener el DataFrame solo con los datos de Colombia, como hicimos al principio del curso, cambia el tipo de datos de la columna que contiene los años a int en lugar de mantenerlos como strings:
```python
datos_col['Año'] = datos_col['Año'].astype(int)
```
2 - Luego, creamos un bloque de código donde construiremos esta animación, importando plotly.graph_objs, un módulo de la biblioteca Plotly que contiene clases para crear visualizaciones de datos interactivas y personalizadas.
```python
import plotly.graph_objs as go
```
3 - A continuación, se crea una figura vacía usando la función go.Figure() y se asigna a la variable fig.
```python
fig = go.Figure()
```
4 - Luego, se agrega una línea al gráfico usando la función fig.add_trace(). En esta función, se pasa un objeto Scatter, que recibe como argumentos los datos para los ejes X e Y del gráfico. Para que el gráfico se muestre sin línea antes de hacer clic en el botón de reproducción, usamos iloc[0] en ambas variables. Esto se debe a que iloc[0] selecciona el primer valor de las columnas año e inmigrantes de los datos de Brasil, respectivamente. Al agregar este punto de datos a la visualización del gráfico, inicialmente se mostrará como un solo punto, sin líneas que lo conecten a otros puntos. Además, pasamos el modo de visualización lines, que significa líneas, y el nombre de la línea. También se define el grosor de la línea usando el diccionario line=dict(width=4).
```python
fig.add_trace(
    go.Scatter(x=[datos_col['Año'].iloc[0]], y=[datos_col['Inmigrantes'].iloc[0]], mode='lines', name='Inmigrantes', line=dict(width=4))
)
```
5 - Después de eso, se definen el título del gráfico y las configuraciones de los ejes X e Y usando la función fig.update_layout(). Los argumentos del título son:

    text='<b>Inmigración de Colombianos hacia Canadá en el periodo de 1980 a 2013</b>': define el texto del título como una cadena formateada en negrita (usando las etiquetas HTML "<b>" y "</b>")
    x=0.12: define la posición horizontal del título en el diseño, en relación con el ancho de la figura. El valor 0.12 especifica que el título comenzará al 12% del ancho de la figura.
    xanchor='left': define la alineación horizontal del título. El valor 'left' significa que el título se alineará a la izquierda del diseño.
    font=dict(size=20): define el tamaño del texto del título.

Los argumentos para xaxis y yaxis son diccionarios, con las siguientes propiedades:

    range=[1980, 2013]: define el rango del eje, es decir, el valor mínimo y máximo que se mostrarán. En este caso, el eje x tendrá como valor mínimo 1980 y como valor máximo 2013, mientras que el eje y tendrá como valor mínimo 0 y como valor máximo 7000.

    autorange=False: define si los límites del eje se ajustarán automáticamente (True) o no (False). En este caso, los límites no se ajustarán automáticamente.

    title='<b>Año</b>': define el título del eje. En este caso, el eje x tendrá el título "Año", que está formateado en negrita (usando las etiquetas HTML "" y "").

    title='<b>Número de Inmigrantes</b>': define el título del eje. En este caso, el eje y tendrá el título "Número de Inmigrantes", que está formateado en negrita (usando las etiquetas HTML "<b>" y "</b>").
```python
    fig.update_layout(
        title=dict(
            text='<b>Inmigración de Colombianos hacia Canadá en el periodo de 1980 a 2013</b>',
            x=0.12,
            xanchor='left',
            font=dict(size=20)
        ),
        xaxis=dict(range=[1980, 2013], autorange=False, title='<b>Año</b>'),
        yaxis=dict(range=[0, 7000], autorange=False, title='<b>Número de Inmigrantes</b>'),
    )
```
6 - Se agrega un botón "Play" para la animación usando el argumento updatemenus. Este argumento es una lista que define las opciones de menú para la figura. El valor asignado a esta lista es un diccionario, con las siguientes propiedades:

    type='buttons': define que el menú estará compuesto por botones.
    showactive=False: define que ningún botón estará activo inicialmente.
    buttons=[dict(label='Play', method='animate', args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}])]: Define el botón que se mostrará en el menú. Este botón tiene la etiqueta "Play" (es decir, "reproducir"), que se muestra en el propio botón. El método animate se utiliza para activar la animación de los datos. El argumento args es una lista que contiene dos elementos: el primero es None, indicando que ningún trace (o capa) del gráfico será afectado por la animación, y el segundo es un diccionario que especifica los parámetros de la animación. El parámetro frame define la duración de cada cuadro de la animación y la actualización de cada cuadro. El parámetro fromcurrent determina si se debe mantener el cuadro actual o si la animación debe comenzar desde el primer cuadro.
```python
 updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(
            label='Play',
            method='animate',
            args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}]
        )]
    )],
```
7 - La anchura (width) y la altura (height) del gráfico se definen respectivamente como 1000 y 500.
```python
# Todo el código de la celda anterior, y después:
width=1000,
height=500) 
```
8 - Las configuraciones de animación se especifican mediante la variable frames, que es una lista de objetos Frame de Plotly, conteniendo los datos para cada cuadro de la animación. Cada Frame contiene un trace, que en este caso es un objeto Scatter representando un punto en el gráfico, donde X es el año y Y es el número de inmigrantes. Un bucle for se utiliza para crear un objeto Frame para cada año en el conjunto de datos, añadiendo un punto adicional al gráfico en cada iteración.

Finalmente, la lista frames se asigna a la propiedad frames del objeto Figure (fig) creado anteriormente, lo que permite que la animación se muestre en el gráfico cuando se presiona el botón de control de animación. Cada Frame contiene los datos del gráfico para un año específico y se muestra secuencialmente al presionar el botón "Play".
```python
frames = [go.Frame(data=[go.Scatter(x=datos_col['Año'].iloc[:i+1], y=datos_col['inmigrantes'].iloc[:i+1])]) for i in range(len(datos_col))]
fig.frames = frames
```
9 - La función fig.show() se llama al final para mostrar el gráfico animado en el notebook. Al presionar el botón "Play", el gráfico se animará, mostrando la inmigración de Brasil a Canadá desde 1980 hasta 2013.

El código completo se muestra a continuación:
```python
import plotly.graph_objs as go

# Criando uma figura
fig = go.Figure()

# Adicionando a linha do gráfico e definindo a espessura da linha
fig.add_trace(
    go.Scatter(x=[datos_col['Año'].iloc[0]], y=[datos_col['Inmigrantes'].iloc[0]], mode='lines', name='Inmigrantes', line=dict(width=4))
)

# Definir la configuración del layout
fig.update_layout(
    title=dict(
        text='<b>Inmigración de Colombianos hacia Canadá en el periodo de 1980 a 2013</b>',
        x=0.12,
        xanchor='left',
        font=dict(size=20)
    ),
    xaxis=dict(range=[1980, 2013], autorange=False, title='<b>Año</b>'),
    yaxis=dict(range=[0, 7000], autorange=False, title='<b>Número de Inmigrantes</b>'),
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(
            label='Play',
            method='animate',
            args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}]
        )]
    )],
    width=1000, 
    height=500 
)

# Definir la configuración de la animación
frames = [go.Frame(data=[go.Scatter(x=datos_col['Año'].iloc[:i+1], y=datos_col['Inmigrantes'].iloc[:i+1])]) for i in range(len(datos_col))]
fig.frames = frames

# Mostrar la figura
fig.show()
```
Este enfoque ilustra cómo se pueden crear animaciones dinámicas utilizando Plotly, no solo para líneas sino también para puntos, barras, mapas y mucho más, aprovechando la amplia gama de herramientas y características que ofrece Plotly para crear visualizaciones interactivas y atractivas.

# Desafío: creando una animación para comparar diferentes datos



En la actividad anterior, fue posible comprender cómo crear una animación con la biblioteca Plotly. ¡Ahora viene otro desafío!

¿Recuerdas que creamos una figura estática que contiene los datos de inmigración de Brasil y Argentina? Tu tarea es crear un gráfico animado con Plotly que muestre estos datos. El gráfico debe tener las siguientes características:

    Dos líneas: una para Brasil y otra para Argentina.
    Un botón "Play" para iniciar la animación, mostrando el aumento o disminución del número de inmigrantes a lo largo de los años.
    Las configuraciones de animación deben hacer que las dos líneas se muestren y animen al mismo tiempo.

Consejos:

    Crea un DataFrame con los datos de Argentina y no olvides dejar la columna de años como tipo int (entero).
    Utiliza el código proporcionado para Brasil como base y adáptalo para incluir los datos de Argentina.
    Para configurar las animaciones, puedes hacer un bucle for para recorrer el DataFrame datos_brasil y, para cada iteración, crear una nueva lista que contenga dos objetos del tipo go.Scatter, uno para cada país. Luego, cada lista puede ser utilizada para crear un objeto go.Frame, que se agrega a la lista de frames. Finalmente, la lista de frames puede ser asignada al objeto fig, que es la figura del gráfico que se animará. Con esto, cuando se inicie la animación, el gráfico mostrará las dos líneas en movimiento, una para Brasil y otra para Argentina.

# Lo que aprendimos en esta clase:

    Importar el módulo express de la biblioteca Plotly;
    Crear un gráfico de líneas interactivo;
    Explorar las funcionalidades de la biblioteca Plotly;
    Modificar el tamaño de un gráfico interactivo;
    Rotar los ticks del eje X;
    Agregar título y etiquetas a los ejes;
    Personalizar los gráficos;
    Cambiar colores. Agregar marcadores;
    Guardar gráficos interactivos en formato HTML.

