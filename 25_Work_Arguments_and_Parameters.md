# Trabajando con argumentos y parámetros

[Volver al inicio](#-trabajando-con-argumentos-y-parámetros)

## ARGUMENTOS POR POSICIÓN

---------------------------------------------------------------------------

```python
def resta(a,b):
    return a-b
​resta(1,2)   # posición índice 0 valor 1, posición índice 1 valor 2
# -1
```

[Volver al inicio](#-trabajando-con-argumentos-y-parámetros)

## ARGUMENTOS POR NOMBRE

---------------------------------------------------------------------------

```python
resta(b=2,a=1)
# -1
```

[Volver al inicio](#-trabajando-con-argumentos-y-parámetros)


## LLAMADA SIN ARGUMENTOS

---------------------------------------------------------------------------

Al llamar una función que tiene definidos unos parámetros, si no pasamos los argumentos correctamente provocará un error:

```python
resta()
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-4-78c8f433960e> in <module>()
# ----> 1 resta()
# TypeError: resta() missing 2 required positional arguments: 'a' and 'b'
```

[Volver al inicio](#-trabajando-con-argumentos-y-parámetros)


## PARÁMETROS POR DEFECTO

---------------------------------------------------------------------------

Para solucionarlo podemos asignar unos valores por defecto nulos a los parámetros, y de ésa forma podríamos hacer una comprobación antes de ejecutar el código de la función:

```python
def resta(a=None,b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return
    return a-b
resta(1,5)
# -4
```

[Volver al inicio](#-trabajando-con-argumentos-y-parámetros)