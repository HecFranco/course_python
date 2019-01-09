# Argumentos y parámetros indeterminados

Quizá en alguna ocasión no sabemos de antemano cuantos elementos vamos a enviar a una función. En estos casos podemos utilizar los parámetros indeterminados por posición y por nombre.

[Volver al inicio](#-argumentos-y-parámetros-indeterminados)

## POR POSICIÓN

---------------------------------------------------------------------------

Para recibir un número indeterminado de parámetros por posición, debemos crear una lista dinámica de argumentos (una tupla en realidad):

```python
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
indeterminados_posicion(5,"Hola",[1,2,3,4,5])
# 5
# Hola
# [1, 2, 3, 4, 5]
```

[Volver al inicio](#-argumentos-y-parámetros-indeterminados)

## POR NOMBRE

---------------------------------------------------------------------------

Para recibir un número indeterminado de parámetros por nombre (clave-valor), debemos crear un diccionario dinámico de argumentos:

```python
def indeterminados_nombre(**kwargs):
    print(kwargs)
indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5])    
# {'n': 5, 'c': 'Hola', 'l': [1, 2, 3, 4, 5]}
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5])   
# n
# c
# l
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg," ", kwargs[kwarg])
indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5])   
# n   5
# c   Hola
# l   [1, 2, 3, 4, 5]
```

[Volver al inicio](#-argumentos-y-parámetros-indeterminados)

## POR POSICIÓN Y NOMBRE A LA VEZ

---------------------------------------------------------------------------

Si queremos aceptar ambos tipos de parámetros simultáneamente, entonces debemos crear ambas colecciones dinámicas:

```python
def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("Sumatorio indeterminado es",t)
    for kwarg in kwargs:
        print(kwarg," ", kwargs[kwarg])
​
super_funcion(10,50,-1,1.56,10,20,300,nombre="Hector",edad=27)
# Sumatorio indeterinado es 390.56
# nombre   Hector
# edad   27
```

[Volver al inicio](#-argumentos-y-parámetros-indeterminados)