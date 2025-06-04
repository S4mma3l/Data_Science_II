import pandas as pd
# Importar un archivo CSV
datos = pd.read_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\Leyendo_archivos_CSV\Desafio\datos_sus.csv', sep=';', encoding='ISO-8859-1', skiprows=3, skipfooter=9, engine='python')
# Mostrar las primeras filas del DataFrame
print("mostrando en uso de skiprows y skipfooter para saltar filas al inicio y al final del archivo CSV")
print('ademas el uso de encoding para evitar problemas de codificación y el uso de engine para evitar problemas con el separador')
print(datos.head())

'''
Explicación de los Parámetros:

    encoding='ISO-8859-1':
        ¿Por qué? La codificación es crucial para que los caracteres especiales (como acentos, 'ç' en portugués, etc.) se lean correctamente. ISO-8859-1 (también conocida como Latin-1) es una codificación común para archivos generados en sistemas Windows o en algunas regiones de Latinoamérica y Brasil.
        Si no lo pones: Podrías obtener errores como UnicodeDecodeError o ver caracteres extraños en tus datos.

    sep=';':
        ¿Por qué? Indica el separador de columnas dentro del archivo CSV. Aunque se llama "Comma Separated Values", en muchos países (especialmente en Europa y América Latina) se usa el punto y coma (;) como delimitador porque la coma (,) se usa como separador decimal.
        Consejo: Si al ejecutar el código ves que todas tus columnas están juntas en una sola, o los datos no tienen sentido, prueba cambiando sep=';' por sep=',' (coma) o incluso sep='\t' (tabulación) si fuera un archivo TSV.

    skiprows=3:
        ¿Por qué? Este parámetro le dice a Pandas que ignore las primeras 3 líneas del archivo. Según el desafío, el encabezado real de los datos comienza en la cuarta línea.
        Uso: Útil para saltar metadatos, títulos o líneas en blanco al inicio del archivo.

    skipfooter=9:
        ¿Por qué? Le indica a Pandas que ignore las últimas 9 líneas del archivo. El desafío menciona que estas líneas contienen información sobre el origen de los datos que no son parte de la tabla principal.
        Uso: Perfecto para eliminar pies de página, resúmenes o notas al final del archivo.

    engine='python':
        ¿Por qué? Este parámetro es obligatorio cuando usas skipfooter. Por defecto, read_csv usa un motor de análisis más rápido (el motor 'c'), pero este no es compatible con la funcionalidad skipfooter. El motor 'python' es más flexible y permite esta operación.
        Si no lo pones: Obtendrías un error como ParserError: 'skipfooter' not supported for 'c' engine.
'''