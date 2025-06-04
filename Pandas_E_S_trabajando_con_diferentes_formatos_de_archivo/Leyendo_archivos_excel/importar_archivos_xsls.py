import pandas as pd
# Importar un archivo Excel
archivo_excel = 'Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\\Leyendo_archivos_excel\\data\\emisiones_CO2.xlsx'

datos_co2 = pd.read_excel(archivo_excel)
# Mostrar las primeras filas del DataFrame
print(datos_co2.head())

# ver las hojas del archivo Excel
hojas_excel = pd.ExcelFile(archivo_excel)
print(hojas_excel.sheet_names)

# ver una hoja en concreto
percapita = pd.read_excel(archivo_excel, sheet_name='emisiones_percapita')
# Mostrar las primeras filas de la hoja seleccionada
print(percapita.tail())

fuentes = pd.read_excel(archivo_excel, sheet_name='fuentes')
# Mostrar las primeras filas de la hoja seleccionada
print(fuentes.tail())

intervalos = pd.read_excel(archivo_excel, sheet_name='emisiones_C02', usecols='A:D') # nrows=10 limita el número de filas a leer
# Mostrar las primeras filas de la hoja seleccionada con columnas específicas
print(intervalos)

intervalos.to_excel('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\\Leyendo_archivos_excel\\data\\co2_percapita.xlsx', index=False)
# Guardar el DataFrame en un nuevo archivo Excel

# Verificar que el archivo se ha guardado correctamente
nuevo_archivo = pd.read_excel('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\\Leyendo_archivos_excel\\data\\co2_percapita.xlsx')
print(nuevo_archivo.head())