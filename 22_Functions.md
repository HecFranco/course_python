# Funciones

Las funciones, son fragmentos de código que se pueden ejecutar múltiples veces. Pueden recibir y devolver información para comunicarse con el proceso principal.

[Volver al inicio](#-funciones)

## DEFINICIÓN Y LLAMADA

---------------------------------------------------------------------------

```python
def saludar():
    print("Hola! Este print se llama desde la función saludar()")
​saludar()
# Hola! Este print se llama desde la función saludar()
```

Dentro de una función podemos utilizar variables y sentencias de control:

```python
def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * {} = {}".format(i,i*5))
dibujar_tabla_del_5()
# 5 * 0 = 0
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
```

> **NOTA**: A diferencia de en otros lenguajes a la hora de nombrar funciones en **Python** se usa **snake_case** en lugar de **camelCase**.

[Volver al inicio](#-funciones)

## ÁMBITO DE LAS VARIABLES

---------------------------------------------------------------------------

Una variable declarada en una función no existe en el entrono global:

```python
def test():
    n = 10
test()
print(n)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-4-667d7c7a2c02> in <module>()
# ----> 1 print(n)
# NameError: name 'n' is not defined
```

Sin embargo, una variable declarada fuera de la función (al mismo nivel), sí que es accesible desde la función:

```python
m = 10
def test():
    print(m)
test()
# 10
```

Siempre que declaremos la variable antes de la ejecución, podemos acceder a ella desde dentro:

```python
def test():
    print(l)
#test()
l = 10
test()
# 10
```

En el caso que declaremos de nuevo una variable en la función, se creará un copia de la misma que sólo funcionará dentro de la función. Por tanto no podemos modificar una variable externa dentro de una función:

```python
def test():
    o = 5 # variable que sólo existe dentro de la función
    print(o)
test()
​o=10 # variable externa, no modificable
test()
print(o)
# 5
# 5
# 10
```

[Volver al inicio](#-funciones)

## LA INSTRUCCIÓN GLOBAL

---------------------------------------------------------------------------

Para poder modificar una variable externa en la función, debemos indicar que es global de la siguiente forma:

```python
def test():
    global o # variable que hace referencia a la o externa
    o = 5
    print(o)
test()
​o=10
test()
print(o)
# 5
# 5
# 5
```

[Volver al inicio](#-funciones)