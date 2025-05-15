import pandas as pd

def xlsx_a_csv(ruta_xlsx, ruta_csv):
  """
  Convierte un archivo XLSX a CSV.

  Args:
    ruta_xlsx (str): La ruta del archivo XLSX de entrada.
    ruta_csv (str): La ruta donde se guardará el archivo CSV de salida.
  """
  try:
    # Lee el archivo XLSX
    df = pd.read_excel(ruta_xlsx)

    # Guarda el DataFrame como un archivo CSV
    df.to_csv(ruta_csv, index=False, encoding='utf-8')

    print(f"El archivo '{ruta_xlsx}' ha sido convertido a '{ruta_csv}' exitosamente.")

  except FileNotFoundError:
    print(f"Error: El archivo '{ruta_xlsx}' no fue encontrado.")
  except Exception as e:
    print(f"Ocurrió un error durante la conversión: {e}")

# Ejemplo de uso:
ruta_archivo_xlsx = 'Pandas_youtube\\banco_clientes.xlsx'  # Reemplaza con la ruta de tu archivo XLSX
ruta_archivo_csv = 'Pandas_youtube\\banco_clientes.csv'    # Reemplaza con la ruta donde quieres guardar el CSV

xlsx_a_csv(ruta_archivo_xlsx, ruta_archivo_csv)