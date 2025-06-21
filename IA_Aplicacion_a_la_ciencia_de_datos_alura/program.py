import pandas as pd
import warnings
import matplotlib.pyplot as plt
import os
import matplotlib.dates as mdates # Para formatear fechas en el eje X


# Ignorar advertencias, aunque es recomendable manejarlas de forma más específica si es posible.
warnings.filterwarnings("ignore")

# --- 1. Definición de URLs de los DataFrames ---
url_clientes = "IA_Aplicacion_a_la_ciencia_de_datos_alura\\data\\clientes_zoop.csv"
url_ventas = "IA_Aplicacion_a_la_ciencia_de_datos_alura\\data\\ventas_zoop.csv"

# --- 2. Carga de los DataFrames ---
try:
    clientes = pd.read_csv(url_clientes)
    ventas = pd.read_csv(url_ventas)
    print("¡DataFrames cargados exitosamente!\n")
except Exception as e:
    print(f"Error al cargar los DataFrames: {e}")
    # En un entorno real, podrías querer salir o manejar el error de otra forma
    exit()

# --- 3. Preprocesamiento de DataFrames ---
# Convertir la columna 'fecha' del DataFrame de ventas a tipo datetime.
# Esto es crucial para cualquier análisis temporal.
ventas['fecha'] = pd.to_datetime(ventas['fecha'])

# --- 4. Función para la Exploración de DataFrames ---
def explorar_dataframe(df, nombre_df):
    """
    Realiza una exploración básica de un DataFrame de pandas.
    Muestra las primeras filas, información general, estadísticas descriptivas
    y conteo de valores únicos para columnas categóricas.
    """
    print(f"--- Exploración del DataFrame: '{nombre_df}' ---")

    print(f"\n{nombre_df}:")
    print(df.head()) # Mostrar primeras filas

    print(f"\n--- Información del DataFrame '{nombre_df}' ---")
    df.info() # Información general (tipos de datos, nulos)

    print(f"\n--- Estadísticas descriptivas del DataFrame '{nombre_df}' ---")
    print(df.describe()) # Estadísticas para columnas numéricas

    # Identificar y explorar columnas categóricas (objetos y booleanos)
    # Excluir 'fecha' y 'horario' de un conteo simple de value_counts si no es relevante
    categorical_cols = df.select_dtypes(include=['object', 'bool', 'category']).columns.tolist()
    if 'horario' in categorical_cols:
        categorical_cols.remove('horario') # Quitar horario si no se quiere contar como una categoría típica
    if 'fecha' in categorical_cols:
        categorical_cols.remove('fecha') # Quitar fecha si no se quiere contar como una categoría típica

    for col in categorical_cols:
        print(f"\n--- Conteo de valores únicos por '{col}' en '{nombre_df}' ---")
        print(df[col].value_counts())
    print("\n" + "="*50 + "\n") # Separador para mejor visualización

# --- 5. Ejecutar la Exploración para ambos DataFrames ---
explorar_dataframe(clientes, "clientes")
explorar_dataframe(ventas, "ventas")

# --- 6. Unir los DataFrames 'ventas' y 'clientes' ---
# Se realiza un 'inner merge' en 'ID_compra'.
# Importante: Si no hay 'ID_compra' comunes, el DataFrame resultante estará vacío.
# Si esperas que haya coincidencias pero tus datos de ejemplo no las tienen,
# considera usar 'how='left'' o 'how='outer'' para mantener todas las filas.
df_unido = pd.merge(ventas, clientes, on='ID_compra', how='inner')
print("--- Unión de DataFrames 'ventas' y 'clientes' completada ---")

# --- 7. Definir y Reorganizar las columnas del DataFrame unido ---
# Se especifican todas las columnas esperadas en el orden deseado.
column_order = [
    'ID_compra', 'fecha', 'horario', 'categoria', 'precio_unitario',
    'cantidad', 'envio', 'metodo_pago', 'ID_cliente', 'edad',
    'sexo_biologico', 'ciudad', 'estado', 'region', 'cashback', 'nota'
]

# Reorganizar las columnas. Si alguna columna en `column_order` no está en `df_unido`
# (por ejemplo, si el merge resultó vacío), esto podría causar un KeyError.
# Se asume que `df_unido` contendrá todas estas columnas si la unión es exitosa.
try:
    df_final = df_unido[column_order]
    print("\n--- Columnas del DataFrame final reorganizadas ---")
    print(df_final.head())
    print("\n--- Información del DataFrame final ---")
    df_final.info()
except KeyError as e:
    print(f"\nAdvertencia: Una o más columnas esperadas no se encontraron después de la unión: {e}")
    print("Esto puede ocurrir si no hay coincidencias de 'ID_compra' y el DataFrame unido está vacío.")
    print("\nDataFrame unido (df_unido) antes de la reorganización de columnas:")
    print(df_unido.head())

# --- Información del DataFrame final ---
print("\n--- Información del DataFrame final ---")
df_final.info()

