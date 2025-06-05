import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData, Table, inspect, text
import pandas as pd

engine = create_engine ("sqlite:///:memory:")

archivo = 'Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\\Leyendo_banco_de_datos\\data\\clientes_banco.csv'

datos = pd.read_csv(archivo)
print(datos.head())

datos.to_sql('clientes', engine, index=False)

inspector = inspect(engine)
print(inspector.get_table_names())