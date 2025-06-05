import requests
import json
import pandas as pd

datos_frutas = requests.get('https://fruityvice.com/api/fruit/all')

resultado = json.loads(datos_frutas.text)

resultado_final = pd.DataFrame(resultado)

print(resultado_final)
resultado_final.to_json('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo/Leyendo_archivos_JSON/desafio/frutas.json')