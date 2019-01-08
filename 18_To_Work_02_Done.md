# BLOQUE 04

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

**1) Realiza un programa que siga las siguientes instrucciones:**

* Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
* Crea un conjunto llamado administradores con los administradores Juan y Marta.
* Borra al administrador Juan del conjunto de administradores.
* Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
* Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
> **NOTA**: Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista. También cuentan con un método llamado .discard(elemento) que sirve para borrar un elemento.

​**PASOS A SEGUIR**

1. Creamos un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos.

```python
# Completa el ejercicio aquí
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
```

2. Creamos un conjunto llamado administradores con los administradores Juan y Marta.

```diff
# Completa el ejercicio aquí
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
++ administradores = {"Juan", "Marta"}
```

3. Borramos al administrador Juan del conjunto de administradores.

```diff
# Completa el ejercicio aquí
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
++ administradores.discard("Juan")
```

4. Añadimos a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.

```diff
# Completa el ejercicio aquí
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
administradores.discard("Juan")
++ administradores.add("Marcos")
```

5. Mostramos mediante un `for` todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.

```diff
# Completa el ejercicio aquí
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
administradores.discard("Juan")
administradores.add("Marcos")
++ for usuario in usuarios:
++     if usuario in administradores:
++         print(usuario, "es admin")
++     else:
++         print(usuario, "no es admin")
```

El código final será así:

```python
# Completa el ejercicio aquí
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
administradores.discard("Juan")
administradores.add("Marcos")
for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "es admin")
    else:
        print(usuario, "no es admin")
```

**2) Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:**

* El caballero tiene el doble de vida y defensa que un guerrero.
* El guerrero tiene el doble de ataque y alcance que un caballero.
* El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
* Muestra como quedan las propiedades de los tres personajes.

```python
caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
```

caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }

​**PASOS A SEGUIR**

1. Empezamos cumpleindo la primera condición, **El caballero tiene el doble de vida y defensa que un guerrero.**:

```python
# Completa el ejercicio aquí
caballero['vida']    = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2
```

2. El guerrero tiene el doble de ataque y alcance que un caballero.

```diff
# Completa el ejercicio aquí
caballero['vida']    = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2
++ guerrero['ataque']   = caballero['ataque'] * 2
++ guerrero['alcance']  = caballero['alcance'] * 2
```

3. El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.

```diff
# Completa el ejercicio aquí
caballero['vida']    = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2
guerrero['ataque']   = caballero['ataque'] * 2
guerrero['alcance']  = caballero['alcance'] * 2
++ arquero['vida']     = guerrero['vida']
++ arquero['ataque']   = guerrero['ataque']
++ arquero['defensa']  = guerrero['defensa'] / 2
++ arquero['alcance']  = guerrero['alcance'] * 2
```

4. Ahora mostramos los resultados:

```diff
# Completa el ejercicio aquí
caballero['vida']    = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2
guerrero['ataque']   = caballero['ataque'] * 2
guerrero['alcance']  = caballero['alcance'] * 2
arquero['vida']     = guerrero['vida']
arquero['ataque']   = guerrero['ataque']
arquero['defensa']  = guerrero['defensa'] / 2
arquero['alcance']  = guerrero['alcance'] * 2
++ print("Caballero:\t", caballero)
++ print("Guerrero:\t", guerrero)
++ print("Arquero:\t", arquero)
```

El código final será así:

```python
# Completa el ejercicio aquí
caballero['vida']    = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2

guerrero['ataque']   = caballero['ataque'] * 2
guerrero['alcance']  = caballero['alcance'] * 2

arquero['vida']     = guerrero['vida']
arquero['ataque']   = guerrero['ataque']
arquero['defensa']  = guerrero['defensa'] / 2
arquero['alcance']  = guerrero['alcance'] * 2

print("Caballero:\t", caballero)
print("Guerrero:\t", guerrero)
print("Arquero:\t", arquero)
```

**3) Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).**

**¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?**

> **PISTA**: Para ordenar automáticamente una lista es posible utilizar el método `.sort()`.

```python
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]
​
print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])
```
​
```bash
==Tareas desordenadas==
6 Distribución
2 Diseño
1 Concepción
7 Mantenimiento
4 Producción
3 Planificación
5 Pruebas
```

​**PASOS A SEGUIR**

1. Cargamos el array de tareas inicial:

```python
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]
```

2. Añadimos un `print`que muestre el siguiente texto `==Tareas desordenadas==`:

```diff
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

++ print("==Tareas desordenadas==")
```

3. Recorremos mediante un for la lista:

```diff
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("==Tareas desordenadas==")
++ for tarea in tareas:
++     print(tarea[0], tarea[1])
```

4. Ordenamos la lista de datos:

```diff
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]
print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])
++ tareas.sort()
```

5. Importamos `deque` de la librería `collection` y creamos una cola vacía.

```diff
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]
print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])
tareas.sort()    
++ from collections import deque
++ cola = deque()
```

6. Recorremos el array ordenado para incluirlo dentro de la cola:

```diff
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]
print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])
tareas.sort()    
from collections import deque
cola = deque()
++ for tarea in tareas:
++     cola.append(tarea[1])
```

7. Ahora recorremos el listado ya ordenado:

```diff
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]
print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])
tareas.sort()    
from collections import deque
cola = deque()
for tarea in tareas:
    cola.append(tarea[1])
++ print("\n==Tareas ordenadas==")
++ for tarea in cola:
++     print(tarea)
```

El código final será así:

```python
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])

# Completa el ejercicio aquí
from collections import deque

tareas.sort()

cola = deque()
for tarea in tareas:
    cola.append(tarea[1])

print("\n==Tareas ordenadas==")
for tarea in cola:
    print(tarea)
```