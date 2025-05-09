import numpy as np

clientes = np.array([[1, 'Juan', 30, 'Calle A', 100, 'electrónicos'],
                     [2, 'Maria', 25, 'Calle B', 200, 'moda'],
                     [3, 'Pedro', 35, 'Calle C', 50, 'deportes']])


intencion_compras = clientes[:, 4:6]
print(intencion_compras)  # Imprime la intención de compras de los clientes con el rango de columnas 4 a 6 (excluyendo la 6)



intencion_compras = clientes[:, 4:]
print(intencion_compras)  # Imprime la intención de compras de los clientes desde la columna 4 en adelante