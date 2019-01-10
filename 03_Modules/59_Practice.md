# Práctica

[Volver al inicio](#-el-módulo-pickle)

## CATÁLAGO DE PELÍCULAS CON FICHEROS Y PICKLE

---------------------------------------------------------------------------

```python
from io import open
import pickle
​
class Pelicula:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)
        
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)
​
​
class Catalogo:
    
    peliculas = []
    
    # Constructor de clase
    def __init__(self):
        self.cargar()
        
    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()
        
    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return
        for p in self.peliculas:
            print(p)
            
    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            del(fichero)
            print("Se han cargado {} películas".format( len(self.peliculas) ))
    
    def guardar(self):
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()
        del(fichero)
    
    # Destructor de clase
    def __del__(self):
        self.guardar()  # guardado automático
        print("Se ha guardado el fichero")
```

[Volver al inicio](#-el-módulo-pickle)

## CREANDO UN OBJETO CATÁLOGO

---------------------------------------------------------------------------

```python
c = Catalogo()
# El fichero está vacío
# Se han cargado 0 películas
c.mostrar()
# El catálogo está vacío
c.agregar( Pelicula("El Padrino", 175, 1972) )
# Se ha creado la película: El Padrino
c.agregar( Pelicula("El Padrino: Parte 2", 202, 1974) )
# Se ha creado la película: El Padrino: Parte 2
c.mostrar()
# El Padrino (1972)
# El Padrino: Parte 2 (1974)
del(c)
# Recuperando el catálogo al crearlo de nuevo
c = Catalogo()
# Se han cargado 2 películas
c.mostrar()
# El Padrino (1972)
# El Padrino: Parte 2 (1974)
del(c)
# Se ha guardado el fichero
c = Catalogo()
# Se han cargado 2 películas
c.agregar( Pelicula("Prueba", 100, 2005) )
# Se ha creado la película: Prueba
c.mostrar()
# El Padrino (1972)
# El Padrino: Parte 2 (1974)
# Prueba (2005)
del(c)
# Se ha guardado el fichero
c = Catalogo()
# Se han cargado 3 películas
c.mostrar()
# El Padrino (1972)
# El Padrino: Parte 2 (1974)
# Prueba (2005)
```

[Volver al inicio](#-el-módulo-pickle)

## CONCLUSIONES

---------------------------------------------------------------------------

* Trabajamos en memoria, no en el fichero
* Nosotros decidimos cuando escribir los datos:
* Al manipular un registro
* Al finalizar el programa
