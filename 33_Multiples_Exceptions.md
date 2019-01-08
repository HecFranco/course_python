# Capturando múltiples excepciones

[Volver al inicio](#-capturando-múltiples-excepciones)

## GUARDANDO L EXCEPCIÓN

---------------------------------------------------------------------------

Podemos asignar una excepción a una variable (por ejemplo `e`). De esta forma haciendo un pequeño truco podemos analizar el tipo de error que sucede gracias a su identificador:

```python
try:
    n = input("Introduce un número: ")
    5/n
except Exception as e:
    print( type(e).__name__ )
# Introduce un número: 10
# TypeError
```

[Volver al inicio](#-capturando-múltiples-excepciones)

## ENCADENANDO EXCEPCIONES

---------------------------------------------------------------------------

Gracias a los identificadores de errores podemos crear múltiples comprobaciones, siempre que dejemos en último lugar la excepción por defecto Excepcion que engloba cualquier tipo de error (si la pusiéramos al principio, las demas excepciones nunca se ejecutarían):

```python
try:
    n = float(input("Introduce un número: "))
    5/n
except TypeError:
    print("No se puede dividir el número por una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print( type(e).__name__ )
# Introduce un número: aaaa
# ValueError
```

[Volver al inicio](#-capturando-múltiples-excepciones)