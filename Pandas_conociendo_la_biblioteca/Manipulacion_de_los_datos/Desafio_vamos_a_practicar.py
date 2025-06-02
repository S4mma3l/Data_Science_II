import pandas as pd # Importa la librería pandas para manipulación de datos
import os # Importa el módulo os para trabajar con rutas de archivos de forma segura

# --- 1. Carga de la Base de Datos ---
# Define la URL del archivo CSV que contiene los datos de los estudiantes
url = "https://gist.githubusercontent.com/ahcamachod/807a2c1cf6c19108b2b701ea1791ab45/raw/fb84f8b2d8917a89de26679eccdbc8f9c1d2e933/alumnos.csv"
df = pd.read_csv(url) # Carga el archivo CSV en un DataFrame de pandas

# --- 2. Inspección Inicial y Tratamiento de Datos Nulos ---
print("--- DataFrame Original (Primeras 5 filas) ---")
print(df.head()) # Muestra las primeras filas del DataFrame para una primera inspección

print("\n--- Conteo de Valores Nulos por Columna ---")
print(df.isnull().sum()) # Verifica cuántos valores nulos hay en cada columna

# Elimina las filas que contienen cualquier valor nulo.
# `inplace=True` modifica el DataFrame original directamente.
# Es una buena práctica para este tipo de datos donde una nota nula podría ser un registro incompleto.
df.dropna(inplace=True)
print("\n--- DataFrame después de eliminar filas con valores nulos (Primeras 5 filas) ---")
print(df.head())

# --- 3. Eliminación de Estudiantes Específicos ---
# Los estudiantes "Alicia" y "Carlos" ya no forman parte del grupo y deben ser eliminados.
# Se utiliza el operador '~' para seleccionar las filas donde el 'Nombre' NO está en la lista ['Alicia', 'Carlos'].
# `.copy()` se usa para crear una copia explícita del DataFrame filtrado.
# Esto previene el `SettingWithCopyWarning` si se modifican las columnas en `df` más adelante.
df = df[~df['Nombre'].isin(['Alicia', 'Carlos'])].copy()
print("\n--- DataFrame después de eliminar a 'Alicia' y 'Carlos' (Primeras 5 filas) ---")
print(df.head())

# --- 4. Creación de Nuevas Columnas Basadas en Puntos Extras ---

# a) Crear la columna "Puntos_extras"
# Los puntos extras corresponden al 40% de la nota actual de cada estudiante.
# Se realiza una operación directa entre la columna 'Nota' y un valor numérico.
df['Puntos_extras'] = df['Nota'] * 0.40
print("\n--- DataFrame con la nueva columna 'Puntos_extras' (Primeras 5 filas) ---")
print(df[['Nombre', 'Nota', 'Puntos_extras']].head())

# b) Crear la columna "Notas_finales"
# Contiene la suma de la nota actual y los puntos extras.
# Se realiza una operación de suma entre dos columnas existentes.
df['Notas_finales'] = df['Nota'] + df['Puntos_extras']
print("\n--- DataFrame con la nueva columna 'Notas_finales' (Primeras 5 filas) ---")
print(df[['Nombre', 'Nota', 'Puntos_extras', 'Notas_finales']].head())

# c) Crear la columna "Aprobado_final"
# Indica si el estudiante está aprobado (True si Nota_final >= 7.0) o reprobado (False si Nota_final < 7.0).
# Se asigna directamente el resultado de una expresión booleana a la nueva columna.
df['Aprobado_final'] = df['Notas_finales'] >= 7.0
print("\n--- DataFrame con la nueva columna 'Aprobado_final' (Primeras 5 filas) ---")
print(df[['Nombre', 'Nota', 'Notas_finales', 'Aprobado', 'Aprobado_final']].head())

# --- 5. Filtrar Estudiantes Aprobados Originalmente (para el archivo CSV) ---
# Filtra el DataFrame para seleccionar solo a los estudiantes cuya 'Nota' original era >= 7.0.
# Importante: Si la tarea es guardar los "aprobados originales" antes de los puntos extra,
# usamos df['Nota'] >= 7.0. Si es después de puntos extra, sería df['Notas_finales'] >= 7.0.
# Aquí nos ceñimos a la instrucción original: "aplica un filtro que seleccione solo a los estudiantes que fueron aprobados."
# La corrección de 7.0 a 8.0 se aplica a ESTOS estudiantes aprobados.
df_aprobados_originales = df[df['Nota'] >= 7.0].copy() # Usamos .copy() para crear una copia independiente

# --- 6. Corregir Calificaciones para Estudiantes Aprobados (Extra) ---
# Se nota que algunas calificaciones de 7.0 en estudiantes aprobados debían ser 8.0.
# Se usa `.replace()` para cambiar todos los valores '7.0' a '8.0' en la columna 'Nota'
# de los estudiantes ya identificados como aprobados (`df_aprobados_originales`).
df_aprobados_originales['Nota'] = df_aprobados_originales['Nota'].replace(7.0, 8.0)
print("\n--- Estudiantes Aprobados con Nota de 7.0 corregida a 8.0 (Primeras 5 filas) ---")
print(df_aprobados_originales[['Nombre', 'Nota', 'Notas_finales', 'Aprobado', 'Aprobado_final']].head())


# --- 7. Guardar el DataFrame de Estudiantes Aprobados ---
# Define el directorio y el nombre del archivo de salida.
# `os.path.join` es la forma más robusta de construir rutas de archivos,
# asegurando compatibilidad entre sistemas operativos (Windows, macOS, Linux).
# Los raw strings (r"...") son útiles para rutas de Windows que contienen barras invertidas.
output_directory = r"Pandas_conociendo_la_biblioteca\Manipulacion_de_los_datos"
output_filename = "alumnos_aprobados.csv"
full_output_path = os.path.join(output_directory, output_filename)

# Crea el directorio si no existe. `exist_ok=True` evita un error si ya existe.
os.makedirs(output_directory, exist_ok=True)

# Guarda el DataFrame de estudiantes aprobados en un archivo CSV.
# `index=False` evita escribir el índice del DataFrame como una columna en el CSV.
df_aprobados_originales.to_csv(full_output_path, index=False)
print(f"\nDataFrame de alumnos aprobados guardado exitosamente en: {full_output_path}")

# --- 8. Verificación Final: Estudiantes Recién Aprobados por Puntos Extra ---
# Selecciona los estudiantes que NO estaban 'Aprobado' originalmente,
# pero que SÍ están 'Aprobado_final' después de los puntos extras.
estudiantes_recien_aprobados = df[(df['Aprobado'] == False) & (df['Aprobado_final'] == True)]

print("\n--- Estudiantes que NO estaban aprobados originalmente, pero SÍ después de puntos extras ---")
# Muestra las columnas más relevantes para estos estudiantes
print(estudiantes_recien_aprobados[['Nombre', 'Nota', 'Puntos_extras', 'Notas_finales', 'Aprobado', 'Aprobado_final']])