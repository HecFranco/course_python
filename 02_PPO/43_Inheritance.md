# Herencia

En programación orientada a objetos, la herencia es, después de la agregación o composición, el mecanismo más utilizado para alcanzar algunos de los objetivos más preciados en el desarrollo de software como lo son la reutilización y la extensibilidad. 

A través de ella, los diseñadores pueden crear nuevas clases partiendo de una clase o de una jerarquía de clases preexistente (ya comprobadas y verificadas) evitando con ello el rediseño, la modificación y verificación de la parte ya implementada. La herencia facilita la creación de objetos a partir de otros ya existentes e implica que una subclase obtiene todo el comportamiento (métodos) y eventualmente los atributos (variables) de su superclase.

## EJEMPLO SIN HERENCIA

---------------------------------------------------------------------------

Primeramente veamos como se definiría una nueva clase sin la posibilidad de usar herencias.

```python
class Producto:
    def __init__(self,referencia,tipo,nombre,pvp,descripcion,productor=None,distribuidor=None,isbn=None,autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor
        
adorno = Producto('000A','ADORNO','Vaso Adornado',15,'Vaso de porcelana con dibujos')   

adorno
# <__main__.Producto at 0x5243810>
adorno.tipo
# 'ADORNO'
```

[Volver al inicio](#-herencia)

## ESTEREOTIPOS DE HERENCIA

---------------------------------------------------------------------------

[Volver al inicio](#-herencia)

### HERENCIA SIMPLE

---------------------------------------------------------------------------

Una clase sólo puede heredar de una clase base y de ninguna otra.

[Volver al inicio](#-herencia)

### HERENCIA MÚLTIPLE

---------------------------------------------------------------------------

Una clase puede heredar las características de varias clases base, es decir, puede tener varios padres. En este aspecto hay discrepancias entre los diseñadores de lenguajes. Algunos de ellos han preferido no admitir la herencia múltiple debido a que los potenciales conflictos entre métodos y variables con igual nombre, y eventualmente con comportamientos diferentes crea un desajuste cognitivo que va en contra de los principio de la programación orientada a objetos. Por ello, la mayoría de los lenguajes orientados a objetos admite herencia simple. En contraste, algunos pocos lenguajes admiten herencia múltiple, entre ellos: C++, Python, Eiffel, mientras que Smalltalk, Java, Ada y C# sólo permiten herencia simple.

[Volver al inicio](#-herencia)

## CREANDO UNA JERARQUÍA DE PRODUCTOS CON CLASES

---------------------------------------------------------------------------

Ahora definiremos clases usando herencias. Para ello primeramnete crearemos una clase **Producto** con unas propiedades que lo definiran, así a partir de esta clase derivaran otros objetos que heredaran las propiedades de **Producto**, como es el caso de **Adorno**.

[Volver al inicio](#-herencia)

### SUPERCLASE PRODUCTO

---------------------------------------------------------------------------

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
```

[Volver al inicio](#-herencia)

### SUPERCLASE ADORNO

---------------------------------------------------------------------------

```python
class Adorno(Producto):
    pass
​a = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con árboles")
print(a)
```

[Volver al inicio](#-herencia)

### SUPERCLASE ALIMENTO

---------------------------------------------------------------------------

```python
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
        
    
al = Alimento(2035,"Botella de Aceite de Oliva Extra",5,"250 ML")
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"
​
print(al)
REFERENCIA	2035
NOMBRE		Botella de Aceite de Oliva Extra
PVP		5
DESCRIPCIÓN	250 ML
PRODUCTOR	La Aceitera
DISTRIBUIDOR	Distribuciones SA
```

[Volver al inicio](#-herencia)

### SUPERCLASE LIBRO

---------------------------------------------------------------------------

```python
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
    
li = Libro(2036,"Cocina Mediterránea",9,"Recetas sanas y buenas")
li.isbn = "0-123456-78-9"
li.autor = "Doña Juana"
​
print(li)
REFERENCIA	2036
NOMBRE		Cocina Mediterránea
PVP		9
DESCRIPCIÓN	Recetas sanas y buenas
ISBN		0-123456-78-9
AUTOR		Doña Juana
```

[Volver al inicio](#-herencia)