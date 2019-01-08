# Listas

Las listas son un tipo compuesto de dato que puede almacenar distintos valores (llamados **ítems**) ordenados entre `[ ]` y separados con comas, `, `.

[Volver al inicio](#-listas)

## DEFINIR UNA LISTA

---------------------------------------------------------------------------

```python
numeros = [1,2,3,4]
datos = [4,"Una cadena",-15,3.14,"Otra cadena"]
```

> **NOTA**: Además podemos crear una lista usando el método `list()` el cual admite un sólo argumento. Por lo que deberemos incluir dentro el listado entre corchetes.

```python
list(1,2,3,4)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: list expected at most 1 arguments, got 4
numeros = list([1,2,3,4])
```

Además podemos generar una lista a partir de un **string**:

```python
text = list("ricardo")
text
# ['r', 'i', 'c', 'a', 'r', 'd', 'o']
text_2 = list("youtube es genial")
text_2
# ['y', 'o', 'u', 't', 'u', 'b', 'e', ' ', 'e', 's', ' ', 'g', 'e', 'n', 'i', 'a', 'l']
```

[Volver al inicio](#-listas)

### MÉTODO SPLIT()

---------------------------------------------------------------------------

El método `.split()` permite convertir un **string** en lista utilizando como delimitador el espacio ` `.

```python
text = "youtube es genial".split()
text
# ['youtube', 'es', 'genial']
```

Podemos cambier el limitador por otro caracter distinto:

```python
comida_favorita = "pizza, spaguetti, lentejas"
comida_favorita.split(', ')
# ['pizza', 'spaguetti', 'lentejas']
```

[Volver al inicio](#-listas)

### MÉTODO JOIN()

---------------------------------------------------------------------------

Este método pertenece a las cadenas (**String**) y permite unir una lista usando un caracter designado:

```python
comida_favorita = ['pizza', 'spaguetti', 'lentejas']
', '.join(comida_favorita)
# 'pizza, spaguetti, lentejas'
"Mi comida favorita es: " + ', '.join(comida_favorita)
# 'Mi comida favorita es: pizza, spaguetti, lentejas'
```

## ÍNDICES Y SLICING

---------------------------------------------------------------------------

Los **índices** y **slicings** funcionan de una forma muy similar a las cadenas de caracteres.

```python
datos = [4,"Una cadena",-15,3.14,"Otra cadena"]
datos[0]
# 4
datos[-1]
# 'Otra cadena'
datos[-2:]
# [3.14, 'Otra cadena']
```

[Volver al inicio](#-listas)

## SUMA DE LISTAS

---------------------------------------------------------------------------

La **Suma de listas** da como resultado una nueva lista que incluye todos los ítems.

```python
numeros = [1,2,3,4]
numeros + [5,6,7,8]
# [1, 2, 3, 4, 5, 6, 7, 8]
numeros = numeros + [1,2,3,4]
numeros
# [1, 2, 3, 4, 1, 2, 3, 4]
```

> **NOTA**: Podemos usar la siguiente nomenclatura para sumar listas:

```python
numeros = [1,2,3,4]
numeros + [5,6,7,8]
# [1, 2, 3, 4, 5, 6, 7, 8]
numeros += [1,2,3,4]
numeros
# [1, 2, 3, 4, 1, 2, 3, 4]
```


[Volver al inicio](#-listas)

## MULTIPLICAR LISTAS

---------------------------------------------------------------------------

Podemos "multiplicar" o repetir listas de la siguiente manera:

```python
numeros = [1,2,3,4]
numeros * 2
# [1, 2, 3, 4, 1, 2, 3, 4]
```

[Volver al inicio](#-listas)

## MODIFICAR LISTAS

---------------------------------------------------------------------------

> **NOTA**: **Son modificables**, a diferencia de las cadenas, en las listas sí podemos modificar sus ítems utilizando índices:

```python
pares = [0,2,4,5,8,10]
pares[3]= 6
pares
# [0, 2, 4, 6, 8, 10]
```

[Volver al inicio](#-listas)

### MÉTODO .APPEND()

---------------------------------------------------------------------------

Las listas integran funcionalidades internas, como el método `.append()` para añadir un ítem al final de la lista.

```python
pares = [0,2,4,5,8,10]
pares.append(12)
pares
# [0, 2, 4, 5, 8, 10, 12]
pares.append(7*2)
pares
# [0, 2, 4, 5, 8, 10, 12, 14]
```

> **NOTA**: El método `.append()` sólo admite un argumento. 

```python
pares = [0,2,4,5,8,10]
pares.append(12, 2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: append() takes exactly one argument (2 given)
```

[Volver al inicio](#-listas)

### MÉTODO .EXTEND()

---------------------------------------------------------------------------

Si quiseramos añadir más argumentos deberíamos usar el método `.extend()`.

```python
pares = [0,2,4,5,8,10]
pares.extend([7, 8])
pares
# [0, 2, 4, 5, 8, 10, 7, 8]
```

[Volver al inicio](#-listas)

### MÉTODO .REMOVE()

---------------------------------------------------------------------------

Si quisieramos quitar un elemento de la lista usaremos el método `.remove(8)`.

> **NOTA**: Con `.remove()` eliminamos el elemento y no la posición al contrario de en otros lenguajes.

```python
pares = [0,2,4,5,8,10]
pares.remove(8)
pares
# [0, 2, 4, 5, 10,]
```

[Volver al inicio](#-listas)

### MÉTODO .INDEX()

---------------------------------------------------------------------------

Utilizamos el método `.index()` para poder localizar la posición de un elemnto dentro de una lista:

```python
pares = [0,2,4,5,8,10]
pares.index(8)
# 4
```

> **NOTA**: Las posiciones en las listas empiezan desde `0`.

[Volver al inicio](#-listas)

### MÉTODO DEL

---------------------------------------------------------------------------

Utilizamos el método `del` para eliminar variables **enteras**.

> **NOTA**: `del` pertenece al listado de palabras reservadas del lenguaje **Python**

```python
vocales = "aeiou"
lista_vocales = list(vocales)
lista_vocales
# ['a', 'e', 'i', 'o', 'u']
del lista_vocales
lista_vocales
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'lista_vocales' is not defined
```

Además podemos eliminar parte de una lista usando el método `del`.

```python
vocales = "aeiou"
lista_vocales = list(vocales)
lista_vocales
# ['a', 'e', 'i', 'o', 'u']
del lista_vocales[1]
lista_vocales
# ['a', 'i', 'o', 'u']
```

> **NOTA**: Las posiciones en las listas empiezan desde `0`.
> **IMPORTANTE**: El método `del`devolvería un error al tratar de ejecuarlo en una cadena, ya que las mismas son inmutables:

```python
vocales = "aeiou"
del vocales[1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object doesn't support item deletion
```

[Volver al inicio](#-listas)

### MÉTODO IN

---------------------------------------------------------------------------

Utilizamos el método `in` para saber si un elemento se encuentra dentro de una lista.

> **NOTA**: `in` pertenece al listado de palabras reservadas del lenguaje **Python**

```python
alfabeto = ['a', 'e', 'i', 'o', 'u']
"a" in alfabeto
# True
if "a" in vocales:
  print("existe la vocal")
```

[Volver al inicio](#-listas)

### SLICING 

---------------------------------------------------------------------------

Y una peculiaridad, es que también aceptan asignación con **slicing** para modificar varios ítems en conjunto

```python
letras = ['a','b','c','d','e','f']
letras[:3]
# ['a', 'b', 'c']
letras[:3] = ['A','B','C']
letras
# ['A', 'B', 'C', 'd', 'e', 'f']
```

> **NOTA**: Asignar una lista vacía equivale a borrar los ítems de la lista o sublista

```python
letras = ['a','b','c','d','e','f']
letras[:3] = []
letras
# ['d', 'e', 'f']
letras = []
letras
# []
```

[Volver al inicio](#-listas)

## LONGITUD DE UNA LISTA

---------------------------------------------------------------------------

La función `len()` también funciona con las listas del mismo modo que en las cadenas:

```python
letras = ['a','b','c','d','e','f']
len(letras)
# 0
pares = [0, 2, 4, 5, 8, 10, 12, 14]
len(pares)
# 8
```

[Volver al inicio](#-listas)

## LISTAS DENTRO DE LISTAS (ANIDADAS)

---------------------------------------------------------------------------

Podemos manipular fácilmente este tipo de estructuras utilizando múltiples índices, como si nos refieréramos a las filas y columnas de una tabla.

```python
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
r
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r[0]  # Primera sublista
# [1, 2, 3]
r[-1]  # Última sublista
# [7, 8, 9]
r[0][0]  # Primera sublista, y de ella, primer ítem
# 1
r[1][1]  # Segunda sublista, y de ella, segundo ítem
# 5
r[2][2]  # Tercera sublista, y de ella, tercer ítem
# 9
r[-1][-1]  # Última sublista, y de ella, último ítem
# 9
```

[Volver al inicio](#-listas)

# RETO

---------------------------------------------------------------------------

**Partiendo de la siguiente cadena en minúsculas, `vocales = "aeiou"`, imprimir en pantalla las vocales en mayúsculas.**