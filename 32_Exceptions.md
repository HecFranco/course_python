# Las excepciones

Son bloques de código excepcionales que nos permiten continuar con la ejecución de un programa pese a que ocurra un error.

Siguiendo con el ejemplo de la lección anterior
Teníamos el caso en que leíamos un número por teclado, pero el usuario no introducía un número:

```python
n = float(input("Introduce un número: "))
m = 4
print("{}/{}={}".format(n,m,n/m))
# Introduce un número: aaa
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-1-c0e7fd4a26a9> in <module>()
# ----> 1 n = float(input("Introduce un número: "))
#       2 m = 4
#       3 print("{}/{}={}".format(n,m,n/m))
# ValueError: could not convert string to float: 'aaa'
```

[Volver al inicio](#-las-excepciones)

## CREANDO LA EXCEPCIÓN - BLOQUES TRY Y EXCEPT

---------------------------------------------------------------------------

Para prevenir el error, debemos poner el código propenso a error un bloque `try` y luego encadenaremos un bloque `except` para tratar la excepción:

```python
try:
    n = float(input("Introduce un número: "))
    m = 4
    print("{}/{}={}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduce bien el número")
# Introduce un número: aaa
# Ha ocurrido un error, introduce bien el número
```

Utilizando un `while(true)`, podemos asegurárnos de que el usuario introduce bien el valor
Repitiendo la lectura por teclado hasta que lo haga bien, y entonces rompemos el bucle con un `break`:

```python
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
        break  # Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduce bien el número")
# Introduce un número: aaa
# Ha ocurrido un error, introduce bien el número
# Introduce un número: sdsdsd
# Ha ocurrido un error, introduce bien el número
# Introduce un número: sdsdsd
# Ha ocurrido un error, introduce bien el número
# Introduce un número: sdsd
# Ha ocurrido un error, introduce bien el número
# Introduce un número: 10
# 10.0/4=2.5
```

[Volver al inicio](#-las-excepciones)

## BLOQUE ELSE EN EXCEPCIONES

---------------------------------------------------------------------------

Es posible encadenar un bloque else después del except para comprobar el caso en que todo funcione correctamente (no se ejecuta la excepción).

El bloque `else` es un buen momento para romper la iteración con break si todo funciona correctamente:

```python
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien
# Introduce un número: 10
# 10.0/4=2.5
# Todo ha funcionado correctamente
```

[Volver al inicio](#-las-excepciones)

## BLOQUE FINALLY EN EXCEPCIONES

---------------------------------------------------------------------------

Por último es posible utilizar un bloque `finally` que se ejecute al final del código, ocurra o no ocurra un error:

```python
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien
    finally:
        print("Fin de la iteración") # Siempre se ejecuta
# Introduce un número: aaa
# Ha ocurrido un error, introduce bien el número
# Fin de la iteración
# Introduce un número: 10
# 10.0/4=2.5
# Todo ha funcionado correctamente
# Fin de la iteración
```

[Volver al inicio](#-las-excepciones)