import pandas as pd

# Leer un archivo HTML
peliculas = pd.read_html('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\\Leyendo_paginas_en_HTML_e_XML\\data\\peliculas_wikipedia.html')[1]

# Imprimir el número de tablas encontradas
print(peliculas)

top_peliculas = peliculas

print(top_peliculas.head())

top_peliculas.to_html('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\\Leyendo_paginas_en_HTML_e_XML\\data\\top_peliculas.html', index=False)


# Leer un archivo xml
peliculas_xml = pd.read_xml('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\\Leyendo_paginas_en_HTML_e_XML\\data\\imdb_top_1000.xml')

# Imprimir el número de tablas encontradas
print(peliculas_xml)

peliculas_xml.to_xml('Pandas_E_S_trabajando_con_diferentes_formatos_de_archivo\\Leyendo_paginas_en_HTML_e_XML\\data\\peliculas_xml.xml', index=False)