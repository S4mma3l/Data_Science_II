### Para saber más: profundizando en la función read_excel



Microsoft Excel es una de las herramientas de hojas de cálculo más utilizadas en el mundo, siendo ampliamente utilizada para almacenar y analizar datos en formato de tabla. En el video anterior, mostramos cómo la función read_excel se puede usar para leer un archivo de Excel en formato xlsx. Sin embargo, esta función es capaz de leer archivos en otros formatos, como: xls, xlsm, xlsb, odf, ods y odt.

¿Vamos a entender un poco más sobre estos diferentes tipos de archivos?

xls

El formato xls es un formato de archivo de Excel más antiguo y se utilizó hasta la versión de 2003.

xlsx

El formato xlsx es el formato de archivo de Excel predeterminado a partir de la versión 2007. Este formato se basa en XML(Extensible Markup Language - Lenguaje de marcación extensible) y es ampliamente compatible con otras herramientas de hojas de cálculo online, incluida Google Sheets.

    Atención : Si tienes dudas sobre el término XML, ¡no te preocupes! Tendremos un aula sobre este tema más adelante. En ella entenderás qué es este formato, cómo leer y escribir en XML.

xlsm

También existe xlsm, una extensión de archivo utilizada por Excel para almacenar hojas de cálculo que contienen macros. Son secuencias de comandos o instrucciones que se pueden ejecutar automáticamente para realizar tareas específicas en la hoja de trabajo.

Entonces, el formato xlsm permite guardar las macros junto con la hoja de trabajo, de modo que puedan ejecutarse cada vez que se abra la hoja de trabajo.

xlsb

Por último, tenemos el formato xlsb, una extensión de archivo que utiliza Excel para almacenar hojas de cálculo en formato binario. La codificación binaria permite abrir y guardar hojas de cálculo más rápido que aquellas en formato xlsx.

Los formatos odf, ods y odt son archivos abiertos, gratuitos y universales que pueden ser utilizados por cualquier software, es decir, fueron creados para ser independientes de plataformas, esto quiere decir que pueden ser utilizados en diferentes sistemas operativos, como Windows, Linux y Mac OS.

Además, son independientes de aplicaciones y se pueden utilizar en muchos programas diferentes, incluidos OpenOffice, LibreOffice, Google Docs y Microsoft Office. Este estándar de archivos fue creado y es mantenido por OASIS (Organization for the Advancement of Structured Information Standards), una organización internacional creada para desarrollar y promover estándares digitales para su uso en Internet.

¡Muy bien! Ahora sabemos un poco más sobre todos los tipos de archivos que se pueden leer con la función read_excel.

Si deseas profundizar más en el tema, aquí te dejamos algunos enlaces a materiales que fueron utilizados como referencia:

    Formatos de archivo compatibles con Excel  https://support.microsoft.com/es-es/office/formatos-de-archivo-que-admite-excel-0943ff2c-6014-4e8d-aaea-b83d51d46247


    OpenDocument  https://pt.wikipedia.org/wiki/OpenDocument

### Leyendo intervalos

Théo está trabajando en una análisis de datos en Python utilizando la biblioteca Pandas. Él está utilizando una hoja de cálculo de Excel que tiene 4 páginas y quiere leer sólo una de las tablas contenidas en una de ellas. La tabla que quiere leer está en la página "pagos" y los datos están en las primeras 50 filas desde la columna F hasta la columna L de la hoja de cálculo.

¿Cuál es el código correcto que debería usar Théo para leer sólo el intervalo deseado?
```python
df = pd.read_excel('datos.xlsx', sheet_name=’pagos’, usecols='F:L', nrows=50)
```
El parámetro sheet_name se utiliza para especificar la página de la hoja de cálculo que Théo quiere leer. En este caso, es la página "pagos". El parámetro usecols se utiliza para especificar las columnas que se leerán, que son las columnas de la F a la L. Además, el parámetro nrows se agregó para especificar el número de líneas que Théo quiere leer, que es 50.

### Para saber más: importando hacia Google Sheets



Google Sheets es una herramienta de hojas de cálculo online basada en nube que le permite crear, editar y colaborar en hojas de cálculo de manera fácil y conveniente. Es una de las aplicaciones de Google Workspace que ofrece una alternativa a Microsoft Excel.

Con Google Sheets se puede crear y formatear hojas de cálculo, agregar fórmulas y funciones, crear gráficos y tablas dinámicas y trabajar con otros usuarios con datos en tiempo real. También admite la importación y exportación de varios formatos de archivos, como CSV y XLSX.

Una de las principales ventajas de Google Sheets es la colaboración en tiempo real. Varias personas pueden trabajar simultáneamente en la misma hoja de trabajo y ver los cambios simultáneamente. Esto facilita el trabajo en proyectos de equipo, aumentando la eficiencia y la productividad.

Para importar el archivo de Excel emisiones_CO2.xlsx hacia Google Sheets, siga estos pasos:

    Abra la página de Google Sheets y haga clic en "Ir a Sheets". Inicie sesión en su cuenta de Google si es necesario.
    Haga clic en Nueva Hoja de cálculo en blanco.
    Cuando haya abierto, haga clic en "Archivo" (File) en el menú superior y luego haga clic en la opción "Importar archivo" (Import).
    Haga clic en la pestaña "Subir" (Upload) y seleccione el archivo que desea importar. Puede hacer clic en la opción Examinar para ubicar el archivo en su computadora o arrastrar el archivo dentro de la pestaña.
    Espere mientras se carga el archivo. Cuando se complete la carga, verá un mensaje de confirmación y podrá hacer clic en "Importar datos" (Import data).
    Después de importar, se mostrarán los datos.

¡Excelente! Los datos se han importado correctamente. En el siguiente video, aprenderá cómo leer estos datos en Google Colab usando el link para compartir de Google Sheets.


### Desafío: leyendo datos de otro link



Es hora de que pongas a prueba los conocimientos desarrollados durante la clase. Tenemos un link de Google Sheets que contiene datos importantes sobre las emisiones de dióxido de carbono en todo el mundo. El conjunto de datos se obtuvo de Kaggle y consta de las emisiones de CO2 per cápita de todos los países del mundo entre 1990 y 2019.

En este desafío, tu función es leer este link de Google Sheets y luego guardar el DataFrame obtenido en formato CSV. ¿Listo para comenzar?

https://cdn3.gnarususercontent.com.br/1980-pandas-e-s/emisiones_carbono_mundo.xlsx

### En esta aula, aprendimos a:

    Entender lo qué es una hoja de cálculo;
    Leer un archivo en formato XLSX;
    Identificar páginas en una hoja de trabajo;
    Leer páginas e intervalos específicos de una hoja de trabajo;
    Leer sólo unas pocas líneas de una hoja de cálculo;
    Escribir un archivo en formato XLSX;
    Importar datos de Google Sheets.

