# Colección de Datos - Tuplas

Son unas colecciones parecidas a las listas, con la peculiaridad de que son inmutables. Las **Tuplas** se definen entre paréntesis `tupla = (1, 2, 3)`.

```python
tupla = (1, 2, 3, 4, 5) # Tupla de enteros
tupla1 = ('aaa', 'bbb', 'ccc') # Tupla de strings
tupla2 = (100,"Hola",[1,2,3],-50) # Tupla mixta 
tupla2
# (100, 'Hola', [1, 2, 3, 4], -50)
```

> **NOTA**: Las tuplas no permiten la variación de valores en sus elementos.

```python
tupla = (100,"Hola",[1,2,3],-50) # Tupla mixta 
tupla
# (100, 'Hola', [1, 2, 3, 4], -50)
tupla[0]
# 100
tupla[0] = 200
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# TypeError: 'tuple' object does not support item assignment
```

[Volver al inicio](#-colección-de-datos---tuplas)

## INDEXACIÓN Y SLICING

---------------------------------------------------------------------------

```python
tupla = (100,"Hola",[1,2,3],-50)
tupla[0]
# 100
tupla[-1]
# -50
tupla[2:]
# ([1, 2, 3, 4], -50)
tupla[2][-1]
# 4
```

[Volver al inicio](#-colección-de-datos---tuplas)

## INMUTABILIDAD

---------------------------------------------------------------------------

```python
tupla = (100,"Hola",[1,2,3],-50)
tupla[0] = 50
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-9-b45433b4cee9> in <module>()
# ----> 1 tupla[0] = 50
# TypeError: 'tuple' object does not support item assignment
```

[Volver al inicio](#-colección-de-datos---tuplas)

## FUNCIÓN LEN()

---------------------------------------------------------------------------

```python
tupla = (100,"Hola",[1,2,3],-50)
len(tupla)
# 4
len(tupla[2])
# 3
```

[Volver al inicio](#-colección-de-datos---tuplas)

## MÉTODOS INTEGRADOS

---------------------------------------------------------------------------

[Volver al inicio](#-colección-de-datos---tuplas)

### INDEX()

---------------------------------------------------------------------------

`index()`, sirve para buscar un elemento y saber su posición en la tupla. Da error si no se encuentra.

```python
tupla = (100,"Hola",[1,2,3],-50)
tupla.index(100)
# 0
tupla
# (100, 'Hola', [1, 2, 3], -50)
tupla.index('Hola')
# 1
tupla.index('Otro')
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-18-640d616163a2> in <module>()
# ----> 1 tupla.index('Otro')
# ValueError: tuple.index(x): x not in tuple
```

[Volver al inicio](#-colección-de-datos---tuplas)

### COUNT()

---------------------------------------------------------------------------

`count()`, sirve para contar cuantas veces aparece un elemento en una tupla.

```python
tupla = (100,"Hola",[1,2,3],-50)
tupla.count(100)
# 1
tupla.count('Algo')
# 0
tupla = (100,100,100,50,10)
tupla.count(100)
# 3
```

[Volver al inicio](#-colección-de-datos---tuplas)

### APPEND()

---------------------------------------------------------------------------

`append() ?`, al ser inmutables, las tuplas no disponen de métodos para modificar su contenido.

```python
tupla = (100,"Hola",[1,2,3],-50)
tupla.append(10)
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-23-758d195ec9d7> in <module>()
# ----> 1 tupla.append(10)
# AttributeError: 'tuple' object has no attribute 'append'
```

[Volver al inicio](#-colección-de-datos---tuplas)

## EJEMPLO COMPLEJO

---------------------------------------------------------------------------

```python
def enviar_datos():
  nombre = 'héctor'
  correo = 'test@admin.com'
  edad = 15
  ciudad = 'córdoba'
  return (nombre, correo, edad, ciudad)

def recibir_datos(datos):
  print(datos[0])
  print(datos[1])
  print(datos[2])

datos = enviar_datos()
recibir_datos(datos)
# héctor
# test@admin.com
# 15
```

[Volver al inicio](#-colección-de-datos---tuplas)

## DIFERENCIA ENTRE TUPLAS Y LISTAS 

---------------------------------------------------------------------------

* Las **tuplas** se implementan entre parénteisis en **Python**, `()`.
* Las **listas** se implementan entre corchetes en **Python**, `[]`.
* Las **tuplas** están formadas por elementos inmutables.
* Las **listas** están formadas por elementos mutables.

[Volver al inicio](#-colección-de-datos---tuplas)