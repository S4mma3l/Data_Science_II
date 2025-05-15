import pandas as pd

df = pd.read_csv("Pandas_youtube\\banco_clientes.csv")
print(df)

df['nombre']= df['nombre'].str.upper()  # Convierte a mayúsculas
print(df)

df['telefono']= df['telefono'].str.replace("(", "", regex= False).str.replace(")", "", regex=False)  # Elimina el paréntesis
print(df)

df['cp']= df['direccion'].str.extract('(\d{5}-\d{3})')  # Extrae el código postal
print(df)

df['direccion']= df['direccion'].str.replace("(\d{5}-\d{3})", "", regex=True).str.strip()  # Elimina el código postal
print(df)

df[['calle', 'direccion']]= df['direccion'].str.replace(',','', regex= False).str.split('\s(?=\d+$)', expand=True)  # Separa la calle y el número de la dirección
print(df)

df = df.drop('direccion', axis = 1)  # Elimina la columna 'direccion'
print(df)

# https://github.com/ingridcristh/manipulacion_de_string