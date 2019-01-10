# El módulo collections

Este módulo implementa tipos de datos de contenedores especializados que proporcionan alternativas a los contenedores, `dict`, `list`, `set` y `tuple` integrados de propósito general de **Python**.

[Volver al inicio](#-método-collections)

## CONTADOR

---------------------------------------------------------------------------

Es una subclase de diccionario utilizada para realizar cuentas, y devuelve el número de repeticiones que cada elemento distinto tiene en una cadena o string.

```python
from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]
Counter(l)
# Counter({1: 4, 2: 3, 3: 2, 4: 1})
p = "palabra"
Counter(p)
# Counter({'a': 3, 'b': 1, 'l': 1, 'p': 1, 'r': 1})
animales = "gato perro canario perro canario perro"
Counter(animales)
# Counter({'r': 8, 'o': 6, 'a': 5, ' ': 5, 'p': 3, 'e': 3, 'c': 2, 'n': 2, 'i': 2, 'g': 1, 't': 1})
animales.split()
# ['gato', 'perro', 'canario', 'perro', 'canario', 'perro']
Counter(animales.split())
# Counter({'canario': 2, 'gato': 1, 'perro': 3})
```

Mediante el método `.most_common()`obtendremos como respuesta el contador de repeticiones de los elementos de la siguiente manera.

```python
from collections import Counter

c = Counter(animales.split())
c.most_common(1)
# [('perro', 3)]
c.most_common(2)
# [('perro', 3), ('canario', 2)]
c.most_common()
# [('perro', 3), ('canario', 2), ('gato', 1)]
```

Además existen los siguientes métodos asociados a **Counter**.

```python
from collections import Counter

l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l)
c.items()
# dict_items([(40, 1), (10, 4), (20, 3), (30, 2)])
c.keys()
# dict_keys([40, 10, 20, 30])
c.values()
# dict_values([1, 4, 3, 2])
sum(c.values())
# 10
list(c)
# [40, 10, 20, 30]
dict(c)
# {10: 4, 20: 3, 30: 2, 40: 1}
```

> **NOTA**: Dentro de un diccionario no se pueden extraer el `.most_common()`.

```python
from collections import Counter

l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l)
d = dict(c)
d.most_common(1)
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-30-4fdd6ba29964> in <module>()
# ----> 1 d.most_common(1)
# AttributeError: 'dict' object has no attribute 'most_common'
set(c)
# {10, 20, 30, 40}
```

[Volver al inicio](#-método-collections)

## DICCIONARIOS CON VALOR POR DEFECTO

---------------------------------------------------------------------------

Se utilizan para crear diccionarios con un valor por defecto aunque el registro no haya sido definido anteriormente.

```python
d = {}
d['algo']
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-38-c4e2998bb821> in <module>()
# ----> 1 d['algo']
# KeyError: 'algo'
```          

```python
from collections import defaultdict

d = defaultdict(float)
d['algo']
# 0.0
d
# defaultdict(float, {'algo': 0.0})
d = defaultdict(str)
d['algo']
# ''
d
# defaultdict(str, {'algo': ''})
d = defaultdict(object)
d['algo']
# <object at 0x1ad7f3201f0>
d
# defaultdict(object, {'algo': <object at 0x1ad7f3201f0>})
d = defaultdict(int)
d['algo'] = 10.5
d['algo']
# 10.5
d['algomas']
# 0
d
# defaultdict(int, {'algo': 10.5, 'algomas': 0})
n = {}
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
n
# {'dos': 'two', 'tres': 'three', 'uno': 'one'}
```

[Volver al inicio](#-método-collections)

## DICCIONARIOS ORDENADOS

---------------------------------------------------------------------------

Otra subclase de diccionario que conserva el orden en que añadimos los registros.

```python
from collections import OrderedDict

n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
n
# OrderedDict([('uno', 'one'), ('dos', 'two'), ('tres', 'three')])
n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'
​n2 = {}
n2['dos'] = 'two'
n2['uno'] = 'one'
n1 == n2
# True
n1 = OrderedDict()
n1['uno'] = 'one'
n1['dos'] = 'two'
​n2 = OrderedDict()
n2['dos'] = 'two'
n2['uno'] = 'one'
n1 == n2
# False
```

[Volver al inicio](#-método-collections)

## TUPLAS CON NOMBRES

---------------------------------------------------------------------------

Subclase de las tuplas utilizada para crear pequeñas estructuras inmutables, parecidas a una clase y sus objetos pero mucho más simples.

```python
t = (20,40,60)
t[0]
# 20
t[-1]
# 60
```

```python
from collections import namedtuple

Persona = namedtuple('Persona','nombre apellido edad')
p = Persona(nombre="Hector",apellido="Costa",edad=27)
p.nombre
# 'Hector'
p.apellido
# 'Costa'
p.edad
# 27
p
Persona(nombre='Hector', apellido='Costa', edad=27)
p[0]
# 'Hector'
p[1]
# 'Costa'
p[-1]
# 27
p.nombre = "Hola"
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-91-5cd7aba08457> in <module>()
# ----> 1 p.nombre = "Hola"
# AttributeError: can't set attribute
```

[Volver al inicio](#-método-collections)