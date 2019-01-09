# Métodos especiales de clase

[Volver al inicio](#-constructor-y-destructor)

## CONSTRUCTOR Y DESTRUCTOR

---------------------------------------------------------------------------

Aunque existe un debate bastante acalorado con respecto a la existencia o no de constructor en **Python** el método `init()` puede ser lo más próximo a un constructor. 

> **NOTA**: Un constructor básicamente hay que entenderlo como **una última oportunidad de modificar las propiedades de un objeto antes de ser finalmente creado**.

```python
class Pelicula:
    # Constructor de clase (al crear la instancia)
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película",self.titulo)
    # Destructor de clase (al borrar la instancia)
    def __del__(self):
        print("Se está borrando la película", self.titulo)
p = Pelicula("El Padrino",175,1972)
# Se ha creado la película El Padrino
```

Al reinstanciar la misma variable se crea de nuevo y se borra la anterior

```python
p = Pelicula("El Padrino",175,1972)
# Se ha creado la película El Padrino
# Se está borrando la película El Padrino
```

[Volver al inicio](#-constructor-y-destructor)

## __STR__(SELF)

---------------------------------------------------------------------------

```python
class Pelicula:
    # Constructor de clase (al crear la instancia)
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película",self.titulo)
    # Destructor de clase (al borrar la instancia)
    def __del__(self):
        print("Se está borrando la película", self.titulo)

p = Pelicula("El Padrino",175,1972)
p
# <__main__.Pelicula at 0x20bb8318fd0>
str(10)
# '10'
str(p)
# '<__main__.Pelicula object at 0x0000020BB8318FD0>'
```

El método `__str__(self)` permite devolver una cadena por defecto al convertir un objeto a una cadena con `str(objeto)`.

```python
class Pelicula:
    # Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película",self.titulo)
    # Destructor de clase
    def __del__(self):
        print("Se está borrando la película", self.titulo)
    # Redefinimos el método string
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(self.titulo,self.lanzamiento,self.duracion) 
p = Pelicula("El Padrino",175,1972)
# Se ha creado la película El Padrino
str(p)
# 'El Padrino lanzada en 1972 con una duración de 175 minutos'
```

[Volver al inicio](#-constructor-y-destructor)

## __LEN__(SELF)

---------------------------------------------------------------------------

El método `Length` permite devolver un número que simula la longitud del objeto `len(objeto)`. 

```python
len(p)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-16-503cac95e140> in <module>()
# ----> 1 len(p)
# TypeError: object of type 'Pelicula' has no len()

class Pelicula:
    # Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película",self.titulo)
    # Destructor de clase
    def __del__(self):
        print("Se está borrando la película", self.titulo)
    # Redefinimos el método string
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)
    # Redefinimos el método length
    def __len__(self):
        return self.duracion
        
p = Pelicula("El Padrino",175,1972)
len(p)
# Se ha creado la película El Padrino
# Se está borrando la película El Padrino
# 175
```

[Volver al inicio](#-constructor-y-destructor)