# Invocación de excepciones
En algunas ocasiones quizá nos interesa llamar un error manualmente, ya que un print común no es muy elegante:

```python
def mi_funcion(algo=None):
    if algo is None:
        print("Error! No se permite un valor nulo (con un print)")
mi_funcion("algo")
mi_funcion()
# Error! No se permite un valor nulo (con un print)
```

[Volver al inicio](#-invocación-de-excepciones)

## INSTRUCCIÓN RAISE

---------------------------------------------------------------------------

Gracias a la instrucción `raise` podemos lanzar un error manual pasándole el identificador. Luego simplemente podemos añadir un `except` para tratar esta excepción que hemos lanzado:

```python
def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error! No se permite un valor nulo")
    except ValueError:
        print("Error! No se permite un valor nulo (desde la excepción)")
mi_funcion()
Error! No se permite un valor nulo (desde la excepción)
```

[Volver al inicio](#-invocación-de-excepciones)