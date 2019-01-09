# BLOQUE 09

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

**En este ejercicio vas a trabajar el concepto de herencia un poco más en profundidad, aprovechando para introducir un nuevo concepto muy importante que te facilitará mucho la vida.**

**Hasta ahora sabemos que una clase heredada puede fácilmente extender algunas funcionalidades, simplemente añadiendo nuevos atributos y métodos, o sobreescribiendo los ya existentes. Como en el siguiente ejemplo**

```python
class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc".format( self.color, self.velocidad, self.ruedas, self.cilindrada )

c = Coche("azul", 150, 4, 1200)
print(c)
# Color azul, 4 km/h, 150 ruedas, 1200 cc
```

**El inconveniente más evidente de ir sobreescribiendo es que tenemos que volver a escribir el código de la superclase y luego el específico de la subclase.**

**Para evitarnos escribir código innecesario, podemos utilizar un truco que consiste en llamar el método de la superclase y luego simplemente escribir el código de la clase:**

```diff
class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
--      self.color = color
--      self.ruedas = ruedas    
++      Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
--      return "color {}, {} km/h, {} ruedas, {} cc".format( self.color, self.velocidad, self.ruedas, self.cilindrada )    
++      return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

c = Coche("azul", 4, 150, 1200)
print(c)
# Color azul, 4 ruedas, 150 km/h, 1200 cc
```

> **NOTA**: Como tener que determinar constantemente la superclase puede ser fastidioso, Python nos permite utilizar un acceso directo mucho más cómodo llamada `super()`. Hacerlo de esta forma además nos permite llamar cómodamente los métodos o atributos de la superclase sin necesidad de especificar el `self`.

```diff
class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
--      Vehiculo.__init__(self, color, ruedas)    
++      super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
--      return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)    
++      return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
​
c = Coche("azul", 4, 150, 1200)
print(c)
# color azul, 4 ruedas, 150 km/h, 1200 cc
```

## EJERCICIO

Utilizando esta nueva técnica, extiende la clase Vehiculo y realiza la siguiente implementación: 

### Experimenta

* Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
* Realiza una función llamada `catalogar()` que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
* Modifica la función `catalogar()` para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje `"Se han encontrado {} vehículos con {} ruedas:"` únicamente si se envía el argumento ruedas. Ponla a prueba con `0`, `2` y `4` ruedas como valor.

> **RECORDATORIO**: Puedes utilizar el atributo especial de clase `name` de la siguiente forma para recuperar el nombre de la clase de un objeto:

```python
type(objeto).__name__
```

```diff
class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super()
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


# Completa el ejercicio aquí

-- class Camioneta():
++ class Camioneta(Coche):
--  pass
++  def __init__(self, color, ruedas, velocidad, cilindrada, carga):
++      super().__init__(color, ruedas, velocidad, cilindrada) 
++      self.carga = carga

++  def __str__(self):
++      return super().__str__() + ", {} kg de carga".format(self.carga)

-- class Bicicleta():
++ class Bicicleta(Vehiculo):
--  pass
++  def __init__(self, color, ruedas, tipo):
++      super().__init__(color, ruedas) 
++      self.tipo = tipo

++  def __str__(self):
++      return super().__str__() + ", {}".format(self.tipo)

-- class Motocicleta():
++ class Motocicleta(Bicicleta):
--  pass
++  def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
++      super().__init__(color, ruedas, tipo) 
++      self.velocidad = velocidad
++      self.cilindrada = cilindrada

++  def __str__(self):
++      return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


++ vehiculo = [
++  Coche("azul", 4, 150, 1200),
++  Camioneta("blanco", 4, 150, 1200, 1500),
++  Bicicleta("verde", 4, "urbana"),
++  Motocicleta("negro", 4, "deportiva", 100, 900),
++ ]

-- def catalogar():
++ def catalogar(lista):
--  pass
++  for v in lista:
++      print("{} {}".format(type(v).__name__, v))

++ catalogar(vehiculos)
```

Ampliamos el ejercicio:

```diff
class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super()
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


# Completa el ejercicio aquí

class Camioneta(Coche):
 def __init__(self, color, ruedas, velocidad, cilindrada, carga):
     super().__init__(color, ruedas, velocidad, cilindrada) 
     self.carga = carga

 def __str__(self):
     return super().__str__() + ", {} kg de carga".format(self.carga)

class Bicicleta(Vehiculo):
 def __init__(self, color, ruedas, tipo):
     super().__init__(color, ruedas) 
     self.tipo = tipo

 def __str__(self):
     return super().__str__() + ", {}".format(self.tipo)

class Motocicleta(Bicicleta):
 def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
     super().__init__(color, ruedas, tipo) 
     self.velocidad = velocidad
     self.cilindrada = cilindrada

 def __str__(self):
     return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


-- def catalogar(lista):
++ # def catalogar(lista):
--  for v in lista:
++ #  for v in lista:
--      print("{} {}".format(type(v).__name__, v))
++ #      print("{} {}".format(type(v).__name__, v))

++ def catalogar(vehiculos, ruedas=None):
      
++     # Primera pasada, mostrar recuento
++     if ruedas != None:
++         contador = 0
++         for v in vehiculos:
++             if v.ruedas == ruedas: 
++                 contador += 1
++         print("\nSe han encontrado {} vehículos con {} ruedas:".format(contador, ruedas))
    
++     # Segunda pasada, mostrar vehículos
++     for v in vehiculos:
++         if ruedas == None:
++             print(type(v).__name__, v)
++         else:
++             if v.ruedas == ruedas:
++                 print(type(v).__name__, v)

lista = [
    Coche("azul", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

catalogar(lista)

++ catalogar(lista, 0)
++ catalogar(lista, 2)
++ catalogar(lista, 4)
```