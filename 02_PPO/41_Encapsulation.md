# Encapsulación

La **Encapsulación** consiste en denegar el acceso a los atributos y métodos internos de la clase desde el exterior.

En **Python** no existe, pero se puede simular precediendo atributos y métodos con dos barras bajas `__`:

```python
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera"
    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera")
e = Ejemplo()
e.__atributo_privado
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-3-73328dd71c23> in <module>()
# ----> 1 e.__atributo_privado
# AttributeError: 'Ejemplo' object has no attribute '__atributo_privado'
e.__metodo_privado()
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-4-164c67db4a9b> in <module>()
# ----> 1 e.__metodo_privado()
# AttributeError: 'Ejemplo' object has no attribute '__metodo_privado'
```

[Volver al inicio](#-encapsulación)

## COMO ACCEDER

---------------------------------------------------------------------------

Internamente la clase sí puede acceder a sus atributos y métodos encapsulados, el truco consiste en crear sus **equivalentes "publicos"**:

```python
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera"
    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera")
    def atributo_publico(self):
        return self.__atributo_privado
    def metodo_publico(self):
        return self.__metodo_privado()
e = Ejemplo()
e.atributo_publico()
# 'Soy un atributo inalcanzable desde fuera'
e.metodo_publico()
# Soy un método inalcanzable desde fuera
```

[Volver al inicio](#-encapsulación)