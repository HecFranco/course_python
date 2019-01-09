# Cadenas de Caracteres

En programación, una cadena de caracteres, palabras, ristra de caracteres o frase (string, en inglés) es una secuencia ordenada (de longitud arbitraria, aunque finita) de elementos que pertenecen a un cierto lenguaje formal o alfabeto análogas a una fórmula o a una oración.

[Volver al inicio](#-cadena-de-caracteres)

## DEFINIR UNA CADENA

---------------------------------------------------------------------------

Una cadena de caracteres puede definirse encerrandola entre comillas dobles, `""`, o simples, `''`.

```python
'Hola Mundo'
# 'Hola Mundo'
"Hola Mundo"
# 'Hola Mundo'
"""Hola Mundo"""
# 'Hola Mundo'
```

**¿Como podemos incluir comillas dentro de nuestras cadenas de caracteres?**

```python
'Este texto incluye unas " " '
# 'Este texto incluye unas " " '
"Esta 'palabra' se encuentra escrita entre comillas simples"
# "Esta 'palabra' se encuentra escrita entre comillas simples"
```

También podemos usar caracteres de escape, `\`.

```python
"Esta \"palabra\" se encuentra escrita entre comillas dobles"
# 'Esta "palabra" se encuentra escrita entre comillas dobles'
'Esta \'palabra\' se encuentra escrita entre comillas dobles'
# "Esta 'palabra' se encuentra escrita entre comillas dobles"
```

[Volver al inicio](#-cadena-de-caracteres)

### FUNCIÓN PRINT()

---------------------------------------------------------------------------

Es una instrucción que nos permite mostrar correctamente el valor de una cadena (u otros valores/variables) por pantalla.

```python
print("Una cadena")
# Una cadena
print('otra cadena')
# otra cadena
print('otra cadena más')
# otra cadena más
```

Además podemos escribir cadenas que contenga diferentes variables de la siguiente manera:

```python
a = '10'
b = "10"
c = "Jose"
print('Tengo {} y quierp {} manzanas, me llamo {}'.format(a,b,c))
```

> **NOTA**: 
Acepta carácteres especiales como las tabulaciones `/t` o los saltos de línea `/n`

```python
print("Un texto\tuna tabulación")
# Un texto	una tabulación
print("Un texto\nuna nueva línea")
# Un texto
# una nueva línea
```

[Volver al inicio](#-cadena-de-caracteres)

### CADENA CRUDA

---------------------------------------------------------------------------

Para evitar los carácteres especiales, debemos indicar que una **cadena es cruda** (**raw**)

```python
print("C:\nombre\directorio")
# C:
# ombre\directorio
print(r"C:\nombre\directorio")  # r => raw (cruda)
# C:\nombre\directorio
```

[Volver al inicio](#-cadena-de-caracteres)

### CADENA MULTILÍNEA

---------------------------------------------------------------------------

Podemos utilizar `"""` (**triple comillas**) para cadenas multilínea

```python
print("""Una línea
otra línea
otra línea\tuna tabulación""")
# Una línea
# otra línea
# otra línea	una tabulación
```

También es posible asignar cadenas a variables. La forma correcta de mostrarlas es con la instrucción `print()`.

```python
c = "Esto es una cadena\ncon dos líneas"
c
# 'Esto es una cadena\ncon dos líneas'
print(c)
# Esto es una cadena
# con dos líneas
```

[Volver al inicio](#-cadena-de-caracteres)

## OPERACIONES

---------------------------------------------------------------------------

Una de las operaciones de las cadenas es la concatenación (o suma de cadenas)

```python
c = "Esto es una cadena\ncon dos líneas"
c + c
# 'Esto es una cadena\ncon dos líneasEsto es una cadena\ncon dos líneas'
```

Usnado el comando `print()`, el resultado sería:

```python
c = "Esto es una cadena\ncon dos líneas"
print(c+c)
# Esto es una cadena
# con dos líneasEsto es una cadena
# con dos líneas
```

[Volver al inicio](#-cadena-de-caracteres)

### COMPONIENDO CADENAS

---------------------------------------------------------------------------

```python
s = "Una cadena" " compuesta de dos cadenas"
print(s)
# Una cadena compuesta de dos cadenas
c1 = "Una cadena"
c2 = "otra cadena"
print("Una cadena " + c2)
# Una cadena otra cadena
# También es posible utilizar la multiplicación de cadenas
```

Podemos multiplicar una cadena de caracteres de la siguiente manera:

```python
diez_espacios = " " * 10
print(diez_espacios + "un texto a diez espacios")
#          un texto a diez espacios
```

[Volver al inicio](#-cadena-de-caracteres)

### ÍNDICES EN LAS CADENAS

---------------------------------------------------------------------------

Los índices nos permiten posicionarnos en un carácter específico de una cadena.

Representan un número [índice], que empezando por el `0` indica el carácter de la primera posición, y así sucesivamente.

```python
palabra = "Python"
palabra[0] # carácter en la posición 0
# 'P'
palabra[3]
# 'h'
```

El índice negativo `-1`, hace referencia al carácter de la última posición, el `-2` al penúltimo y así sucesivamente.

```python
palabra[-1]
# 'n'
palabra[-0]
# 'P'
palabra[-2]
# 'o'
palabra[-6]
# 'P'
palabra[5]
# 'n'
```

> **NOTA**: Podemos usar el método `list()`para generar una lista a partir de un string.

```python
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
alfabeto_lista = list(alfabeto)
alfabeto_lista
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

[Volver al inicio](#-cadena-de-caracteres)

### MÉTODO .INDEX()

---------------------------------------------------------------------------

Utilizamos el método `.index()` para poder localizar la posición de un elemnto dentro de una cadena:

```python
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
alfabeto.index('c')
# 2
```

> **NOTA**: Las posiciones en las listas empiezan desde `0`.
> **IMPORTANE**: En caso de no encontrar el elemento buscado devolverá un error **Python**.

[Volver al inicio](#-cadena-de-caracteres)

### MÉTODO IN

---------------------------------------------------------------------------

Utilizamos el método `in` para saber si un elemento se encuentra dentro de una cadena.

> **NOTA**: `in` pertenece al listado de palabras reservadas del lenguaje **Python**

```python
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
"a" in alfabeto
# True
```

[Volver al inicio](#-cadena-de-caracteres)

### SLICING EN LAS CADENAS

---------------------------------------------------------------------------

El **slicing** es una capacidad de las cadenas que devuelve un subconjunto o subcadena utilizando dos índices [inicio:fin]:

El primer índice indica donde empieza la subcadena (se incluye el carácter).
El segundo índice indica donde acaba la subcadena (se excluye el carácter).

```python
palabra = "Python"
palabra[0:2]
# 'Py'
palabra[2:]
# 'thon'
palabra[:2]
# 'Py'
```

Si en el **slicing** no se indica un índice se toma por defecto el principio y el final (incluídos)

```python
palabra[:]
# 'Python'
palabra[:2] + palabra[2:]
# 'Python'
palabra[-2:]
# 'on'
```

> **NOTA**: Si un índice se encuentra fuera del rango de la cadena, dará **error**.

```python
palabra[99]
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-47-b31ddef6ab27> in <module>()
# ----> 1 palabra[99]
# IndexError: string index out of range
```

Pero con **slicing** ésto no pasa y simplemente se ignora el espacio hueco

```python
palabra[:99]
# 'Python'
palabra[99:]
# ''
```

[Volver al inicio](#-cadena-de-caracteres)

### INMUTABILIDAD

---------------------------------------------------------------------------

Una propiedad de las cadenas es que no se pueden modificar. Si intentamos reasignar un carácter, no nos dejará:

```python
palabra[0] = "N"
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-51-c87a9e773639> in <module>()
# ----> 1 palabra[0] = "N"
# TypeError: 'str' object does not support item assignment
```

Sin embargo, utilizando **slicing** y concatenación podemos generar nuevas cadenas fácilmente:

```python
palabra = "N" + palabra[1:]
palabra
# 'Nython'
```

[Volver al inicio](#-cadena-de-caracteres)

### FUNCIONES

---------------------------------------------------------------------------

Un ejemplo de función útil que soportan las cadenas es `len()`, que nos permite saber su longitud (el número de caracteres que contienen).

```python
palabra = "Python"
len(palabra)
# 6
```

Hay más funciones, pero las iremos descubriendo a lo largo del curso.

[Volver al inicio](#-cadena-de-caracteres)