# --- 1. Crear la tabla 'metodos_de_pago' ---
# Asumiendo que 'df_final' ya está cargado y disponible en tu entorno.
# Contar la frecuencia de cada método de pago
metodos_de_pago = df_final['metodo_pago'].value_counts().reset_index()
metodos_de_pago.columns = ['metodo_pago', 'cantidad'] # Renombrar las columnas para mayor claridad

print("\n--- Tabla Resumen de Métodos de Pago ---\n")
print(metodos_de_pago)

# --- 2. Crear la visualización (gráfico de barras) con Matplotlib ---

# Ordenar los datos para la visualización (de mayor a menor cantidad)
metodos_de_pago_sorted = metodos_de_pago.sort_values(by='cantidad', ascending=False)

plt.figure(figsize=(10, 6)) # Define el tamaño de la figura para mejor legibilidad
plt.barh(metodos_de_pago_sorted['metodo_pago'], metodos_de_pago_sorted['cantidad'], color='skyblue')

# Añadir etiquetas y título
plt.xlabel('Cantidad de Usos', fontsize=12)
plt.ylabel('Método de Pago', fontsize=12)
plt.title('Métodos de Pago Más Utilizados en Zoop', fontsize=14)

# Invertir el eje Y para que el método con mayor cantidad esté arriba
plt.gca().invert_yaxis()

# Añadir los valores de la cantidad al lado de cada barra
for index, value in enumerate(metodos_de_pago_sorted['cantidad']):
    plt.text(value, index, str(value), va='center')

plt.tight_layout() # Ajusta automáticamente los parámetros de la subtrama para que quepa en el área de la figura.

# Guardar la visualización como una imagen PNG
file_name = 'metodos_de_pago_mas_utilizados.png'
plt.savefig(f"IA_Aplicacion_a_la_ciencia_de_datos_alura\\data\\{file_name}", format='png', dpi=300)

print(f"\nGráfico de Métodos de Pago guardado como '{file_name}'.")
print("Puedes abrir este archivo de imagen en tu sistema.")

# Asumiendo que 'df_final' ya está cargado y disponible en tu entorno.

# --- 1. Calcular la columna 'facturacion' ---
df_final['facturacion'] = (df_final['precio_unitario'] * df_final['cantidad']) + df_final['envio']

# --- 2. Agrupar por categoría y sumar la facturación ---
facturacion_por_categoria = df_final.groupby('categoria')['facturacion'].sum().reset_index()

# --- 3. Ordenar los resultados para la visualización (de mayor a menor facturación) ---
facturacion_por_categoria_sorted = facturacion_por_categoria.sort_values(by='facturacion', ascending=False)

print("\n--- Tabla de Facturación por Categoría ---\n")
print(facturacion_por_categoria_sorted)

# --- 4. Crear la visualización (gráfico de barras horizontales) con Matplotlib ---

plt.figure(figsize=(12, 8)) # Define el tamaño de la figura para mejor legibilidad
plt.barh(facturacion_por_categoria_sorted['categoria'], facturacion_por_categoria_sorted['facturacion'], color='lightgreen')

# Añadir etiquetas y título
plt.xlabel('Facturación Total', fontsize=12)
plt.ylabel('Categoría de Producto', fontsize=12)
plt.title('Facturación Total por Categoría de Producto en Zoop', fontsize=14)

# Invertir el eje Y para que la categoría con mayor facturación esté arriba
plt.gca().invert_yaxis()

# Añadir los valores de facturación al lado de cada barra
for index, value in enumerate(facturacion_por_categoria_sorted['facturacion']):
    plt.text(value, index, f'${value:,.2f}', va='center') # Formatear como moneda

plt.tight_layout() # Ajusta automáticamente los parámetros de la subtrama para que quepa en el área de la figura.

# Guardar la visualización como una imagen PNG
file_name = 'facturacion_por_categoria.png'
plt.savefig(f"IA_Aplicacion_a_la_ciencia_de_datos_alura\\data\\{file_name}", format='png', dpi=300)

print(f"\nGráfico de Facturación por Categoría guardado como '{file_name}'.")
print("Puedes abrir este archivo de imagen en tu sistema.")

# --- 1. Calcular la columna 'facturacion' si no existe ---
# Esto asegura que 'facturacion' esté disponible para el cálculo mensual.
if 'facturacion' not in df_final.columns:
    df_final['facturacion'] = (df_final['precio_unitario'] * df_final['cantidad']) + df_final['envio']
    print("\nColumna 'facturacion' calculada y añadida a df_final.")
else:
    print("\nLa columna 'facturacion' ya existe en df_final.")


# --- 2. Agrupar por mes y sumar la facturación ---
# Extraer el mes de la columna 'fecha' y agrupar
ventas_mensuales = df_final.set_index('fecha').resample('M')['facturacion'].sum().reset_index()

# --- 3. Crear la columna 'mes' con los nombres traducidos ---
meses_traduccion = {
    'January': 'Ene', 'February': 'Feb', 'March': 'Mar', 'April': 'Abr',
    'May': 'May', 'June': 'Jun', 'July': 'Jul', 'August': 'Ago',
    'September': 'Sep', 'October': 'Oct', 'November': 'Nov', 'December': 'Dic'
}

