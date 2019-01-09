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

**5) Realiza una función llamada `agregar_una_vez()` que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:**

`Error: Imposible añadir elementos duplicados => [elemento].`
**Prueba de agregar los elementos `10`, `-2`, `"Hola"` a la lista de elementos con la función una vez la has creado y luego muestra su contenido.**

> **NOTA**: Puedes utilizar la sintaxis: elemento in lista

```python
elementos = [1, 5, -2]
​```