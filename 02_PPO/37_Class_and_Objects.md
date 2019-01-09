# Clases y Objetos

[Volver al inicio](#-clases-y-objetos)

## DEFINICION DE CLASE

---------------------------------------------------------------------------

Una **clase** es una plantilla para la creación de objetos de datos según un modelo predefinido.

* Las **clases** se utilizan para representar **entidades** o **conceptos*+, como los sustantivos en el lenguaje. 
* Cada **clase** es un modelo que define un conjunto de variables -el estado, y métodos apropiados para operar con dichos datos -el comportamiento. 

Los objetos se definen mediante la palabra reservada `class`. Estas clases definiran el molde a partir del cual se crearan (instanciaran) nuevos objetos.

```python
class Galleta:
    pass
```

[Volver al inicio](#-clases-y-objetos)

## INSTANCIAS

---------------------------------------------------------------------------

Una **instancia** (en inglés, instance) es la particularización, realización específica u ocurrencia de una determinada clase, entidad (modelo entidad-relación) o prototipo.

> **NOTA**: Cada **objeto** creado a partir de la clase se denomina instancia de la clase.

**Instanciar** un clase 
```python
una_galleta = Galleta()
otra_galleta = Galleta()
```

[Volver al inicio](#-clases-y-objetos)

## FUNCIÓN TYPE()

---------------------------------------------------------------------------

La función `type()` sirve para determinar la clase de un objeto.

```python
class Galleta:
    pass

una_galleta = Galleta()

type(una_galleta)
# __main__.Galleta
type(10)
# int
type(3.14)
# float
type("Hola")
# str
type([])
# list
type({})
# dict
type(True)
# bool
def hola():
    pass
type(hola)
# function
```

[Volver al inicio](#-clases-y-objetos)