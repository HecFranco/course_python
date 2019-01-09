# BLOQUE 10

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

**1) Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:**

```bash
un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
En este otro:
```
```pre
Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
```

> **NOTA**: Lo único prohibido es modificar directamente el texto

```python
texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
```

**PASOS A SEGUIR**

1. Copiamos la cadena de texto inicial:

```python
# Completa el ejercicio aquí
texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
```

2.  Separamos la cadena en subcadenas a partir del caracter designado y devolvemos una lista:

```diff
# Completa el ejercicio aquí
texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

++ lineas = texto.split("#")
```

3. Incluimos la lógica de separación del string ya splitteado:

```diff
# Completa el ejercicio aquí
texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

lineas = texto.split("#")
++ for i, linea in enumerate(lineas):
++     lineas[i] = linea.capitalize()
++     if i == 0:
++         lineas[i] = lineas[i] + "..."
++     else:
++         lineas[i] = "- " + lineas[i] + "."
```

4. Mostramos el texto ya formateado:

```diff
# Completa el ejercicio aquí
texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

lineas = texto.split("#")
for i, linea in enumerate(lineas):
    lineas[i] = linea.capitalize()
    if i == 0:
        lineas[i] = lineas[i] + "..."
    else:
        lineas[i] = "- " + lineas[i] + "."

++ # Mostramos el texto final
++ for linea in lineas:
++     print(linea)
```

El código final será así:

```python
# Completa el ejercicio aquí
texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

lineas = texto.split("#")
for i, linea in enumerate(lineas):
    lineas[i] = linea.capitalize()
    if i == 0:
        lineas[i] = lineas[i] + "..."
    else:
        lineas[i] = "- " + lineas[i] + "."

# Mostramos el texto final
for linea in lineas:
    print(linea)
```

**2) Crea una función `modificar()` que a partir de una lista de números realice las siguientes tareas sin modificar la original:**
```pre
Borrar los elementos duplicados
Ordenar la lista de mayor a menor
Eliminar todos los números impares
Realizar una suma de todos los números que quedan
Añadir como primer elemento de la lista la suma realizada
Devolver la lista modificada
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )
> True
```

> **NOTA**: La función `sum(lista)` devuelve una suma de los elementos de una lista

```python
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
```

**PASOS A SEGUIR**

1. Copiamos el array de números inicial:

```python
# Completa el ejercicio aquí
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
```

2. Incluimos el método:


```diff
# Completa el ejercicio aquí
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

++ def modificar(l):
  
++     l = list(set(l))  # Borrar los elementos duplicados (recrea la lista a partir de un nuevo diccionario)
++     l.sort(reverse=True)  # Ordenar la lista de mayor a menor
 
++     l_tmp = []  # Lista temporal que contendrá solo los números pares
++     for n in l:
++         if n%2 == 0:
++             l_tmp.append(n)
            
++     suma = sum(l_tmp)  # Realizar una suma de todos los números que quedan
++     l_tmp.insert(0, suma)  # Añadir como primer elemento de la lista de pares la suma realizada
++     return l_tmp  # Devolver la lista de pares modificada
```

3. Incluimos en una variable el resultado de la función, y lo imprimimos:

```diff
# Completa el ejercicio aquí
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(l):
  
    l = list(set(l))  # Borrar los elementos duplicados (recrea la lista a partir de un nuevo diccionario)
    l.sort(reverse=True)  # Ordenar la lista de mayor a menor
 
    l_tmp = []  # Lista temporal que contendrá solo los números pares
    for n in l:
        if n%2 == 0:
            l_tmp.append(n)
            
    suma = sum(l_tmp)  # Realizar una suma de todos los números que quedan
    l_tmp.insert(0, suma)  # Añadir como primer elemento de la lista de pares la suma realizada
    return l_tmp  # Devolver la lista de pares modificada

++ nueva_lista = modificar(lista)
++ print( nueva_lista[0] == sum(nueva_lista[1:]) )
```

El código final será así:

```diff
# Completa el ejercicio aquí
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(l):
  
    l = list(set(l))  # Borrar los elementos duplicados (recrea la lista a partir de un nuevo diccionario)
    l.sort(reverse=True)  # Ordenar la lista de mayor a menor
 
    l_tmp = []  # Lista temporal que contendrá solo los números pares
    for n in l:
        if n%2 == 0:
            l_tmp.append(n)
            
    suma = sum(l_tmp)  # Realizar una suma de todos los números que quedan
    l_tmp.insert(0, suma)  # Añadir como primer elemento de la lista de pares la suma realizada
    return l_tmp  # Devolver la lista de pares modificada


nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )
```
