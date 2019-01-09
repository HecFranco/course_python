# Atributos y métodos de clase

Los **Atributos** hacen referencia a las variables internas de la clase.
Los **Métodos** hacen referencia a las funciones internas de la clase.

```python
class Galleta:
    pass
​una_galleta = Galleta()
```

[Volver al inicio](#-atributos-y-métodos-de-clase)

## DEFINICIÓN DE ATRIBUTOS DINÁMICOS EN LOS OBJETOS

---------------------------------------------------------------------------

A continuación veremos una forma de definir valores de los atributos dinámicos de las clases en los **Objetos**:

```python
class Galleta:
    pass

​una_galleta = Galleta()

una_galleta.sabor = "Salado"
una_galleta.color = "Marrón"
print("El sabor de esta galleta es ",una_galleta.sabor)
# El sabor de esta galleta es Salado
```

[Volver al inicio](#-atributos-y-métodos-de-clase)

## DEFINICIÓN DE ATRIBUTOS EN LA CLASE

---------------------------------------------------------------------------

A continuación veremos una forma de definir valores de los atributos dinámicos de las clases en la **Clase**:

```python
class Galleta:
    chocolate = False

​g = Galleta()

g.chocolate
# False
g.chocolate = True
g.chocolate
# True
```

[Volver al inicio](#-atributos-y-métodos-de-clase)

## MÉTODO INIT()

---------------------------------------------------------------------------

El método `init()` se llama automáticamente al crear una instancia de clase.

> **NOTA**: El método `init()` en las clases se asemeja a los constructores en otros lenguajes.

```python
class Galleta():
    chocolate = False
    # Constructor de clase (al crear la instancia)
    def __init__(self):
        print("Se acaba de crear una galleta.")
g = Galleta()
# Se acaba de crear una galleta.
```

[Volver al inicio](#-atributos-y-métodos-de-clase)

## MÉTODOS Y LA PALABRA SELF

---------------------------------------------------------------------------

la palabra reservada `Self` sirve para hacer referencia a los métodos y atributos base de una clase dentro de sus propios métodos.

> **NOTA**: La palabra reservada `Self` se asemeja a `this` en otros lenguajes.

```python
class Galleta():
    chocolate = False
    # Constructor de clase (al crear la instancia)
    def __init__(self):
        print("Se acaba de crear una galleta.")
    def chocolatear(self):
        self.chocolate = True
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")
g = Galleta()
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()
# Se acaba de crear una galleta.
# Soy una galleta sin chocolate :-(
# Soy una galleta chocolateada :-D
```

[Volver al inicio](#-atributos-y-métodos-de-clase)

## PARÁMETROS EN EL INIT(argumentos al instanciar)

---------------------------------------------------------------------------

Podremos incluir los parámetros que definan los atributos de la clase dentro de `init()`, de esta forma al instancia la clase para crear un nuevo objeto podremos asignarle unos valores que lo definan.

```python
class Galleta():
    chocolate = False
    # Constructor de clase (al crear la instancia)
    def __init__(self, sabor, forma):
        self.sabor = sabor
        self.forma = forma
        print("Se acaba de crear una galleta {} y {}".format(sabor,forma))
    def chocolatear(self):
        self.chocolate = True
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")
g = Galleta("salada","cuadrada")
# Se acaba de crear una galleta salada y cuadrada
```

[Volver al inicio](#-atributos-y-métodos-de-clase)

## PARÁMETROS CON VALORES POR DEFECTO EN EL INIT()

---------------------------------------------------------------------------

Al igual que en otros lenguajes la definición de parámetros en una clase pueden tener valores por defecto los cuales entran a funcionar cuando no se designan.

```python
class Galleta():
    chocolate = False    
    # Constructor de clase (al crear la instancia)
    def __init__(self, sabor, forma):
        self.sabor = sabor
        self.forma = forma
        print("Se acaba de crear una galleta {} y {}".format(sabor,forma))
    def chocolatear(self):
        self.chocolate = True
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")
g = Galleta()
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-20-bfd19da23fef> in <module>()
# ----> 1 g = Galleta()
# TypeError: __init__() missing 2 required positional arguments: 'sabor' and 'color'
```
```python
class Galleta():
    chocolate = False
        # Constructor de clase (al crear la instancia)
    def __init__(self, sabor=None, forma=None):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print("Se acaba de crear una galleta {} y {}".format(sabor,forma))
    def chocolatear(self):
        self.chocolate = True
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")
g = Galleta("salada","cuadrada")
# Se acaba de crear una galleta salada y cuadrada
```

[Volver al inicio](#-atributos-y-métodos-de-clase)