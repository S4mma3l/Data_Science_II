sheet_id = '1-jQBJQpqopwEhwfgpcd_hjUbVGoo8-mV1I4iK252ROo'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'

import pandas as pd
# Importar datos de Google Sheets   
datos_google_sheets = pd.read_csv(url)
# Mostrar las primeras filas del DataFrame
print(datos_google_sheets.head())

datos_google_sheets.to_csv('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo/Leyendo_archivos_excel/desafio/co2_percapita_desafio.csv', index=False)