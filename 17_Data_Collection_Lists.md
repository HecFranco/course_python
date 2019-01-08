# Colección de Datos - Pilas y Colas con Listas

Son colecciones de elementos ordenados que únicamente permiten dos acciones:

* **Añadir un elemento a la pila**
* **Sacar un elemento de la pila**

La peculiaridad es que el último elemento en entrar es el primero en salir. En inglés se conocen como estructuras **LIFO** (Last In First Out).

[Volver al inicio](#-colección-de-datos---pilas-y-colas-con-listas)

## .APPEND()

---------------------------------------------------------------------------

Las podemos crear como listas normales y añadir elementos al final con el método `append()`:

```python
pila = [3,4,5]
pila.append(6)
pila.append(7)
pila
# [3, 4, 5, 6, 7]
```

[Volver al inicio](#-colección-de-datos---pilas-y-colas-con-listas)

## .POP()

---------------------------------------------------------------------------

Para sacar los elementos utilizaremos el método `.pop()`:

Al utilizar `pop()` devolveremos el último elemento, pero también lo borraremos. Si queremos trabajar con él deberíamos asignarlo a una variable o lo perderemos:

```python
pila.pop()
# 7
pila
# [3, 4, 5, 6]
n = pila.pop()
n
# 6
pila
# [3, 4, 5]
pila.pop()
pila.pop()
pila.pop()
# 3
pila
# []
```

> **NOTA**: Si hacemos `pop()` de una pila vacía, devolverá un error. Debemos asegurarnos siempre de que la `len()` de la pila sea mayor que `0` antes de extraer un elemento automáticamente.

```python
pila.pop()
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-14-3900970cfbef> in <module>()
# ----> 1 pila.pop()
# IndexError: pop from empty list
```

[Volver al inicio](#-colección-de-datos---pilas-y-colas-con-listas)

## LAS COLAS

---------------------------------------------------------------------------

Las colas son colecciones de elementos ordenados que únicamente permiten dos acciones:

* **Añadir un elemento a la cola**
* **Sacar un elemento de la cola**

La peculiaridad es que el primer elemento en entrar es el primero en salir. En inglés se conocen como estructuras **FIFO** (First In First Out).

Debemos importar la colección deque manualmente para crear una cola:

```python
from collections import deque
cola = deque()
cola
# deque([])
```

Podemos añadir elementos directamente pasando una lista a la cola al crearla:

```python
from collections import deque
cola = deque(['Hector','Juan','Miguel'])
cola
# deque(['Hector', 'Juan', 'Miguel'])
```

Y también utilizando el método `.append()`:

```python
cola.append('Maria')
cola.append('Arnaldo')
cola
# deque(['Hector', 'Juan', 'Miguel', 'Maria', 'Arnaldo'])
```

[Volver al inicio](#-colección-de-datos---pilas-y-colas-con-listas)

## POPLEFT() EN LUGAR DE POP()

---------------------------------------------------------------------------

A la hora de sacar los elementos utilizaremos el método `popleft()` para extraerlos por la parte izquierda (el principio de la cola). Al igual que antes, debemos asegurarnos de almacenar los elementos al sacarlos o los perderemos.

```python
from collections import deque
cola = deque(['Hector','Juan','Miguel'])
cola.popleft()
# 'Hector'
cola
# deque(['Juan', 'Miguel', 'Maria', 'Arnaldo'])
p = cola.popleft()
p
# 'Juan'
cola
# deque(['Miguel', 'Maria', 'Arnaldo'])
```

[Volver al inicio](#-colección-de-datos---pilas-y-colas-con-listas)