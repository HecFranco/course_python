# Controlando el Flujo - For

Iterar significa realizar una acción varias veces. Cada vez que se repite se denomina iteración.

[Volver al inicio](#-controlando-el-flujo---for)

## RECORRIENDO UN ARRAY CON WHILE

---------------------------------------------------------------------------

Recorriendo los elementos de una lista utilizando `While`

```python
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
```

[Volver al inicio](#-controlando-el-flujo---for)

## RECORRIENDO UN ARRAY CON FOR

---------------------------------------------------------------------------

La sentencia `For`, (Para), con listas:

```python
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:  # Para [variable] en [lista]
    print(numero)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
```

[Volver al inicio](#-controlando-el-flujo---for)

## MODIFICAR ITEMS DE LA LISTA AL VUELO

---------------------------------------------------------------------------

Para asignar un nuevo valor a los elementos de una lista mientras la recorremos, podríamos intentar asignar al número el nuevo valor:

```python
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numero *= 10

numeros
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Sin embargo, ésto no funciona. La forma correcta de hacerlo es haciendo referencia al índice de la lista en lugar de la variable:

```python
indice = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    numeros[indice] *= 10
    indice+=1

numeros
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

Podemos utilizar la función `enumerate()` para conseguir el índice y el valor en cada iteración fácilmente:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
numeros
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

[Volver al inicio](#-controlando-el-flujo---for)

## FOR CON CADENAS

---------------------------------------------------------------------------

```python
cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)
# H
# o
# l
# a
#  
# a
# m
# i
# g
# o
# s
```

> **NOTA**: Debemos recordar que las cadenas son inmutables:

```python
for i,c in enumerate(cadena):
    cadena[i] = "*"
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-9-8ba888c46579> in <module>()
#       1 for i,c in enumerate(cadena):
# ----> 2     cadena[i] = "*"
# TypeError: 'str' object does not support item assignment
```

Sin embargo siempre podemos generar una nueva cadena:

```python
cadena2 = ""
for caracter in cadena:
    cadena2 += caracter * 2
cadena
# 'Hola amigos'
cadena2
# 'HHoollaa  aammiiggooss'
```

[Volver al inicio](#-controlando-el-flujo---for)

## FUNCIÓN RANGE()

---------------------------------------------------------------------------

La función `range()`, sirve para generar una lista de números que podemos recorrer fácilmente, pero no ocupa memoria porque se interpreta sobre la marcha:

```python
for i in range(10):
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
range(10)
range(0, 10)
for i in [0,1,2,3,4,5,6,7,9]:
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 9
```

> **NOTA**: Si queremos conseguir la lista literal podemos transformar el range a una lista:

```python
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Además podemos indicar el tamaño de los saltos, en el sigueinte ejemplo realizaremos un **for** en el rango de `0` a `50` con saltos de `2` unidades:

```python
for i in range (0, 50, 2):
    print(i)
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24
# 26
# 28
# 30
# 32
# 34
# 36
# 38
# 40
# 42
# 44
# 46
# 48
```

> **NOTA**: Si a ese último parámetro le colocasemos un número negativo realizaría esa operación en cada iteración con el índice.

```python
for i in range (10, 0, -1):
    print(i)
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
```

También podemos recorrer mediante el bucle `for` otros tipos de datos:

```python
datos = ['dato 1', ["dato 2"]], ["dato 3"]
for dato in datos :
    print(dato)
# ['dato 1', ['dato 2']]
# ['dato 3']
```

[Volver al inicio](#-controlando-el-flujo---for)

## FUNCIÓN BREAK

---------------------------------------------------------------------------

La instrucción `break`, sirve para "romper" la ejecución del While en cualquier momento. 

> **NOTA**: `break` pertenece al listado de palabras reservadas del lenguaje **Python**

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero > 5 :
        break
    print(numero)
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

[Volver al inicio](#-controlando-el-flujo---for)

## FUNCIÓN CONTINUE

---------------------------------------------------------------------------

La istrucción `continue`, sirve para "saltarse" la iteración actual sin romper el bucle.

> **NOTA**: `continue` pertenece al listado de palabras reservadas del lenguaje **Python**

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero == 5 :
        continue
    print(numero)
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

[Volver al inicio](#-controlando-el-flujo---for)