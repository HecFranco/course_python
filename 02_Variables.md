# Variables

Una variable es un identificador que representa un espacio en la memoria. A este espacio se le puede asignar un valor para utilizarlo posteriormente como si se tratase de un valor literal, incluso se puede operar con otras variables y reasignarle otro valor en cualquier momento.

Las variables en **Python** al contrario que en otros lenguajes, **NO REQUIEREN DECLARACIÓN**, es decir, se puede usar directamente sin la necesidad de declararla previamente (`int n;` **JAVA**)
El tipo de las variables **puede cambiar fácilmente**, sin ningun previo aviso.

```python
n = 3
```

> **NOTA**: El lenguaje **Python** a diferencia de otros lenguajes no tiene **constantes**. Se podrían crear mediante algunos trucos, pero no es recomendable (generar **getters** y **setters**).

[Volver al inicio](#-variables)

## VARIABLES

---------------------------------------------------------------------------

Asignación de un valor a la variable 'n':

```python
n = 3
n
# 3
```

Además podemos sumar una variable entera con un literal número entero:

```python
n + 3
# 6
```

Y realizar el producto de una variable entera con un literal número entero:

```python
n * 2
# 6
```

O el producto de una variable entera con un literal número entero:

```python
n * n
# 9
```

Incluso la suma de dos variables enteras:

```python
# Creamos otra variable
m = 10
n + m
# 30
```

Producto de dos variables y suma de un literal numérico:

```python
n * m + 10
# 40
```

Reasignación de los valores y cálculo de nuevo resultado:

```python
n = 10
m = 15
n + m
# 25
```

Asignación del valor de una variable a otra:

```python
n = m
n
# 10
```

Incluso se puede asignar una operación mezclada:

```python
n = m + 10
n
# 20
```

O el propio valor sumado con un literal:

```python
n = n + 25
n
# 45
```

[Volver al inicio](#-variables)

### REUTILIZACIÓN

---------------------------------------------------------------------------

Al crear una estructura de cálculos con variables podemos fácilmente adaptar sus valores para hacer distintas comprobaciones:

```python
nota_1 = 2
nota_2 = 5
nota_media = (nota_1 + nota_2) / 2
nota_media
# 3.5
```

[Volver al inicio](#-variables)

### TIPIFICAR VARIABLES

---------------------------------------------------------------------------

Aunque **Python** presume de ser un lenguaje con unas variables bastantes flexibles, se pueden tipificar de la siguiente manera:

```python
a:int = 1
a
# 1
```

> **NOTA** se puede decir que tipifica las variables en **tiempo de ejecución**. Si podría ser interesante usar este tipo de **tipificado** cuando se trabaja de forma colectiva a modo de pistas para los compañeros.

```python
def method (a:int) -> int:
  return a
```

[Volver al inicio](#-variables)

### CASTING VARIABLES

---------------------------------------------------------------------------

En cambio **Python** si permite **forzar** variables a un formato en concreto para su trabajo, a esto se le llama **casting**. De esta manera evitamos encontrarnos con formatos de variables no deseados que conlleven errores en la ejecución de nuestro código.

```python
a='a'
a=10.2
print(a)
# 10.2
print(int(a))
# 10
```

[Volver al inicio](#-variables)

### BOOLEAN

---------------------------------------------------------------------------

Aunque **python** no contempla como tal el tipo **booleano**, si permite el uso de palabras reservadas en la asiganción de variables, tales como `True` y `False`. Hay que tener en cuenta que estas palabras reservadas sólo seran reconocidas como **Sentence Case**

```python
a=True
a
# True
b=False
b
# False
```

[Volver al inicio](#-variables)