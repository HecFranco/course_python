# Retorno de valores

Para comunicarse con el exterior, las funciones pueden devolver valores al proceso principal gracias a la instrucción `return`.

En el momento de devolver un valor, la ejecución de la función finalizará:

```python
def test():
    return "Una cadena retornada"
​test()
# 'Una cadena retornada'
```

Los valores devueltos se tratan como valores literales directos del tipo de dato retornado:

```python
def test():
    return "Una cadena retornada"
print(test())
# Una cadena retornada
c = test()
print(c)
# Una cadena retornada
c = test() + 10
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-6-0ac9d7015445> in <module>()
# ----> 1 c = test() + 10
# TypeError: Can't convert 'int' object to str implicitly
```

Éso incluye cualquier tipo de colección:

```python
def test():
    return [1,2,3,4,5]
​print(test())
# [1, 2, 3, 4, 5]
print(test()[-1])
# 5
print(test()[1:4])
# [2, 3, 4]
l = test()
l[-1]
# 5
```

[Volver al inicio](#-retorno-de-valores)

## RETORNO MÚLTIPLE

---------------------------------------------------------------------------

Una característica interesante, es la posibilidad de devolver múltiples valores separados por comas.

```python
def test():
    return "Una cadena",20,[1,2,3]
​test()
# ('Una cadena', 20, [1, 2, 3])
```

Éstos valores se tratan en conjunto como una tupla inmutable y se pueden reasignar a distintas variables:

```python
c,n,l = test()
c
# 'Una cadena'
n
# 20
l
# [1, 2, 3]
```

[Volver al inicio](#-retorno-de-valores)