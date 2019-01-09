# BLOQUE 08

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

**En este ejercicio vas a trabajar el concepto de puntos, coordenadas y vectores sobre el plano cartesiano y cómo la programación Orientada a Objetos puede ser una excelente aliada para trabajar con ellos. No está pensado para que hagas ningún tipo de cálculo sino para que practiques la automatización de tareas.**

> **NOTA**: Creo que es un ejemplo muy interesante, punto de partida en la programación de gráficos, pero si consideras que esto no lo tuyo puedes simplemente pasar de largo. Ahora bien, debes ser consciente de que te vas a perder uno de los ejercicios más interesantes del curso.

Antes de continuar voy a explicar brevemente los conceptos básicos por si alguien necesita un repaso.

## El plano cartesiano

Representa un espacio bidimensional (en 2 dimensiones), formado por dos rectas perpendiculares, una horizontal y otra vertical que se cortan en un punto. La recta horizontal se denomina eje de las abscisas o eje `X`, mientras que la vertical recibe el nombre de eje de las ordenadas o simplemente eje `Y`. En cuanto al punto donde se cortan, se conoce como el punto de origen `O`.

Es importante remarcar que el plano se divide en 4 cuadrantes:

## Puntos y coordenadas

El objetivo de todo esto es describir la posición de puntos sobre el plano en forma de coordenadas, que se forman asociando el valor del eje de las `X` (horizontal) con el valor del eje `Y` (vertical).

La representación de un punto es sencilla: `P(X,Y)` dónde `X` y la `Y` son la distancia horizontal (izquierda o derecha) y vertical (arriba o abajo) respectivamente, utilizando como referencia el punto de origen `(0,0)`, justo en el centro del plano.

## Vectores en el plano

Finalmente, un vector en el plano hace referencia a un segmento orientado, generado a partir de dos puntos distintos.

A efectos prácticos no deja de ser una línea formada desde un punto inicial en dirección a otro punto final, por lo que se entiende que un vector tiene longitud y dirección/sentido.

En esta figura, podemos observar dos puntos A y B que podríamos definir de la siguiente forma:

```python
A(x1, y1) => A(2, 3)
B(x2, y2) => B(5, 5)
```

Y el vector se representaría como la diferencia entre las coordendas del segundo punto respecto al primero (el segundo menos el primero):

```python
AB = (x2-x1, y2-y1) => (5-2, 5-3) => (3,2)
```

Lo que en definitiva no deja de ser: `3` a la derecha y `2` arriba.

Y con esto finalizamos este mini repaso.
