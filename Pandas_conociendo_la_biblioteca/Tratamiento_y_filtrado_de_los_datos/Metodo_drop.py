import pandas as pd

datos = pd.DataFrame([['Plaza', 'Cebolla', 2.5], 
                      ['Mercado', 'Cebolla', 1.99], 
                      ['Supermercado', 'Cebolla', 1.69], 
                      ['Plaza', 'Tomate', 4], 
                      ['Mercado', 'Tomate', 3.29], 
                      ['Supermercado', 'Tomate', 2.99], 
                      ['Plaza', 'Papa', 4.2], 
                      ['Mercado', 'Papa', 3.99], 
                      ['Supermercado', 'Papa', 3.69]],
                      columns = ['Comercio', 'Producto', 'Precio'])

print(datos)

datos.drop([2, 5, 8], axis=0, inplace=True) # Elimina la fila con índice 'Supermercado'
print(datos)