# BLOQUE 06

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

**1) Realiza una función llamada `area_rectangulo()` que devuelva el área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura.**

> **NOTA**: El área de un rectángulo se obtiene al multiplicar la base por la altura.
​
**PASOS A SEGUIR**

1. Creamos nuestro método `area_rectangulo()`.

```python
# Completa el ejercicio aquí
def area_rectangulo(base, altura):
    return base*altura
```

2. Impirmimos el resultado de la función:

```diff
# Completa el ejercicio aquí
def area_rectangulo(base, altura):
    return base*altura

++ print( area_rectangulo(15,10) )
```

El código final será así:

```python
# Completa el ejercicio aquí
def area_rectangulo(base, altura):
    return base*altura

print( area_rectangulo(15,10) )
```

**2) Realiza una función llamada `area_circulo()` que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:**

> **NOTA**: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor `3.14159` como pi o importarlo del módulo math:

```python
import math
print(math.pi)
> 3.1415...
```

**PASOS A SEGUIR**

1. Cargamos la librería `math`:

```python
# Completa el ejercicio aquí
import math
```

2. Creamos nuestro método `area_circulo(radio)`.

```diff
# Completa el ejercicio aquí
import math

++ def area_circulo(radio):
++     return (radio**2) * math.pi
```

3. Impirmimos el resultado de la función:

```diff
# Completa el ejercicio aquí
import math

def area_circulo(radio):
    return (radio**2) * math.pi

++ print( area_circulo(5) )    
```

El código final será así:

```python
# Completa el ejercicio aquí
import math

def area_circulo(radio):
    return (radio**2) * math.pi

print( area_circulo(5) )
```
​
**3) Realiza una función llamada `relacion()` que a partir de dos números cumpla lo siguiente:**

* **Si el primer número es mayor que el segundo, debe devolver 1.**
* **Si el primer número es menor que el segundo, debe devolver -1.**
* **Si ambos números son iguales, debe devolver un 0.**
**Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'**

**PASOS A SEGUIR**

1. Creamos nuestro método `relacion(a, b)`.

```python
# Completa el ejercicio aquí
def relacion(a, b):
    if a > b: 
        return 1
    elif a < b:
        return -1
    else:
        return 0
```

2. Imprimimos el resultado de la función:

```diff
# Completa el ejercicio aquí
def relacion(a, b):
    if a > b: 
        return 1
    elif a < b:
        return -1
    else:
        return 0

++ print( relacion(5, 10) )
++ print( relacion(10, 5) )
++ print( relacion(5, 5) )
```

El código final será así:

```python
# Completa el ejercicio aquí
def relacion(a, b):
    if a > b: 
        return 1
    elif a < b:
        return -1
    else:
        return 0
    
print( relacion(5, 10) )
print( relacion(10, 5) )
print( relacion(5, 5) )
```

**4) Realiza una función llamada `intermedio()` que a partir de dos números, devuelva su punto intermedio:**

> **NOTA**: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

**Comprueba el punto intermedio entre -12 y 24**

El código final será así:

```python
# Completa el ejercicio aquí
def intermedio(a, b):
    return (a + b) / 2

print( intermedio(-12, 24) )
```

**5) Realiza una función llamada `recortar()` que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:**

* **Devolver el límite inferior si el número es menor que éste**
* **Devolver el límite superior si el número es mayor que éste.**
* **Devolver el número sin cambios si no se supera ningún límite.**
**Comprueba el resultado de recortar 15 entre los límites 0 y 10**

El código final será así:

```python
# Completa el ejercicio aquí
def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero

print( recortar(15, 0, 10) )
```

**6) Realiza una función `separar()` que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:**

Por ejemplo:

```python
pares, impares = separar([6,5,2,1,7])
print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]
```

> **NOTA**: Para ordenar una lista automáticamente puedes usar el método `.sort()`.

```python
numeros = [-12, 84, 13, 20, -33, 101, 9]
```

**PASOS A SEGUIR**

1. Cargamos nuestro array:

```python
numeros = [-12, 84, 13, 20, -33, 101, 9]
# Completa el ejercicio aquí
```

2. Incluimos el método con la lógica:

```diff
numeros = [-12, 84, 13, 20, -33, 101, 9]
# Completa el ejercicio aquí
++ def separar(lista):
++     numeros.sort()
++     pares = []
++     impares = []
++     for n in numeros:
++         if n%2 == 0:
++             pares.append(n)
++         else:
++             impares.append(n)
++     return pares, impares
```

3. Incluimos la impresión de los distintos casos:

```diff
numeros = [-12, 84, 13, 20, -33, 101, 9]

# Completa el ejercicio aquí

def separar(lista):
    numeros.sort()
    pares = []
    impares = []
    for n in numeros:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares
++ pares, impares = separar(numeros)
++ print(pares)
++ print(impares)
```

El código final será así:

```python
numeros = [-12, 84, 13, 20, -33, 101, 9]

# Completa el ejercicio aquí

def separar(lista):
    numeros.sort()
    pares = []
    impares = []
    for n in numeros:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

pares, impares = separar(numeros)
print(pares)
print(impares)
```