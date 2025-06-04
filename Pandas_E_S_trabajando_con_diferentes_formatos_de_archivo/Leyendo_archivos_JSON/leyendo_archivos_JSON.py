import pandas as pd

# Leyendo un archivo JSON
datos_pacientes = pd.read_json('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\\Leyendo_archivos_JSON\\data\\pacientes.json')
# Mostrando las primeras filas del DataFrame
print(datos_pacientes)

# Leyendo un archivo JSON con una estructura más compleja o anidada
datos_pacientes_2 = pd.read_json('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\\Leyendo_archivos_JSON\\data\\pacientes_2.json')
# Mostrando las primeras filas del DataFrame
print(datos_pacientes_2)