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

## EL EJERCICIO

### PREPARACIÓN

1. Crea una clase llamada Punto con sus dos coordenadas `X` e `Y`.

2. Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.

```python
class Punto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
```

3. Sobreescribe el método `string`, para que al imprimir por pantalla un punto aparezca en formato `(X,Y)`

```diff
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
++  def __str__(self):
++      return "({}, {})".format(self.x, self.y)
```

4. Añade un método llamado `cuadrante` que indique a qué cuadrante pertenece el punto, o si es el origen.

```diff
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
++  def cuadrante(self):
++      if self.x > 0 and self.y > 0:
++          print("{} pertenece al primer cuadrante".format(self))
++      elif self.x < 0 and self.y > 0:
++          print("{} pertenece al segundo cuadrante".format(self))
++      elif self.x < 0 and self.y < 0:
++          print("{} pertenece al tercer cuadrante".format(self))
++      elif self.x > 0 and self.y < 0:
++          print("{} pertenece al cuarto cuadrante".format(self))
++      else:
++          print("{} se encuentra sobre el origen".format(self))        
```

5. Añade un método llamado `vector`, que tome otro punto y calcule el vector resultante entre los dos puntos.

```diff
class Punto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))
            
++  def vector(self, p):
++      print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y) )
```

6. (Optativo) Añade un método llamado `distancia`, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

```diff
++ import math

class Punto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))
            
    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y) )
        
++  def distancia(self, p):
++      d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
++      print("La distancia entre los puntos {} y {} es {}".format(self, p, d))
```

> **NOTA**: La función raíz cuadrada en Python `sqrt()` se debe importar del módulo `math` y utilizarla de la siguiente forma:

```python
import math
math.sqrt(9)
# 3.0
```

7. Crea una clase llamada `Rectangulo` con dos puntos (inicial y final) que formarán la diagonal del rectángulo.

8. Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.

```python
class Rectangulo:
    
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
```

9. Añade al rectángulo un método llamado `base` que muestre la base.

```diff
class Rectangulo:

    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal

++  def base(self):
++      self.base = abs(self.pFinal.x - self.pInicial.x)
++      print("La base del rectángulo es {}".format( self.base ) )
```

10. Añade al rectángulo un método llamado `altura` que muestre la altura.

> **NOTA**: Puedes identificar fácilmente estos valores si intentas dibujar el cuadrado a partir de su diagonal. Si andas perdido, prueba de dibujarlo en un papel, ¡seguro que lo verás mucho más claro! Además recuerda que puedes utilizar la función `abs()` para saber el valor absolute de un número.

```diff
class Rectangulo:

    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal

    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        print("La base del rectángulo es {}".format( self.base ) )

++  def altura(self):
++      self.altura = abs(self.pFinal.y - self.pInicial.y)
++      print("La altura del rectángulo es {}".format( self.altura ) )
```

11. Añade al rectángulo un método llamado `area` que muestre el area.

```diff
class Rectangulo:

    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal

    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        print("La base del rectángulo es {}".format( self.base ) )

    def altura(self):
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        print("La altura del rectángulo es {}".format( self.altura ) )
        
++  def area(self):
++      self.base = abs(self.pFinal.x - self.pInicial.x)
++      self.altura = abs(self.pFinal.y - self.pInicial.y)
++      self.area = self.base * self.altura
++      print("El área del rectángulo es {}".format( self.area ) )
```

### PREPARACIÓN

12. Crea los puntos `A(2, 3)`, `B(5,5)`, `C(-3, -1)` y `D(0,0)` e imprimelos por pantalla.

```diff
import math

class Punto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))
            
    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y) )
        
    def distancia(self, p):
        d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))
        

class Rectangulo:
    
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
        
    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        print("La base del rectángulo es {}".format( self.base ) )
        
    def altura(self):
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        print("La altura del rectángulo es {}".format( self.altura ) )
        
    def area(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        self.area = self.base * self.altura
        print("El área del rectángulo es {}".format( self.area ) )

++ A = Punto(2,3)
++ B = Punto(5,5)
++ C = Punto(-3, -1)
++ D = Punto(0,0)
```

13. Consulta a que cuadrante pertenecen el punto `A`, `C` y `D`.

```diff
import math

class Punto:
# ...
        
class Rectangulo:
# ...

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

++ A.cuadrante()
++ C.cuadrante()
++ D.cuadrante()
```

14. Consulta los vectores `AB` y `BA`.

```diff
import math

class Punto:
# ...
        
class Rectangulo:
# ...

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

++ A.vector(B)
++ B.vector(A)
```

15. (Optativo) Consulta la distancia entre los puntos `'A y B'` y `'B y A'`.

```diff
import math

class Punto:
# ...
        
class Rectangulo:
# ...

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

++ A.distancia(B)
++ B.distancia(A)
```

16. (Optativo) Determina cual de los 3 puntos `A`, `B` o `C`, se encuentra más lejos del origen, punto `(0,0)`.

```diff
import math

class Punto:
# ...
        
class Rectangulo:
# ...

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

++ A.distancia(D)
++ B.distancia(D)
++ C.distancia(D)
```

17. Crea un rectángulo utilizando los puntos `A` y `B`.

```diff
import math

class Punto:
# ...
        
class Rectangulo:
# ...

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

++ R = Rectangulo(A, B)
```

18. Consulta la base, altura y área del rectángulo.
​
​
```diff
import math

class Punto:
# ...
        
class Rectangulo:
# ...

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = Rectangulo(A, B)
++ R.base()
++ R.altura()
++ R.area()
```