import pandas as pd
import matplotlib.pyplot as plt # Asegúrate de importar matplotlib

# --- Carga y Preparación de Datos ---
df = pd.read_csv('Visualización_de_datos_creando_gráficos_con_bibliotecas_de_Python\\Conociendo_la_biblioteca_matplotlib\\datos\\inmigrantes_canada.csv')

# Establecer la columna 'Pais' como índice
df.set_index('Pais', inplace=True)

# Generar una lista de años como strings (para la selección de columnas)
Año = list(map(str, range(1980, 2014)))

# Seleccionar los datos de Brasil
brasil = df.loc['Brasil', Año]
# Crear un DataFrame para Brasil
datos_bra = pd.DataFrame({"Año": brasil.index.tolist(), "Inmigrantes": brasil.values.tolist()})

# Seleccionar los datos de Argentina
argentina = df.loc['Argentina', Año]
# Crear un DataFrame para Argentina
datos_arg = pd.DataFrame({"Año": argentina.index.tolist(), "Inmigrantes": argentina.values.tolist()})

print("--- DataFrame de Brasil ---")
print(datos_bra.head())
print("\n--- DataFrame de Argentina ---")
print(datos_arg.head())

# --- Generación del Gráfico ---

plt.figure(figsize=(10, 6)) # Definimos un tamaño de figura un poco más grande para mejor visualización

# 1. Graficar la línea de Brasil: Usamos directamente datos_bra
plt.plot(datos_bra['Año'], datos_bra['Inmigrantes'], label='Brasil', marker='o', linestyle='-') # Añadí marcadores y estilo de línea

# 2. Graficar la línea de Argentina: Usamos directamente datos_arg
plt.plot(datos_arg['Año'], datos_arg['Inmigrantes'], label='Argentina', marker='x', linestyle='--') # Añadí marcadores y estilo de línea

# Personalización del gráfico
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010', '2013'], rotation=45, ha='right') # Alineación a la derecha
plt.title('Inmigrantes de Brasil y Argentina a Canadá (1980-2013)', fontsize=14) # Título del gráfico con tamaño de fuente
plt.xlabel('Año', fontsize=12) # Etiqueta del eje x con tamaño de fuente
plt.ylabel('Número de Inmigrantes', fontsize=12) # Etiqueta del eje y con tamaño de fuente
plt.legend(title='País') # Añadimos una leyenda para distinguir las líneas
plt.grid(True, linestyle='--', alpha=0.6) # Añadimos una cuadrícula para facilitar la lectura
plt.tight_layout() # Ajusta automáticamente los parámetros del gráfico para un diseño ajustado

plt.show() # Mostramos el gráfico
