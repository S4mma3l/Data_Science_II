import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.exc import SQLAlchemyError
import os # Módulo para operaciones con el sistema de archivos

# --- Configuración de la Base de Datos Local ---

# Define la ruta COMPLETA donde se creará tu base de datos SQLite.
# Usamos os.path.join para construir la ruta de forma segura.
db_directory_parts = [
    'Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo',
    'Leyendo_banco_de_datos',
    'desafio',
    'data'
]
db_base_path = os.path.join(*db_directory_parts) # Une las partes del directorio
db_file_name = 'clientes_banco.db'
db_file_path = os.path.join(db_base_path, db_file_name) # Ruta completa del archivo .db

# Asegúrate de que el directorio donde se guardará la base de datos exista.
# Si no existe, os.makedirs lo creará, incluyendo subdirectorios intermedios.
# 'exist_ok=True' evita un error si el directorio ya existe.
os.makedirs(db_base_path, exist_ok=True)

# Crea el motor de la base de datos.
# 'sqlite:///' indica el tipo de base de datos.
# db_file_path es la ruta completa al archivo de la base de datos.
# 'echo=True' mostrará todas las sentencias SQL ejecutadas en la consola (útil para depuración).
engine = create_engine(f"sqlite:///{db_file_path}", echo=True)

print(f"Base de datos SQLite creada/conectada en: {db_file_path}\n")

# --- 1. Leer Datos del Archivo CSV ---

# Define la ruta del archivo CSV de clientes.
# Esta ruta debe ser relativa al script, o una ruta absoluta si lo prefieres.
# Asumiendo que el CSV está dentro del mismo "desafio" folder.
csv_file_path = os.path.join(
    'Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo',
    'Leyendo_banco_de_datos',
    'desafio',
    'clientes_banco.csv'
)

# Carga los datos del CSV en un DataFrame de Pandas.
try:
    datos = pd.read_csv(csv_file_path)
    print("--- Primeras 5 filas del DataFrame cargado desde CSV ---")
    print(datos.head())
    print("\n--- Columnas del DataFrame CSV ---")
    print(datos.columns.tolist())
    print("-" * 50)
except FileNotFoundError:
    print(f"Error: El archivo CSV no se encontró en la ruta: {csv_file_path}")
    print("Por favor, verifica la ruta y asegúrate de que el archivo 'clientes_banco.csv' existe.")
    exit()

# --- 2. Escribir los Datos del DataFrame en la Base de Datos Local ---

# Guarda el DataFrame 'datos' en una tabla llamada 'clientes' en la base de datos.
# `index=False` evita que Pandas escriba el índice del DataFrame como una columna en la tabla SQL.
# `if_exists='replace'` reemplazará la tabla si ya existe (útil para re-ejecuciones durante el desarrollo).
with engine.connect() as connection:
    datos.to_sql('clientes', connection, index=False, if_exists='replace')
    connection.commit()
print("\nDatos del CSV escritos en la tabla 'clientes' de la base de datos.")

# Verificar que la tabla 'clientes' se ha creado
inspector = inspect(engine)
print("\n--- Tablas en la base de datos ---")
print(inspector.get_table_names())

# --- 3. Realizar Actualizaciones en la Base de Datos ---

# a) Actualizar el registro del cliente ID 6840104
cliente_id_actualizar = 6840104
nuevo_rendimiento = 300000
query_update = f'UPDATE clientes SET Rendimiento_anual = {nuevo_rendimiento} WHERE ID_Cliente = {cliente_id_actualizar}'

print(f"\n--- Realizando actualización del cliente ID: {cliente_id_actualizar} ---")
try:
    with engine.connect() as connection:
        r_set = connection.execute(text(query_update))
        connection.commit()
        print(f"Registro del cliente {cliente_id_actualizar} actualizado exitosamente.")
        print(f"Filas afectadas por la actualización: {r_set.rowcount}")
except SQLAlchemyError as e:
    print(f"Error al actualizar el registro del cliente {cliente_id_actualizar}: {e}")

# Verificación de la actualización
print(f"\n--- Verificando actualización para ID_Cliente = {cliente_id_actualizar} ---")
with engine.connect() as connection:
    consulta_verificacion = pd.read_sql(sql=text(f'SELECT ID_Cliente, Rendimiento_anual FROM clientes WHERE ID_Cliente = {cliente_id_actualizar}'), con=connection)
    print(consulta_verificacion)


# b) Eliminar el registro del cliente ID 5008809
cliente_id_eliminar = 5008809
query_delete = f'DELETE FROM clientes WHERE ID_Cliente = {cliente_id_eliminar}'

print(f"\n--- Realizando eliminación del cliente ID: {cliente_id_eliminar} ---")
try:
    with engine.connect() as connection:
        r_set = connection.execute(text(query_delete))
        connection.commit()
        print(f"Registro del cliente {cliente_id_eliminar} eliminado exitosamente.")
        print(f"Filas afectadas por la eliminación: {r_set.rowcount}")
except SQLAlchemyError as e:
    print(f"Error al eliminar el registro del cliente {cliente_id_eliminar}: {e}")

# Verificación de la eliminación
print(f"\n--- Verificando eliminación para ID_Cliente = {cliente_id_eliminar} ---")
with engine.connect() as connection:
    consulta_verificacion_delete = pd.read_sql(sql=text(f'SELECT ID_Cliente FROM clientes WHERE ID_Cliente = {cliente_id_eliminar}'), con=connection)
    print(f"Resultado de la consulta tras eliminación (debería estar vacío si se eliminó):\n{consulta_verificacion_delete}")


# c) Crear un nuevo registro de cliente
query_insert = """
INSERT INTO clientes (
    ID_Cliente, Edad, Grado_estudio, Estado_civil, Tamaño_familia,
    Categoria_de_renta, Ocupacion, Años_empleado, Rendimiento_anual,
    Tiene_carro, Vivienda
) VALUES (
    6850985, 33, 'Doctorado', 'Soltero', 1,
    'Empleado', 'TI', 2, 290000,
    0, 'Casa/Departamento propio'
)
"""
print("\n--- Creando un nuevo registro de cliente ---")
try:
    with engine.connect() as connection:
        r_set = connection.execute(text(query_insert))
        connection.commit()
        print("Nuevo registro de cliente creado exitosamente.")
        print(f"Filas afectadas por la inserción: {r_set.rowcount}")
except SQLAlchemyError as e:
    print(f"Error al crear el nuevo registro: {e}")

# Verificación de la inserción
print(f"\n--- Verificando inserción para ID_Cliente = 6850985 ---")
with engine.connect() as connection:
    consulta_verificacion_insert = pd.read_sql(sql=text('SELECT * FROM clientes WHERE ID_Cliente = 6850985'), con=connection)
    print(consulta_verificacion_insert)

# --- Consulta Final de la Tabla Clientes para ver todos los cambios ---
print("\n--- Estado final de la tabla 'clientes' después de todas las operaciones ---")
with engine.connect() as connection:
    consulta_final = pd.read_sql(sql=text('SELECT * FROM clientes'), con=connection)
    print(consulta_final.head(10))
    print(f"\nNúmero total de registros en la tabla 'clientes': {len(consulta_final)}")