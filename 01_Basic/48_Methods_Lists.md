# Métodos de las listas

`append()`: Añade un ítem al final de la lista

```python
lista = [1,2,3,4,5]
lista.append(6)
clear(): Vacía todos los ítems de una lista
lista
# [1, 2, 3, 4, 5, 6]
lista.clear()
lista
# []
```

`extend()`: Une una lista a otra

```python
l1 = [1,2,3]
l2 = [4,5,6]
​l1.extend(l2)
```

`count()`: Cuenta el número de veces que aparece un ítem

```python
l1
# [1, 2, 3, 4, 5, 6]
["Hola", "mundo", "mundo"].count("Hola")
# 1
```

`index()`: Devuelve el índice en el que aparece un ítem (error si no aparece)

```python
["Hola", "mundo", "mundo"].index("mundo")
# 1
["Hola", "mundo", "mundo"].index("mundoz")
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-1-3c3755903d17> in <module>()
# ----> 1 ["Hola", "mundo", "mundo"].index("mundoz")
# ValueError: 'mundoz' is not in list
```

`insert(indice, valor)`: Agrega un ítem a la lista en un índice específico

* **Primera posición (0)**

```python
l = [1,2,3]
l.insert(0,0)
print(l)
# [0, 1, 2, 3]
```

* **Penúltima posición (-1)**

```python
l = [5,10,15,25]
l.insert(-1,20)
print(l)
# [5, 10, 15, 20, 25]
```

* **Última posición en una lista (podemos utilizar len)**

```python
n = len(l)
l.insert(n,30)
print(l)
# [5, 10, 15, 20, 25, 30]
```

* **Una posición fuera de rango (999)**

```python
l.insert(20,999)
print(l)
# [5, 10, 15, 20, 25, 30, 999]
```

`pop()`: Extrae un ítem de la lista y lo borra

```python
l = [10,20,30,40,50]
l.pop()
# 50
print(l)
# [10, 20, 30, 40]
```

Podemos indicarle un índice con el elemento a sacar (`0` es el primer ítem)

```python
l.pop(0)
# 10
print(l)
# [20, 30, 40]
```

`remove()`: Borra un ítem de la lista directamente a partir del índice

```python
l.remove(30)
print(l)
# [20, 40]
l = [20,30,30,30,40]
l.remove(30)
print(l)
# [20, 30, 30, 40]
```

`reverse()`: Le da la vuelta a la lista actual

```python
l.reverse()
print(l)
# [40, 30, 30, 20]
```

Las cadenas no tienen el método `.reverse()` pero podemos simularlo haciendo unas conversiones...

```python
"Hola mundo".reverse()
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-58-eb5308f434bf> in <module>()
# ----> 1 "Hola mundo".reverse()
# AttributeError: 'str' object has no attribute 'reverse'
lista = list("Hola mundo")
lista
# ['H', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
lista.reverse()
lista
# ['o', 'd', 'n', 'u', 'm', ' ', 'a', 'l', 'o', 'H']
cadena = "".join(lista)
cadena
# 'odnum aloH'
```

`sort()`: Ordena automáticamente los ítems de una lista por su valor de menor a mayor

```python
lista = [5,-10,35,0,-65,100]
lista.sort()
lista
# [-65, -10, 0, 5, 35, 100]
```

Podemos utilizar el argumento `reverse=True` para indicar que la ordene del revés

```python
lista.sort(reverse=True)
lista
# [100, 35, 5, 0, -10, -65]
```

[Volver al inicio](#-métodos-de-las-listas)