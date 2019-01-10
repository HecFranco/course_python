# El módulo pickle

El módulo de **pickle** implementa un algoritmo fundamental, pero potente, para la **serialización** y **deserialización** de una estructura de objetos Python. 

> **NOTA**: Serializar consiste en un proceso de codificación de un objeto en un medio de almacenamiento (como puede ser un archivo, o un buffer de memoria) con el fin de transmitirlo a través de una conexión en red como una serie de bytes o en un formato humanamente más legible como **XML** o **JSON**, entre otros.

[Volver al inicio](#-el-módulo-pickle)

## GUARDAR ESTRUCTURA EN FICHERO BINARIO

---------------------------------------------------------------------------

```python
import pickle
lista = [1,2,3,4,5] # Podemos guardar lo que queramos, listas, diccionarios, tuplas...
fichero = open('lista.pckl','wb') # Escritura en modo binario, vacía el fichero si existe
pickle.dump(lista, fichero) # Escribe la estructura en el fichero 
fichero.close()
```

[Volver al inicio](#-el-módulo-pickle)

## RECUPERAR ESTRUCTURA DE FICHERO BINARIO

---------------------------------------------------------------------------

```python
import pickle
fichero = open('lista.pckl','rb') # Lectura en modo binario
lista_fichero = pickle.load(fichero)
print(lista_fichero)
# [1, 2, 3, 4, 5]
```

[Volver al inicio](#-el-módulo-pickle)

## LÓGICA PARA TRABAJAR CON OBJETOS

---------------------------------------------------------------------------

* Crear una colección
* Introducir los objetos en la colección
* Guardar la colección haciendo un dump
* Recuperar la colección haciendo un load
* Seguir trabajando con nuestros objetos

```python
class Persona:

    def __init__(self,nombre):
        self.nombre = nombre
        
    def __str__(self):
        return self.nombre
​
nombres = ["Héctor","Mario","Marta"]
personas = []
​
for n in nombres:
    p = Persona(n)
    personas.append(p)
    
import pickle
f = open('personas.pckl','wb')
pickle.dump(personas, f)
f.close()

f = open('personas.pckl','rb')
personas = pickle.load(f)
f.close()
for p in personas:
    print(p)
# Héctor
# Mario
# Marta
```

[Volver al inicio](#-el-módulo-pickle)