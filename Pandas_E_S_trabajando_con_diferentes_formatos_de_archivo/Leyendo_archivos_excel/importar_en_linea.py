sheet_id = '1axuvpJty18VEdks71VSfQIDwDQR8AKwp86R8eu50VlY' # ID del Google Sheet que se quiere importar
# Este ID se puede obtener de la URL del Google Sheet, que tiene el formato: # https://docs.google.com/spreadsheets/d/ID_DEL_SHEET/edit#gid=0
# El ID es la parte entre /d/ y /edit del enlace
sheet_name = 'emisiones_percapita' # Nombre de la hoja que se quiere importar
# Importar datos de Google Sheets en línea usando pandas
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}' # URL para importar datos de Google Sheets con api de Google Sheets que es : gviz/tq y agregar elformato de salida como csv y se especifica la hoja

import pandas as pd
# Importar datos de Google Sheets
datos_google_sheets = pd.read_csv(url)
# Mostrar las primeras filas del DataFrame
print(datos_google_sheets.head())

