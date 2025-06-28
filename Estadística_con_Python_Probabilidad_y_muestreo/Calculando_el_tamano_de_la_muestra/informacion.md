# Calculando el tamaño de la muestra

El valor promedio gastado por los clientes en una tienda es de $ 45.50. Suponiendo que la desviación estándar de los gastos es de $ 15.00, ¿cuál debería ser el tamaño de la muestra para estimar la media de la población con un nivel de significancia del 10%?

Tenga en cuenta que el error máximo aceptable es del 10%.

Aproximadamente 29

¡Alternativa correcta! Aquí está el código de la solución:
```python
from scipy.stats import norm

media = 45.5
sigma = 15
significancia = 0.10
confianza = 1 - significancia

z = norm.ppf(0.5 + (confianza / 2))
error_porcentual = 0.10
e = media * error_porcentual

n = (z * (sigma / e)) ** 2
n.round()
```
# Muestra de sacos de harina

Un fabricante de harina encontró que, en una muestra aleatoria compuesta por 200 sacos de 25 kg de un lote compuesto por 2000 sacos, mostraba una desviación estándar muestral del peso igual a 480 g.

Considerando un error máximo asociado con el promedio poblacional de 0.3 kg y un nivel de confianza del 95%, ¿qué tamaño de muestra debe seleccionarse para obtener una estimación confiable del parámetro poblacional?

Aproximadamente 10 bolsas

¡Alternativa correcta! Siempre recordando comprobar las unidades de medida de error, media y desviación estándar. Aquí está el código propuesto para la solución:
```python
from scipy.stats import norm

N = 2000
z = norm.ppf(0.5 + (0.95 / 2))
s = 480
e = 0.3 * 1000   # Convirtiendo kg para g

n = ((z**2) * (s**2) * (N)) / (((z**2) * (s**2)) + ((e**2) * (N - 1)))
int(n.round())
```

# Lo que aprendimos en esta aula:

    Determinación del tamaño de una muestra, para asegurar que sea representativa de la población
    Cálculo del tamaño de la muestra para variables cuantitativas finitas e infinitas