# Obtener el nombre del mes en inglés y luego traducirlo
ventas_mensuales['mes_nombre_en'] = ventas_mensuales['fecha'].dt.strftime('%B')
ventas_mensuales['mes'] = ventas_mensuales['mes_nombre_en'].map(meses_traduccion)

print("\n--- Ventas Totales Mensuales ---\n")
print(ventas_mensuales[['mes', 'facturacion']])

# --- 4. Crear el gráfico de líneas con Matplotlib ---

plt.figure(figsize=(14, 7)) # Define el tamaño de la figura

# Aseguramos el orden correcto de los meses en el eje X
# Obtener el orden único de los meses de las fechas originales o del dataframe agrupado
# Para asegurar el orden cronológico si abarca varios años, usaremos la fecha original
# Si es para un solo año o el orden importa solo por mes, podemos usar el mapeo
# Para este caso, dado que es 'ventas_mensuales' con fechas, se ordenará automáticamente.

plt.plot(ventas_mensuales['fecha'], ventas_mensuales['facturacion'], marker='o', linestyle='-', color='blue')

# Añadir etiquetas y título
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Ventas Totales ($)', fontsize=12)
plt.title('Ventas Totales Mensuales de Zoop', fontsize=14)

# Formatear el eje X para mostrar solo los nombres de los meses traducidos
# Locators para fijar las marcas en cada mes
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
# Formatters para usar el nombre del mes
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b')) # %b da la abreviación del mes en el locale actual, o usaremos la columna 'mes'

# Si el locale no es español para %b, podemos forzar las etiquetas usando la columna 'mes'
# Obtener las fechas y las etiquetas de los meses traducidos
x_ticks = ventas_mensuales['fecha']
x_labels = ventas_mensuales['mes']
plt.xticks(x_ticks, x_labels, rotation=45, ha='right')

plt.grid(True, linestyle='--', alpha=0.6) # Añadir una cuadrícula para mejor lectura
plt.tight_layout() # Ajusta automáticamente los parámetros de la subtrama para que quepa en el área de la figura.

# Guardar la visualización como una imagen PNG
file_name = 'ventas_totales_mensuales.png'
plt.savefig(f"IA_Aplicacion_a_la_ciencia_de_datos_alura\\data\\{file_name}", format='png', dpi=300)

print(f"\nGráfico de Ventas Totales Mensuales guardado como '{file_name}'.")
print("Puedes abrir este archivo de imagen en tu sistema.")

# --- 1. Calcular la columna 'facturacion' si no existe ---
if 'facturacion' not in df_final.columns:
    df_final['facturacion'] = (df_final['precio_unitario'] * df_final['cantidad']) + df_final['envio']
    print("\nColumna 'facturacion' calculada y añadida a df_final.")
else:
    print("\nLa columna 'facturacion' ya existe en df_final.")

# --- 2. Extraer el trimestre y agrupar por trimestre y método de pago ---
df_final['trimestre'] = df_final['fecha'].dt.to_period('Q') # Extrae el trimestre
ventas_trimestrales_metodo_pago = df_final.groupby(['trimestre', 'metodo_pago'])['facturacion'].sum().unstack(fill_value=0)

# Reordenar los trimestres cronológicamente para la visualización
ventas_trimestrales_metodo_pago = ventas_trimestrales_metodo_pago.sort_index()

print("\n--- Ventas Trimestrales por Método de Pago ---\n")
print(ventas_trimestrales_metodo_pago)

# --- 3. Crear el gráfico de barras apiladas con Matplotlib ---

plt.figure(figsize=(14, 8)) # Define el tamaño de la figura

# Crear el gráfico de barras apiladas
# Cada columna de 'ventas_trimestrales_metodo_pago' representa un método de pago.
# El índice es el trimestre.
ventas_trimestrales_metodo_pago.plot(kind='bar', stacked=True, ax=plt.gca())

# Añadir etiquetas y título
plt.xlabel('Trimestre', fontsize=12)
plt.ylabel('Ventas Totales ($)', fontsize=12)
plt.title('Ventas Trimestrales por Método de Pago', fontsize=14)

# Rotar las etiquetas del eje X para mejor legibilidad
plt.xticks(rotation=45, ha='right')

# Añadir leyenda
plt.legend(title='Método de Pago', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.grid(axis='y', linestyle='--', alpha=0.7) # Cuadrícula en el eje Y
plt.tight_layout() # Ajusta automáticamente los parámetros de la subtrama para que quepa en el área de la figura.

# Guardar la visualización como una imagen PNG
file_name = 'ventas_trimestrales_metodo_pago_apiladas.png'
plt.savefig(f"IA_Aplicacion_a_la_ciencia_de_datos_alura\\data\\{file_name}", format='png', dpi=300)

print(f"\nGráfico de Ventas Trimestrales por Método de Pago guardado como '{file_name}'.")
print("Puedes abrir este archivo de imagen en tu sistema.")