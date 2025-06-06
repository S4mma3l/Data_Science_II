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

query = 'SELECT * FROM clientes WHERE Categoria_de_renta = "Empleado"' # Consulta SQL para filtrar por categoría de renta

consulta = pd.read_sql(sql = text(query), con = engine.connect()) # Ejecutar la consulta SQL y cargar los resultados en un DataFrame

print(consulta.head())

# Guardar el DataFrame resultante en un archivo sql

consulta.to_sql('consulta_empleados', con = engine.connect(), index=False)

nueva_consulta = pd.read_sql_table('consulta_empleados', con = engine.connect())
print(nueva_consulta.head())

nueva_consulta2 = pd.read_sql_table('consulta_empleados', con = engine.connect(), columns=['ID_Cliente', 'Grado_estudio', 'Rendimiento_anual'])
print(nueva_consulta2.head())

query2 = 'SELECT * FROM clientes'

consulta2 = pd.read_sql(sql = text(query2), con = engine.connect())
print(consulta2.head())

# Borrando registros de la tabla clientes
from sqlalchemy.exc import SQLAlchemyError
query3 = 'DELETE FROM clientes WHERE ID_Cliente = 5008804' # Consulta SQL para eliminar un registro específico
try:
    r_set = engine.connect().execute(text(query3))   # Ejecutar la consulta SQL para eliminar el registro
    print("Registro eliminado exitosamente.")
except SQLAlchemyError as e:
    print(f"Error al eliminar el registro: {e}")
else:
    print("Registro eliminado exitosamente.", r_set.rowcount, "filas afectadas.")

nueva_consulta3 = pd.read_sql_table('clientes', con = engine.connect())
print(nueva_consulta3.head())


# Actualizando registros de la tabla clientes
query3 = 'UPDATE clientes SET Grado_estudio = "Nivel superior" WHERE ID_Cliente = 5008808' # Consulta SQL para actua;izar un registro específico
try:
    r_set = engine.connect().execute(text(query3))   # Ejecutar la consulta SQL para actualizar el registro
    print("Registro Actualizado exitosamente.")
except SQLAlchemyError as e:
    print(f"Error al actualizar el registro: {e}")
else:
    print("Registro actualizado exitosamente.", r_set.rowcount, "filas afectadas.")


nueva_consulta3 = pd.read_sql_table('clientes', con = engine.connect())
print(nueva_consulta3.head())

inspector = inspect(engine)
print(inspector.get_table_names())