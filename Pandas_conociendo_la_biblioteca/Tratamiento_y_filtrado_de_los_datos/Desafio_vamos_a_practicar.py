import pandas as pd
import os # Importa el módulo 'os' para manejar rutas de archivos de forma robusta

# URL del archivo CSV
url = "https://gist.githubusercontent.com/ahcamachod/807a2c1cf6c19108b2b701ea1791ab45/raw/fb84f8b2d8917a89de26679eccdbc8f9c1d2e933/alumnos.csv"

# Cargar la base de datos
df = pd.read_csv(url)

print("--- DataFrame original (primeras 10 filas) ---")
print(df.head(10))
print("\n--- Valores nulos por columna antes del tratamiento ---")
print(df.isnull().sum())

# 1. Verificar y Tratar Datos Nulos
# Elimina las filas que contengan cualquier valor nulo (ej: en 'Nota')
df.dropna(inplace=True)
print("\n--- DataFrame después de eliminar nulos (primeras 5 filas) ---")
print(df.head()) # Muestra el DF después de dropna

# 2. Eliminar Estudiantes "Alicia" y "Carlos"
# Filtra el DataFrame para excluir a 'Alicia' y 'Carlos'
df = df[~df['Nombre'].isin(['Alicia', 'Carlos'])]
print("\n--- DataFrame después de eliminar Alicia y Carlos (primeras 5 filas) ---")
print(df.head()) # Muestra el DF después de eliminar estudiantes

# 3. Seleccionar Estudiantes Aprobados
# Filtra por estudiantes con 'Nota' mayor o igual a 7.0
# Es crucial usar .copy() para asegurar que df_aprobados sea un DataFrame independiente
df_aprobados = df[df['Nota'] >= 7.0].copy()
print("\n--- DataFrame de Alumnos Aprobados (primeras 5 filas antes de la corrección de notas) ---")
print(df_aprobados.head())

# 4. Corregir Calificaciones de 7.0 a 8.0 (Extra)
# Reemplaza las notas de 7.0 por 8.0 exclusivamente en el DataFrame de aprobados
df_aprobados['Nota'] = df_aprobados['Nota'].replace(7.0, 8.0)
print("\n--- DataFrame de Alumnos Aprobados (primeras 5 filas después de la corrección de notas) ---")
print(df_aprobados.head())

# 5. Guardar el DataFrame de Estudiantes Aprobados
# Define la ruta de salida de forma robusta usando os.path.join
# Para tu caso específico con las barras invertidas en el path literal,
# es recomendable usar un raw string (r"...") para evitar problemas con caracteres de escape.
output_directory = r"Pandas_conociendo_la_biblioteca\Tratamiento_y_filtrado_de_los_datos"
output_filename = "alumnos_aprobados.csv"
full_output_path = os.path.join(output_directory, output_filename)

# Asegurarse de que el directorio exista
os.makedirs(output_directory, exist_ok=True)

df_aprobados.to_csv(full_output_path, index=False)
print(f"\nDataFrame de alumnos aprobados guardado exitosamente en: {full_output_path}")

