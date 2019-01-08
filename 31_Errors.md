# Provocando errores

[Volver al inicio](#-provocando-errores)

## ERRORES DE SINTAXIS (SYNTAXERROR)

---------------------------------------------------------------------------

Los errores de sintaxis (SyntaxError) son los que podemos apreciar repasando el código, por ejemplo al dejarnos de cerrar un paréntesis:

```python
print("Hola"
  File "<ipython-input-1-8bc9f5174855>", line 1
    print("Hola"
# SyntaxError: unexpected EOF while parsing
```

[Volver al inicio](#-provocando-errores)

## ERRORES DE NOMBRE (NAMEERROR)

---------------------------------------------------------------------------

Los errores de nombre (NameError) se producen cuando el sistema interpreta que debe ejecutar alguna función, método... pero no lo encuentra definido:

```python
pint("Hola")
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-2-155163d628c2> in <module>()
# ----> 1 pint("Hola")
# NameError: name 'pint' is not defined
```

La mayoría de errores de sintácticos los identifica Python antes de ejecutar el código y nos avisa de que debemos arreglarlos.
Sin embargo existen otro tipo de errores que pasan más desapercibidos...

[Volver al inicio](#-provocando-errores)

## ERRORES SEMÁNTICOS

---------------------------------------------------------------------------

Los errores semánticos son muy difíciles de identificar, ya que van ligados al sentido del funcionamiento y dependen de la situación. Algunas veces pueden ocurrir y otras no.

Cuanta más experiencia como programador tengas, y más te hayas equivocado, más aprenderás a avanzarte a los errores semánticos.

Ejemplo `pop()` con lista vacía:

```python
l = [1,2,3]
l.pop()
l.pop()
l.pop()
l
# []
l.pop()
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-6-9e6f3717293a> in <module>()
# ----> 1 l.pop()
# IndexError: pop from empty list
```

Prevención utilizando comprobación con `len() > 0`

```python
l = [1,2,3]
if len(l) > 0:
    l.pop()
l
# [1, 2]
```

Ejemplo lectura de cadena por teclado y operación de resultado sin conversión a número

```python
m = 4
n = input("Introduce un número: ")
# Introduce un número: 4
print("{}/{}={}".format(n,m,n/m))
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-12-85bb893ab3e3> in <module>()
# ----> 1 print("{}/{}={}".format(n,m,n/m))
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

[Volver al inicio](#-provocando-errores)

## PREVENCIÓN CONVIRTIENDO A FLOTANTE

---------------------------------------------------------------------------

Prevención haciendo una conversión a flotante

```python
n = float(input("Introduce un número: "))
m = 4
print("{}/{}={}".format(n,m,n/m))
# Introduce un número: 10
# 10.0/4=2.5
```

Sin embargo en algunas ocasiones no podemos prevenir el error, como cuando se introduce una cadena:


```python
m = 4
n = float(input("Introduce un número: "))
print("{}/{}={}".format(n,m,n/m))
# Introduce un número: aaa
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-14-c0e7fd4a26a9> in <module>()
# ----> 1 n = float(input("Introduce un número: "))
#       2 m = 4
#       3 print("{}/{}={}".format(n,m,n/m))
# ValueError: could not convert string to float: 'aaa'
```

Para prevenir estos casos existen las **excepciones**.

Las veremos en la próxima lección.

[Volver al inicio](#-provocando-errores)