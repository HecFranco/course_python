# Métodos de las cadenas

`upper()`: Devuelve la cadena con todos sus caracteres a mayúscula

```python
"Hola Mundo".upper()
# 'HOLA MUNDO'
```

`lower()`: Devuelve la cadena con todos sus caracteres a minúscula

```python
"Hola Mundo".lower()
# 'hola mundo'
```

`capitalize()`: Devuelve la cadena con su primer carácter en mayúscula

```python
"hola mundo".capitalize()
# 'Hola mundo'
```

`title()`: Devuelve la cadena con el primer carácter de cada palabra en mayúscula

```python
"hola mundo".title()
# 'Hola Mundo'
```

`count()`: Devuelve una cuenta de las veces que aparece una subcadena en la cadena
```python
"Hola mundo".count('mundo')
# 1
```

`find()`: Devuelve el índice en el que aparece la subcadena (`-1` si no aparece)

```python
"Hola mundo".find('mundo')
# 5
"Hola mundo".find('mundoz')
# -1
```

`rfind()`: Devuelve el índice en el que aparece la subcadena, empezando por el final

```python
"Hola mundo mundo mundo".rfind('mundo')
# 17
```

`isdigit()`: Devuelve `True` si la cadena es todo números (`False` en caso contrario)

```python
c = "100"
c.isdigit()
# True
```

`isalnum()`: Devuelve `True` si la cadena es todo números o carácteres alfabéticos

```python
c2 = "ABC10034po"
c2.isalnum()
# True
```

`isalpha()`: Devuelve `True` si la cadena es todo carácteres alfabéticos

```python
c2.isalpha()
# False
"Holamundo".isalpha()
# True
```

`islower()`: Devuelve `True` si la cadena es todo minúsculas

```python
"Hola mundo".islower()
# False
```

`isupper()`: Devuelve `True` si la cadena es todo mayúsculas
```python
"Hola mundo".isupper()
# False
```

`istitle()`: Devuelve `Truev si la primera letra de cada palabra es mayúscula

```python
"Hola Mundo".istitle()
# True
```

`isspace()`: Devuelve `True` si la cadena es todo espacios

```python
"  -  ".isspace()
# False
```

`startswith()`: Devuelve `True` si la cadena empieza con una subcadena

```python
"Hola mundo".startswith("Mola")
# False
```

`endswith()`: Devuelve `True` si la cadena acaba con una subcadena

```python
"Hola mundo".endswith('mundo')
# True
```

`split()`: Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista

```python
"Hola mundo mundo".split()[0]
# 'Hola'
```

Podemos indicar el carácter a partir del que se separa:

```python
"Hola,mundo,mundo,otra,palabra".split(',')
# ['Hola', 'mundo', 'mundo', 'otra', 'palabra']
```

`join()`: Une todos los caracteres de una cadena utilizando un caracter de unión

```python
",".join("Hola mundo")
# 'H,o,l,a, ,m,u,n,d,o'

" ".join("Hola")
# 'H o l a'
```

`strip()`: Borra todos los espacios por delante y detrás de una cadena y la devuelve

```python
"   Hola mundo     ".strip()
# 'Hola mundo'
```

Podemos indicar el carácter a borrar:

```python
"-----Hola mundo---".strip('-')
# 'Hola mundo'
```

`replace()`: Reemplaza una subcadena de una cadena por otra y la devuelve

```python
"Hola mundo".replace('o','0')
# 'H0la mund0'`
```

Podemos indicar un límite de veces a reemplazar:

```python
"Hola mundo mundo mundo mundo mundo".replace(' mundo','',4)
# 'Hola mundo'
```

[Volver al inicio](#-métodos-de-las-cadenas)