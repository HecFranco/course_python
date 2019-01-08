# BLOQUE 07

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

**1) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**

```python
resultado = 10/0
# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-13-fa18751f1091> in <module>()
#       1 # Completa el ejercicio aquí
# ----> 2 resultado = 10/0
# ZeroDivisionError: division by zero
```

**PASOS A SEGUIR**

El código final será así:

```python
try:
    resultado = 10/0
except ZeroDivisionError:
    print("Error: No es posible dividir por cero, debes introducir un número distinto.")
```

**2) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**

```python
lista = [1, 2, 3, 4, 5]
lista[10]
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-14-04f772275640> in <module>()
#       1 # Completa el ejercicio aquí
#       2 lista = [1, 2, 3, 4, 5]
# ----> 3 lista[10]
# IndexError: list index out of range
```

**PASOS A SEGUIR**

El código final será así:

```python
# Completa el ejercicio aquí
lista = [1, 2, 3, 4, 5]
try:
    lista[10]
except IndexError:
    print("Error: El índice al que intentas acceder se encuentra fuera del rango, debes utilizar un número mayor o igual que cero y menor que la longitud de la lista.")
```

**3) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**

```python
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
colores['blanco']
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-11-9316804f855a> in <module>()
#       1 # Completa el ejercicio aquí
#       2 colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
# ----> 3 colores['blanco']
# KeyError: 'blanco'
```

**PASOS A SEGUIR**

El código final será así:

```python
# Completa el ejercicio aquí
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
try:
    colores['blanco']
except KeyError:
    print("Error: La clave del diccionario no se encuentra, debes probar con otra que sí exista.")
```

**4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**

```python
resultado = 15 + "20"
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-10-4c554866ea5f> in <module>()
#       1 # Completa el ejercicio aquí
# ----> 2 resultado = 15 + "20"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

**PASOS A SEGUIR**

El código final será así:

```python
# Completa el ejercicio aquí
try:
    resultado = "20" + 15
except TypeError:
    print("Error: Sólo es posible sumar datos del mismo tipo, debes transformar el número a cadena o la cadena a número.")
```

**5) Realiza una función llamada `agregar_una_vez()` que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:**

`Error: Imposible añadir elementos duplicados => [elemento].`
**Prueba de agregar los elementos `10`, `-2`, `"Hola"` a la lista de elementos con la función una vez la has creado y luego muestra su contenido.**

> **NOTA**: Puedes utilizar la sintaxis: elemento in lista

```python
elementos = [1, 5, -2]
```

**PASOS A SEGUIR**

1. Copiamos el array inicial:

```python
elementos = [1, 5, -2]

# Completa el ejercicio aquí
```

2. Incluimos el método que recoge los parámetros y en función de estos discretiza el error:

```diff
elementos = [1, 5, -2]

# Completa el ejercicio aquí
++ def agregar_una_vez(lista, el):
++     try:
++         if el in lista:
++             raise ValueError
++         else:
++             lista.append(el)
++     except ValueError:
++         print("Error: Imposible añadir elementos duplicados =>", el)
```

3. Probamos el método con distintas opciones:

```diff
elementos = [1, 5, -2]

# Completa el ejercicio aquí
def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError
        else:
            lista.append(el)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados =>", el)

++ agregar_una_vez(elementos, 10)
++ agregar_una_vez(elementos, -2)
++ agregar_una_vez(elementos, "Hola")
print(elementos)
```

4. Imprimimos la lista:

```diff
elementos = [1, 5, -2]

# Completa el ejercicio aquí
def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError
        else:
            lista.append(el)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados =>", el)
        
agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")
++ print(elementos)
```

El código final será así:

```python
elementos = [1, 5, -2]

# Completa el ejercicio aquí
def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError
        else:
            lista.append(el)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados =>", el)

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")
print(elementos)
```