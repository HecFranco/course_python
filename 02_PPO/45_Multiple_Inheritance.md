# Herencia múltiple

Posibilidad de que una subclase herede de múltiples superclases.

El problema aparece cuando las superclases tienen atributos o métodos comunes.

En estos casos, Python dará prioridad a las clases más a la izquierda en el momento de la declaración de la subclase.

```python
class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este método lo heredo de A")

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este método lo heredo de B")
class C(B,A):
    def c(self):
        print("Este método es de C")

c = C()
# Soy de clase B
c.a()
# Este método lo heredo de A
c.b()
# Este método lo heredo de B
c.c()
# Este método es de C
```