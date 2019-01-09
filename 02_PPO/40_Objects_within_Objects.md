# Objetos en Objetos

```python
class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)
```

Creando un catálogo de películas

```python
class Catalogo:
    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula
    def __init__(self,peliculas=[]):
        self.peliculas = peliculas
    def agregar(self,p):  # p será un objeto Pelicula
        self.peliculas.append(p)
    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)
p = Pelicula("El Padrino",175,1972)
c = Catalogo([p])
# Se ha creado la película: El Padrino
c.mostrar()
# El Padrino (1972)

c.agregar(Pelicula("El Padrino: Parte 2",202,1974))  # Añadimos una película directamente
# Se ha creado la película: El Padrino: Parte 2

c.mostrar()
# El Padrino (1972)
# El Padrino: Parte 2 (1974)
```

[Volver al inicio](#-objetos-en-objetos)