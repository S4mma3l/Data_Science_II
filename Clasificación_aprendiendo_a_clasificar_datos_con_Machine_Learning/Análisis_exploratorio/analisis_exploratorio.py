import pandas as pd

datos = pd.read_csv('Clasificación_aprendiendo_a_clasificar_datos_con_Machine_Learning\\Análisis_exploratorio\\datos\\marketing_inversiones.csv')

print(datos.head())
print(datos.info())
print(datos.describe())

# analizar como se encuentran los datos
import plotly.express as px

fig1 = px.histogram(datos, x='adherencia_inversion', text_auto=True)
fig2 =px.histogram(datos, x='estado_civil', text_auto=True, color='adherencia_inversion')
fig3 =px.histogram(datos, x='escolaridad', text_auto=True, color='adherencia_inversion')
fig4 =px.histogram(datos, x='default', text_auto=True, color='adherencia_inversion', barmode='group')
fig5 =px.histogram(datos, x='prestatario', text_auto=True, color='adherencia_inversion', barmode='group')


# fig5.show()

# analizar las varibles numericas

fig6 =px.box(datos, x='edad', color='adherencia_inversion')
fig7 =px.box(datos, x='saldo', color='adherencia_inversion')
fig8 =px.box(datos, x='ultimo_contacto', color='adherencia_inversion')
fig9 =px.box(datos, x='ct_contactos', color='adherencia_inversion')


fig9.show()