# BLOQUE 05

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

**1) Formatea los siguientes valores para mostrar el resultado indicado:**

* `"Hola Mundo"` → Alineado a la derecha en 20 caracteres
* `"Hola Mundo"` → Truncamiento en el cuarto carácter (índice 3)
* `"Hola Mundo"` → Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
* `150` → Formateo a 5 números enteros rellenados con ceros
* `7887` → Formateo a 7 números enteros rellenados con espacios
* `20.02` → Formateo a 3 números enteros y 3 números decimales


**2) Crea un script llamado tabla.py que realice las siguientes tareas:**

* Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
* El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
* En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
* El script contendrá un bucle for que itere el número de veces del primer argumento.
* Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
* Dentro del segundo for ejecuta una instrucción `print(" * ", end='')`, (`end=''` evita el salto de línea).

**Ejecuta el código y observa el resultado.**
**Ahora intenta deducir dónde y cómo añadir otra instruccion print para dibujar una tabla.**

> **RECORDATORIO**: Los argumentos se envían como cadenas separadas por espacios, si quieres enviar varias palabras como un argumento deberás indicarlas entre comillas dobles `"esto es un argumento"`. Para capturar los argumentos debes utilizar el módulo `sys` y su lista `argv`:

```python
import sys
print(sys.argv) # argumentos enviados
```

**3) [Avanzado] Crea un script llamado `descomposicion.py` que realice las siguientes tareas:**

* Debe tomar 1 argumento que será un número entero positivo.
* En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
**El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**

> 3647
**El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:**
> 0007
  0040
  0600
  3000

> **PISTA**: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa