# Trabajando con clases heredadas en conjunto

```python
class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)
​
class Adorno(Producto):
    pass
​​
class Alimento(Producto):
    productor = ""
    distribuidor = ""
    
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)
​
​
class Libro(Producto):
    isbn = ""
    autor = ""
    
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
ISBN\t\t{}
AUTOR\t\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)
```

[Volver al inicio](#-trabajando-con-clases-heredadas-en-conjunto)

## CREAMOS ALGUNOS OBJETOS

---------------------------------------------------------------------------

```python
ad = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con árboles")
​
al = Alimento(2035,"Botella de Aceite de Oliva Extra",5,"250 ML")
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"
​
li = Libro(2036,"Cocina Mediterránea",9,"Recetas sanas y buenas")
li.isbn = "0-123456-78-9"
li.autor = "Doña Juana"
```

[Volver al inicio](#-trabajando-con-clases-heredadas-en-conjunto)

## LISTA DE PRODUCTOS

---------------------------------------------------------------------------

```python
productos = [ad, al]
productos.append(li)
productos
# [<__main__.Adorno at 0x14c58660940>,
#  <__main__.Alimento at 0x14c586608d0>,
#  <__main__.Libro at 0x14c58660978>]
```

[Volver al inicio](#-trabajando-con-clases-heredadas-en-conjunto)

## LECTURA SECUENCIAL DE PRODUCTS CON UN `FOR... IN`

---------------------------------------------------------------------------

```python
for p in productos:
    print(p,"\n")
# REFERENCIA	2034
# NOMBRE		Vaso adornado
# PVP		15
# DESCRIPCIÓN	Vaso de porcelana adornado con árboles 

# REFERENCIA	2035
# NOMBRE		Botella de Aceite de Oliva Extra
# PVP		5
# DESCRIPCIÓN	250 ML
# PRODUCTOR	La Aceitera
# DISTRIBUIDOR	Distribuciones SA 

# REFERENCIA	2036
# NOMBRE		Cocina Mediterránea
# PVP		9
# DESCRIPCIÓN	Recetas sanas y buenas
# ISBN		0-123456-78-9
# AUTOR		Doña Juana 
```

Podemos acceder a los atributos si son compartidos entre todos los objetos

```python
for p in productos:
    print(p.referencia, p.nombre)
# 2034 Vaso adornado
# 2035 Botella de Aceite de Oliva Extra
# 2036 Cocina Mediterránea
```

Pero si un objeto no tiene el atributo deseado, dará error:

```python
for p in productos:
    print(p.autor)
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-8-36e9baf5c1cc> in <module>()
#       1 for p in productos:
# ----> 2     print(p.autor)
# AttributeError: 'Adorno' object has no attribute 'autor'
```

Tendremos que tratar cada subclase de forma distinta, gracias a la función isistance():

```python
for p in productos:
    if( isinstance(p, Adorno) ):
        print(p.referencia,p.nombre)
    elif( isinstance(p, Alimento) ):
        print(p.referencia,p.nombre,p.productor)
    elif( isinstance(p, Libro) ):
        print(p.referencia,p.nombre,p.isbn)        
# 2034 Vaso adornado
# 2035 Botella de Aceite de Oliva Extra La Aceitera
# 2036 Cocina Mediterránea 0-123456-78-9
```

[Volver al inicio](#-trabajando-con-clases-heredadas-en-conjunto)

## FUNCIONES QUE RECIBEN OBJETOS DE DISTINTAS CLASES

---------------------------------------------------------------------------

> **NOTA**: Los objetos se envían por referencia a las funciones
Así que debemos tener en cuenta que cualquier cambio realizado dentro afectará al propio objeto.

```python
def rebajar_producto(p, rebaja):
    """Rebaja un producto en porcentaje de su precio"""
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
​rebajar_producto(al, 10)
print(al_rebajado)
# REFERENCIA	2038
# NOMBRE		Botella de Aceite de Oliva Extra
# PVP		4.5
# DESCRIPCIÓN	250 ML
# PRODUCTOR	La Aceitera
# DISTRIBUIDOR	Distribuciones SA
print(al)
# REFERENCIA	2035
# NOMBRE		Botella de Aceite de Oliva Extra
# PVP		4.5
# DESCRIPCIÓN	250 ML
# PRODUCTOR	La Aceitera
# DISTRIBUIDOR	Distribuciones SA
```

Una copia de un objeto también hace referencia al objeto copiado (como un acceso directo)

```python
copia_al = al
copia_al.referencia = 2038
print(copia_al)
# REFERENCIA	2038
# NOMBRE		Botella de Aceite de Oliva Extra
# PVP		4.5
# DESCRIPCIÓN	250 ML
# PRODUCTOR	La Aceitera
# DISTRIBUIDOR	Distribuciones SA
print(al)
# REFERENCIA	2038
# NOMBRE		Botella de Aceite de Oliva Extra
# PVP		4.5
# DESCRIPCIÓN	250 ML
# PRODUCTOR	La Aceitera
# DISTRIBUIDOR	Distribuciones SA
```

Esto también sucede con los tipos compuestos:

```python
l = [1,2,3]
l2 = l[:]
l2.append(4)
l
# [1, 2, 3, 4]
```

Para crear una copia `100%` nueva debemos utilizar el módulo copy:

```python
import copy
​copia_ad = copy.copy(ad)
print(copia_ad)
# REFERENCIA	2034
# NOMBRE		Vaso adornado
# PVP		15
# DESCRIPCIÓN	Vaso de porcelana adornado con árboles
copia_ad.pvp = 25
print(copia_ad)
# REFERENCIA	2034
# NOMBRE		Vaso adornado
# PVP		25
# DESCRIPCIÓN	Vaso de porcelana adornado con árboles
print(ad)
# REFERENCIA	2034
# NOMBRE		Vaso adornado
# PVP		15
# DESCRIPCIÓN	Vaso de porcelana adornado con árboles
```

[Volver al inicio](#-trabajando-con-clases-heredadas-en-conjunto)

## POLIMORFISMO

---------------------------------------------------------------------------

Se refiere a una propiedad de la herencia por la que objetos de distintas subclases pueden responder a una misma acción.

```python
def rebajar_producto(p, rebaja):
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
```

El método `rebajar_producto()` es capaz de tomar objetos de distintas subclases y manipular el atributo `pvp`.

La acción de manipular el pvp funcionará siempre que los objetos tengan ése atributo, pero en el caso de no ser así, daría error.

La polimorfia es implícita en Python en todos los objetos, ya que todos son hijos de una superclase común llamada Object.

[Volver al inicio](#-trabajando-con-clases-heredadas-en-conjunto)