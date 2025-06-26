# Un poco de teoría

Sobre las poblaciones, califique las siguientes afirmaciones:

1) Cuando se pueden contabilizar los elementos de una población, pero tienen una cantidad muy grande, se supone que la población es infinita.

2) Los estudios que involucren poblaciones infinitas deben realizarse utilizando muestras.

3) Una muestra es cualquier subconjunto de una población.

¿Cuáles son las correctas?

Sólo las afirmaciones 1 y 2 son correctas

¡Alternativa correcta! Las muestras son subconjuntos representativos de una población.

# Seleccionando una muestra

Teniendo en cuenta el ejemplo visto en clase, marque la forma correcta de obtener una muestra aleatoria simple de nuestro dataset datos.

Para este problema, considere que queremos una muestra de tamaño 1000.

muestra = datos.sample(1000)

¡Alternativa correcta! Perfecto, en clase usamos el parámetro random_state, que es la semilla para el generador de números aleatorios (utilícelo si desea repetir el proceso y mantener la misma muestra seleccionada).

#  Un poco más de teoría

Evalúe las alternativas a continuación y marque las correctas.



En el muestreo por conglomerados, los subgrupos separados de la población no necesitan ser homogéneos.

¡Alternativa correcta! Un ejemplo muy común de la aplicación de este tipo de técnica es la división de la población en grupos territoriales, donde los elementos investigados tendrán características bastante variadas.

El requisito fundamental para un proceso de muestreo aleatorio simple es que cada miembro de la población tenga las mismas posibilidades de ser seleccionado para formar parte de la muestra.

¡Alternativa correcta! Usando pandas, podemos hacer la selección de una muestra aleatoria simple con el método sample() de pandas DataFrame.

# Lo que aprendimos en esta aula:

    Los conceptos de población y muestra
    La identificación de poblaciones finitas e infinitas
    Cuándo utilizar la técnica de muestreo en un estudio
    Técnicas de selección de muestras, como:
        Muestreo aleatorio simple
        Muestreo estratificado
        Muestreo por conglomerados

