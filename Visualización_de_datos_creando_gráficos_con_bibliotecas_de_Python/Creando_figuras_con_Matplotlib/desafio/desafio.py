import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Crear el DataFrame con los datos de ventas ---

# Datos proporcionados para el desafío
tiendas = ['A', 'B', 'C', 'D']
ventas_2022 = {
    'Ene': [100, 80, 150, 50],
    'Feb': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'May': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Sep': [240, 160, 290, 130],
    'Oct': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dec': [300, 350, 400, 250]
}

# Crear el DataFrame.
# Se define 'tiendas' como el índice del DataFrame, lo que facilita seleccionar los datos por tienda.
df_ventas = pd.DataFrame(ventas_2022, index=tiendas)

print("--- DataFrame de Ventas por Tienda (2022) ---")
print(df_ventas)
print("\n--- Información del DataFrame ---")
print(df_ventas.info())

# --- 2. Crear la Figura con Subgráficos para cada Tienda ---

# Definimos el tamaño general de la figura.
# Creamos una figura (fig) y una cuadrícula de 2x2 ejes (axes) para los subgráficos.
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

# Ajustar el espaciado entre subgráficos para evitar superposiciones y mejorar la legibilidad.
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# Título general de la figura que abarca todos los subgráficos.
fig.suptitle('Variación de Ventas por Tienda (2022)', fontsize=16, y=0.98) # 'y' ajusta la posición vertical del título

# Obtenemos los nombres de los meses para usarlos en el eje X de cada gráfico.
meses = list(ventas_2022.keys())

# Iterar sobre cada tienda y su correspondiente posición en la cuadrícula de subgráficos.
for i, tienda in enumerate(tiendas):
    # Calcular la fila y columna para el subgráfico actual:
    # Fila: 0 para tiendas A y B, 1 para tiendas C y D (división entera por 2)
    # Columna: 0 para tiendas A y C, 1 para tiendas B y D (resto de la división por 2)
    fila = i // 2
    columna = i % 2

    # Seleccionar los datos de ventas para la tienda actual.
    # Usamos .loc[] para acceder a la fila completa de la tienda por su nombre de índice.
    ventas_tienda = df_ventas.loc[tienda]

    # Graficar la línea en el subgráfico actual (axes[fila, columna]).
    # Añadimos marcadores 'o' para los puntos de datos y un estilo de línea sólido '-'.
    axes[fila, columna].plot(meses, ventas_tienda, marker='o', linestyle='-')

    # Añadir un título específico a cada subgráfico.
    axes[fila, columna].set_title(f'Tienda {tienda}', fontsize=12)

    # Añadir etiquetas a los ejes X e Y de cada subgráfico.
    axes[fila, columna].set_xlabel('Mes', fontsize=10)
    axes[fila, columna].set_ylabel('Número de Ventas', fontsize=10)

    # Establecer los límites del eje Y para todos los subgráficos, como se solicitó.
    # Esto asegura que todos los gráficos tengan la misma escala vertical para una mejor comparación visual.
    axes[fila, columna].set_ylim(0, 450)

    # Rotar las etiquetas del eje X para mejorar la legibilidad, especialmente si hay muchos meses.
    axes[fila, columna].tick_params(axis='x', rotation=45)

    # Añadir una cuadrícula al subgráfico para facilitar la lectura de los valores.
    axes[fila, columna].grid(True, linestyle='--', alpha=0.7)

# Mostrar el gráfico completo con todos los subgráficos.
plt.show()