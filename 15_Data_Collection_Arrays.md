# Colección de Datos - Conjuntos

Son colecciones desordenadas de elementos únicos utilizados para hacer pruebas de pertenencia a grupos y eliminación de elementos duplicados.

```python
conjunto = set()
conjunto
# set()
conjunto = {1,2,3}
conjunto
# {1, 2, 3}
```

[Volver al inicio](#-colección-de-datos---conjuntos)

## MÉTODO ADD()

---------------------------------------------------------------------------

El método `add()`, sirve para añadir elementos al conjunto. Si un elemento ya se encuentra, no se añadirá de nuevo.

```python
conjunto = {1,2,3}
conjunto.add(4)
conjunto
# {1, 2, 3, 4}
conjunto.add(0)
conjunto
# {0, 1, 2, 3, 4}
```

[Volver al inicio](#-colección-de-datos---conjuntos)

## COLECCIONES DESORDENADAS

---------------------------------------------------------------------------

Se dice que son desordenados porque gestionan automáticamente la posición de sus elementos, en lugar de conservarlos en la posición que nosotros los añadimos.

```python
conjunto.add('H')
conjunto
# {0, 1, 2, 3, 4, 'H'}
conjunto.add('A')
conjunto.add('Z')
conjunto
# {0, 1, 2, 3, 4, 'A', 'Z', 'H'}
```

[Volver al inicio](#-colección-de-datos---conjuntos)

## PERTENENCIA A GRUPOS CON IN

---------------------------------------------------------------------------

Podemos conocer la pertenencia a grupos con el método `in`.

```python
grupo = {'Hector','Juan','Mario'}
'Hector' in grupo
# True
'Maria' in grupo
# False
'Hector' not in grupo
# False
```

[Volver al inicio](#-colección-de-datos---conjuntos)

## AUTOELIMINACIÓN DE ELEMENTOS DUPLICADOS

---------------------------------------------------------------------------

Auto-eliminación de elementos duplicados

```python
test = {'Hector','Hector','Hector'}
test
# {'Hector'}
```

[Volver al inicio](#-colección-de-datos---conjuntos)

## CAST DE LISTA A CONJUNTO Y VICEVERSA

---------------------------------------------------------------------------

> **NOTA**: El término ***Cast** se conoce como la conversión/transformación de una variable de un tipo a otro tipo distinto.

Es muy útil transformar listas a conjuntos para borrar los elementos duplicados automáticamente.

```python
l = [1,2,3,3,2,1]
l
# [1, 2, 3, 3, 2, 1]
c = set(l)
c
# {1, 2, 3}
l = list(c)
l
# [1, 2, 3]
l = [1,2,3,3,2,1]
```

> **NOTA**: Podemos realizar esta operación en una sola línea.

```python
l = [1,2,3,3,2,1]
l = list( set( l ) )
l
# [1, 2, 3]
```

[Volver al inicio](#-colección-de-datos---conjuntos)

## CAST DE CADENA A CONJUNTO

---------------------------------------------------------------------------

> **NOTA**: El término ***Cast** se conoce como la conversión/transformación de una variable de un tipo a otro tipo distinto.

Sirve para crear un conjunto con todos los caracteres de la cadena.

```python
s = "Al pan pan y al vino vino"
set(s)
# {' ', 'A', 'a', 'i', 'l', 'n', 'o', 'p', 'v', 'y'}
```

[Volver al inicio](#-colección-de-datos---conjuntos)