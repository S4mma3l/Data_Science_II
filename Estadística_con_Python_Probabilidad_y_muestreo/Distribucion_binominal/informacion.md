# Utilizando DataFrames

Con la biblioteca pandas, podemos leer conjuntos de datos en diferentes formatos y convertirlos en un DataFrame. Para un conjunto de datos en formato CSV, ¿cuál sería la función de pandas para leer estos datos?

.read_csv()

¡Alternativa correcta! Recuerde anotar el tipo de separador de columna que utiliza el archivo CSV. Por defecto, la función read_csv() usa el parámetro sep=','. Si el separador es cualquier carácter que no sea la coma, necesitaremos informar esto para la función, por ejemplo: read_csv('data.csv', sep =';')).

# Exposición de premios de Alura

Supongamos que acabamos de crear un juego de lotería llamado Exposición de Premios de Alura. En este nuevo juego, el que apuesta marca 20 números, de los 25 disponibles en el boleto, y puede ganar hasta 1 millón de pesos.

Determine el número de combinaciones posibles (espacio muestral) y la probabilidad de ganar el premio jugando solo un boleto (considere sólo quince lugares decimales).

Combinaciones = 53130

Probabilidad = 0.000018821757952

¡Alternativa correcta! El resultado anterior se puede obtener con el siguiente código:

from scipy.special import comb

combinaciones = comb(25, 20)
probabilidad = 1 / combinaciones
print(f'Combinaciones = {combinaciones:.0f} e Probabilidad = {probabilidad:0.15f}')    

Recordando que las combinaciones las obtenemos con la siguiente fórmula:

img![alt text](data/eu0hqusp.png)

#  Distribución de probabilidad binomial

Las siguientes alternativas describen las características básicas de un experimento binomial.

Marque las que sean correctas.

Solo dos resultados son posibles.

¡Alternativa correcta! Ejemplo: verdadero o falso; cara o cruz; éxito o fracaso.
Alternativa correta

Realización de n pruebas idénticas.

¡Alternativa correcta! Todas las pruebas realizadas deben tener la misma configuración.

# Lanzamiento de monedas

Una moneda perfectamente equilibrada se lanza al aire cuatro veces. Usando la distribución binomial, obtenga la probabilidad de que la moneda caiga con la cruz hacia arriba dos veces.

    Alternativa incorreta

    0.375

¡Alternativa correcta! Perfecto, tenga en cuenta que la expresión "perfectamente equilibrado" indica que la moneda utilizada es honesta, es decir, tiene la misma probabilidad de obtener cara o cruz. El siguiente código es un ejemplo de una solución:
```python
from scipy.stats import binom

p = 1 / 2  # Probabilidad de salir CRUZ
n = 4          # Total de lanzamientos
k = 2          # Total de aciertos (CRUZ hacia arriba)

binom.pmf(k, n, p)
```

# Lanzamiento de dados

Un dado perfectamente equilibrado se lanza hacia arriba diez veces. Usando la distribución binomial, obtenga la probabilidad de que los dados caigan con el número cinco hacia arriba al menos tres veces.

22.48%

¡Alternativa correcta! El siguiente código es una posible solución:
```python
from scipy.stats import binom

p = 1 / 6   # Probabilidad de salir el número CINCO
n = 10      # Total de lanzamientos

print(f'{binom.sf(2, n, p):.2%}')
```

# Lo que aprendimos

    Los conceptos básicos de la distribución binomial de probabilidad
    Identificar y resolver problemas que involucran un experimento binomial
    Obtener la probabilidad de eventos que involucran sólo dos posibilidades de resultado